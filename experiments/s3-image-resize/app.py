from chalice import Chalice, Response
import boto3
import re
import os

from chalicelib.utils import parse_multipart, suffix_filename
from chalicelib.s3_helpers import resize

app = Chalice(app_name='s3-image-resize')

BUCKET = os.getenv('BUCKET_NAME')
s3_client = boto3.client('s3')


@app.route('/')
def index():
    return Response(
        body='<h1>POST /{prefix}</h1> Store uploaded files to s3 using the prefix and path specified. <h2>URL Params</h2>prefix: string <h2>Headers</h2>content-type: multipart/form-data<h2>Body</h2>files: file | [files]<br> path: string',
        headers={'Content-Type': 'text/html'}) 

@app.route('/upload/{prefix}', methods=['POST'], cors=True, content_types=['multipart/form-data'])
def upload(prefix):
    body, files = parse_multipart(app.current_request)
    pattern = r'[^a-z0-9.-]+'
    path_pattern = r'[^a-z0-9.-/]+'
    prefix = re.sub(pattern, '', prefix.lower())
    path = re.sub(path_pattern, '', body.get('path').lower())

    for key in files:
        field = files[key]

        # normalize for multiple parts with the same key
        if type(field) is not list:
            field = [field]
        
        for index, data in enumerate(field):
            meta = body[key][index]

            file_name = re.sub(pattern, '-', meta.get('filename').lower())
            file_name = re.sub(r'([\.-])+', r'\1', file_name)
            file_name = f'/{prefix}/{path}/{file_name}'

            s3_client.put_object(
                Bucket=BUCKET,
                Key=f"__incoming{file_name}",
                Body=data,
                ContentType=meta['content-type'])
            meta['filename'] = f'https://{BUCKET}.s3.amazonaws.com{file_name}'
            meta['thumb'] = suffix_filename(meta['filename'], '-thumb')

    return body

# process __incoming files
# only works when using chalice deploy
# https://chalice.readthedocs.io/en/latest/topics/events.html#s3-events
@app.on_s3_event(bucket=BUCKET, events=['s3:ObjectCreated:*'], prefix="__incoming/")
def handle_s3_event(event):
    resize(s3_client, event.bucket, event.key, 320, 180, '-thumb')
