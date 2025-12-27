import boto3
import sys

# Configuration
REGION = 'us-east-1'

# Get instance ID from command line argument
if len(sys.argv) != 2:
    print("Usage: python terminate_ec2_instance.py <instance-id>")
    sys.exit(1)

instance_id = sys.argv[1]

# Create EC2 client
ec2 = boto3.client('ec2', region_name=REGION)

# Terminate instance
response = ec2.terminate_instances(InstanceIds=[instance_id])

print(f"Terminating instance: {instance_id}")
print(f"Current state: {response['TerminatingInstances'][0]['CurrentState']['Name']}")
print(f"Previous state: {response['TerminatingInstances'][0]['PreviousState']['Name']}")
