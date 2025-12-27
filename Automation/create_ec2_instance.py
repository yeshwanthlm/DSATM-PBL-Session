import boto3

# Configuration
REGION = 'us-east-1'
INSTANCE_TYPE = 't3.micro'
AMI_ID = 'ami-0ecb62995f68bb549'  # Ubuntu 22.04 LTS

# Create EC2 client
ec2 = boto3.client('ec2', region_name=REGION)

# Launch instance
response = ec2.run_instances(
    ImageId=AMI_ID,
    MinCount=1,
    MaxCount=1,
    InstanceType=INSTANCE_TYPE,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'DSTAMServer'
                }
            ]
        }
    ]
)

instance_id = response['Instances'][0]['InstanceId']
print(f"Instance created: {instance_id}")
print(f"Region: {REGION}")
print(f"Instance Type: {INSTANCE_TYPE}")
print(f"OS: Ubuntu 22.04 LTS")
