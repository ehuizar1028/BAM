README:  
Script Info:  
Python 2.7  
Boto3 Package  
  
There are no required parameters. Ensure that AWS access/secret keys are configured for programmatic access via IAM.  
A list will be outputted with manual defined parameters. Any empty parameters mean it's using the default parameter.  
Public IP address is automatically assigned.  
NOTE: ACCESS/SECRET KEYS ARE HARDCODED. THIS IS NOT BEST PRACTICE, I REMOVED MY KEYS AND REPLACED THEM WITH OBVIOUS VALUES. 
I've created V2 of the script, to add additional features and to separate my original submission.

USAGE:  
python EC2.py --ARG=VALUE    
--VolumeSize = Size of the EBS Volume, in GB  
--VolumeType = Type of volume  
--InstanceType = Instance Type  
--ImageId = ID of Amazon AMI image  
--AZ = Availability Zone  
--SubnetId = ID of subnet (this would also assign the VPC of wherever the subnet's VPC assigned to)  
--SecurityGroupIds = List of Security Groups. Comma Separated  
--UseConfig = Uses credentials found at ~/.aws/credentials (Only in EC2_v2.py)

EXAMPLE:  
python EC2.py --VolumeSize=8 --VolumeType=standard --InstanceType=t2.micro --ImageId=ami-97785bed --AZ=us-east-1a --SubnetId=5ubn3t1d --SecurityGroupIds=53cur,1tyGr0,uP1D5