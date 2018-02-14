README:  
There are no required parameters. Ensure that AWS access/secret keys are configured for programmatic access via IAM.  
A list will be outputted with all parameters defined. Any empty parameters mean it's using the default parameter.  
Public IP address is automatically assigned.  
NOTE: ACCESS/SECRET KEYS ARE HARDCODED. THIS IS NOT BEST PRACTICE, I REMOVED MY KEYS AND REPLACED THEM WITH OBVIOUS VALUES.  

USAGE:  
python EC2.py --ARG=VALUE    
--VolumeSize = Size of the EBS Volume, in GB  
--VolumeType = Type of volume  
--InstanceType = Instance Type  
--ImageId = ID of Amazon AMI image  
--AZ = Availability Zone  
--SubnetId = ID of subnet (this would also assign the VPC of wherever the subnet's VPC assigned to)  
--SecurityGroupIds = List of Security Groups. Comma Separated  