title: CloudFormation parameters
slug: cloudformation-parameters
category: Software
date: 2018-10-03


Sometimes you want to deploy your CloudFormation templates in a way that results in specific and different configuration per stack. Perhaps you deploy to a production stack and a development stack and need to flag a different logging value. Maybe your stacks connect to different databases, or expect a different authentication token. To achieve any of these you will want to pass some parameter to CloudFormation that can be used in the deployment.

Following on from my recent post on [lambda variables with CloudFormation](https://xku6.com/2018/09/28/cloudformation-variables/) - where I passed an environment variable to a lambda function - I have a need to actually parameterize the value of that variable. So when I deploy to a stack, I want to be able to provide a value that will be available to the functions within that stack.

CloudFormation provides the ability to add parameters during the [`deploy`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deploy/index.html) command. We can provide these to the API command using the `--parameter-overrides` option, and they will be templated or injected into the template and ultimately end up inside a lambda, as part of an API Gateway method or resource, or in any other component that is deployed via CloudFormation. Let's see how it works.

## Example template

Define a parameter in a CloudFormation template as simply as this:
```yaml
#### `template.cfn.yml`
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Parameters:
  TestValueParam:
    Type: String
    Description: The value to be provided to lambda function environment

Resources:
  MyLambdaFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: .
      Environment:
        Variables:
          TestValue: !Ref TestValueParam
      Handler: handlers.handle_event
      Runtime: python3.6
```
To note here (and compare with the [previous version](https://xku6.com/2018/09/28/cloudformation-variables/))
- the `Parameters` section defines the expected parameters, and
- the parameter value is referenced by `!Ref TestValueParam` during deploy


## Including parameters in `deploy`

If we run the simple deployment commands we'll get an error:
```
$ aws cloudformation package --template-file template.cfn.yml \
    --output-template-file template-xfm.cfn.yml --s3-bucket us-east-1-embassy-test
$ aws cloudformation deploy --template-file template-xfm.cfn.yml --stack-name my-stack \
    --region us-east-1 --capabilities CAPABILITY_IAM

An error occurred (ValidationError) when calling the CreateChangeSet operation: 
Parameters: [TestValueParam] must have values
```
We need to specify the value of the `TestValueParam` parameter:
```
aws cloudformation deploy --template-file template-xfm.cfn.yml --stack-name my-stack \
    --region us-east-1 --parameter-overrides TestValueParam="hi!" --capabilities CAPABILITY_IAM
```


## Additional options
The [parameters section](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) allows you to specify
- default values, so you wouldn't need to provide a value
- `AllowedValues` and `AllowedPatterns` against which your value will be verified.
- `MinValue` and `MaxValue` for numeric types
- `MinLength` and `MaxLength` for string types

Very easy, very useful. Now we can build high automated deployments based on - for example - git branches.
