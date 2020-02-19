[back](../README.md)

# New Project Setup

    source ~/.chalice/venv/bin/activate
    chalice new-project experiment-name
    cd experiment-name
    deactivate # exit user chalice
    python3.7 -m venv venv

> Now if you are using multiple AWS profiles and went with option 2, this is when you would add the desired [AWS_PROFILE unset/export](aws-profile.md#option-2) to your virtual environment. Otherwise, continue with the setup ignoring this instruction.

    source venv/bin/activate
    pip install boto3 # or whatever else you want to use
    pip freeze > requirements.txt