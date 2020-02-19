[back](../README.md)

# AWS Profile

If you are using more than one AWS account, you will want to install the AWS CLI and configure named profiles for each account.

    python3.7 -m pip install --user awscli
    aws configure --profile your-aws-profile-name
    # enter IAM key, secret and default region

If you need to edit/review this, the profile is stored in your `~/.aws/config` file.

## Option 1

Set profile manually (per session or in `~/.bashrc` or equivalent)

    export AWS_PROFILE=your-aws-profile-name

## Option 2

This is to be done per virtual environment, assuming you DO NOT have AWS_PROFILE set in your environment already.

Modify the `venv/bin/activate` script for you virtual environment to set/unset this environment variable:
    
    # in the deactivate part of the script
    unset AWS_PROFILE

    # around the `export PATH` section, add this:
    export AWS_PROFILE=your-aws-profile-name

Save the file then activate and test that it is set correctly

    source venv/bin/activate
    echo $AWS_PROFILE # should be `your-aws-profile-name`
    deactivate
    echo $AWS_PROFILE # should be empty

Now when you activate the virtual environment your desired AWS profile will be used. This helps prevent using the wrong account accidently.