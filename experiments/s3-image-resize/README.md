# client

    cd client
    python -m http.server

# API

Update environment variables (`BUCKET_NAME`)

    cp .chalice/config.json.example .chalice/config.json

Uploads are sent in prefixed with `__incoming`. Once they are processed, they are moved to their final destination. this application will create a copy of any images uploaded to 320x180 as the same filename with `-thumb` added before the extension name. Images with the same prefix, path and filename as existing files are overwritten. File names are normalized to lowercase, a-z0-9-. characters only.

All files are uploaded with public read access.
