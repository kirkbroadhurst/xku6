title: Lambda function environment variables with CloudFormation
slug: cloudformation-variables
category: Software
date: 2018-09-28


Automated deployments are a good idea, if only because deploying is tedious. Being able to reproduce something confidently, easily, and quickly is priceless.

I've recently had the need to deploy Lambda functions with some included parameters, so went out to learn about passing variables to CloudFormation and consuming those values inside Lambda.

When deploying simple components to AWS you have the option of using the simpler [Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model), or the more comprehensive CloudFormation model. I'll walk through the pros and cons at some other time, but for now note that SAM is really a subset of CF, and each is completely compatible with the other - your  templates can include SAM components and CF components side-by-side. Start with SAM and then go to CF when necessary.

---

Assuming a really simple Lambda function does something with a local variable - but you need to change or modify that variable during deployment (say per environment or instance).
```
def handle_event(event, context):
    "Return the variable specified in cloudformation template"
    some_value = 'hi guys' # <- want to replace/inject this value during deployment
    return some_value
```
Q: How do we handle environment specific variables? 
A: Using environment variables! 

## Code that uses environment variables

Luckily we are able to provide environment variables to our Lambda function (via CloudFormation) and access them in the usual Pythonic manner - for example we can include our Lambda function and CloudFormation template in small files such as:

```python
#### `handlers.py `
import os
def handle_event(event, context):
    "Return the variable specified in cloudformation template"  
    return os.environ['TestValue']
```
```yaml
#### `template.cfn.yml`
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MyLambdaFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: .
      Environment:
        Variables:
          TestValue: "hi guys"
      Handler: handlers.handle_event
      Runtime: python3.6
```
Some notes on this template:

 - We're creating just one resource, and are naming it `LambdaFunction`
 - The code for the function is in the same directory as this template, in a module named `handlers`in a method named `handle_event`
 - We are creating an environment variable named `TestValue`

## Deploying

To run this, make sure you have an IAM user with appropriate access (CloudFormation, S3, and Lambda permissions) and first run a package command:
```
aws cloudformation package --template-file template.cfn.yml \
  --output-template-file template-xfm.cfn.yml --s3-bucket my-bucket
```
This 'packages' the template, which means:
- uploads your code to S3 (the path specified in `CodeUri` above to the `s3-bucket` above
- creates a 'transformed template file' (`template-xfm.cfn.yml`) which can be deployed
- replace the `CodeUri` in your template with the new s3 location of that code
- other transformations which might need to take place (none apply here)

Then deploy using a command like this:
```
aws cloudformation deploy --template-file template-xfm.cfn.yml \
  --stack-name my-stack --region us-east-1 --capabilities CAPABILITY_IAM
```
This will
- take the 'transformed' template file and deploy it
- to the named region
- in a CloudFormation 'stack' named `my-stack`

A CloudFormation stack is something like a deployment group, and a way to relate resources back to a specific deployment (which could be an environment or instance).

## Next 

Hardcoding the value of the environment variable is far from ideal. Next post I'll show how to parameterize this within the `deploy` step.
