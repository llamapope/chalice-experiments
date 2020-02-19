[back](../README.md)

# Common commands

Run local server (stage defaults to dev):

    chalice local
    chalice local --stage prod

Deploy (stage defaults to dev). Some services (s3, dynamodb, cloudwatch, etc...) only run in AWS and you must deploy the stage before your local version will work if it uses these AWS resources, otherwise they won't exist yet.

    chalice deploy
    chalice deploy --stage prod

Delete project from AWS (stage defaults to dev)

    chalice delete
    chalice delete --stage prod