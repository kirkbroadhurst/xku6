aws cloudformation package --template-file template.cfn.yml --output-template-file template-xfm.cfn.yml --s3-bucket us-east-1-embassy-test
aws cloudformation deploy --template-file template-xfm.cfn.yml --stack-name my-stack --region us-east-1 --parameter-overrides TestValueParam="hi!" --capabilities CAPABILITY_IAM
#aws cloudformation deploy --template-file template-xfm.cfn.yml --stack-name my-stack --region us-east-1 --capabilities CAPABILITY_IAM

