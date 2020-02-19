import PIL
from PIL import Image
from io import BytesIO
import re

def resize(s3_client, bucket, original_key, width, height, suffix):
    obj = s3_client.get_object(Bucket=bucket, Key=original_key)

    full_size_key = original_key.replace('__incoming/', '')
    ext = re.sub(r'.+\.([^.]+)$', r'\1', full_size_key)
    key = re.sub(r'\.[^.]+$', '', full_size_key)
    content_type = obj['ContentType']

    if content_type == 'image/png':
        image_type = 'PNG'
    elif content_type == 'image/jpg' or content_type == 'image/jpeg':
        image_type = 'JPEG'
    else:
        raise Exception(f'Invalid image type: {content_type}')

    obj_body = obj['Body'].read()
    img = Image.open(BytesIO(obj_body))
    img = img.resize((width, height), PIL.Image.ANTIALIAS)
    buffer = BytesIO()
    img.save(buffer, image_type)
    buffer.seek(0)

    resized_key=f"{key}-{suffix}.{ext}"

    # write the resized image
    obj = s3_client.put_object(
        Key=resized_key,
        Bucket=bucket,
        Body=buffer,
        ContentType=content_type,
        ACL='public-read')

    # move the original out of __incoming
    s3_client.copy_object(
        Bucket=bucket,
        Key=full_size_key,
        CopySource=f'{bucket}/{original_key}',
        ACL='public-read')
    s3_client.delete_object(Bucket=bucket, Key=original_key)

    app.log.debug("resized: %s, key: %s",
                  bucket, key)