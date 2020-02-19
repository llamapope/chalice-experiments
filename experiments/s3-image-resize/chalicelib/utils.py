from requests_toolbelt import MultipartDecoder
import re


# stop gap until chalice supports enctype=multipart/form-data natively...
# takes a chalice request, returns the (body, files) tuple representing the request
def parse_multipart(request):
    # decode the request
    decoder = MultipartDecoder(request.raw_body, request.headers['content-type'])

    body = {}
    files = {}

    # loop each part in the multipart upload
    for p in decoder.parts:
        data = p.content
        meta_data = {}

        # get the content type
        content_type = p.headers.get(b'content-type', b'').decode()
        if content_type:
            meta_data['content-type'] =  content_type

        # parse content disposition
        content_disposition = p.headers.get(b'content-disposition', b'').decode()
        if content_disposition:
            meta = content_disposition.split(';')

            for m in meta:
                m = re.sub(r'\s+', '', m)
                try:
                    # if there is a key value pair here, add to the meta_data for this field
                    k, v = m.split('=')
                    meta_data[k] = v.strip('"')
                except:
                    pass

            field_name = meta_data.get('name')

            # if there is no content-type, just store as a string
            if not meta_data.get('content-type'):
                meta_data = data.decode()

            multi_value_insert(body, field_name, meta_data)

            if type(meta_data) is dict and data:
                multi_value_insert(files, field_name, data)

    return (body, files)

# adds key/value to dict. If key already exists, converts
# existing value to array and appends incoming value to the array
def multi_value_insert(dictionary, key, value):
    if key in dictionary:
        if type(dictionary[key]) is list:
            dictionary[key] += [value]
        else:
            dictionary[key] = [dictionary[key]] + [value]
    else:
        dictionary[key] = value

# takes a path or URL and adds a suffix to the filename (before the extension)
def suffix_filename(string, suffix):
    ext = re.sub(r'.+\.([^.]+)$', r'\1', string)
    key = re.sub(r'\.[^.]+$', '', string)

    return f"{key}{suffix}.{ext}"
