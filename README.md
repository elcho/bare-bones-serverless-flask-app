## Deploy a Serverless Flask App in 5 Minutes

This is a basic example of how to deploy a flask app as a microservice on AWS Lambda using the Serverless framework.

### Initial Set-Up

1. Make sure you have node and npm installed on your machine and then run `npm install -g serverless`
2. Make sure you have a .aws folder in your home directory with a file `credentials`. In the file place a `profile`
block with the name of the profile you will be using with the correct aws credentials. In this example the profile name is `serverless-test`.
The structure of the block is:\
`[serverless-test]`\
`aws_access_key_id = your key here`\
`aws_secret_access_key = your key here`
3. For any project dependencies, you must have a requirements.txt file in the service directory. 
If you are using a python virtual environment (which is recommended) such as pipenv, you will need to install a plugin to
generate the file from the Pipfile (see the plugins section in the serverless.yml file -serverless-python-requirements):
`serverless plugin install -n serverless-python-requirements --profile serverless-test`. 
