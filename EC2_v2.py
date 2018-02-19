import boto3
import argparse
import sys

class EC2():
    def __init__(self):
        pass

    def createInstance(self):
        if len(sys.argv) < 1:
            print "There are no arguments specified, using the default parameters" ##If there are no arguments or options used, then prints out that default will be used
        args = self.argParse() ##Parses the args
        self.EC2Config(args) ##passes the parsed args to the configuration function

    def argParse(self):
        p = argparse.ArgumentParser()
        p.add_argument('--VolumeSize', default=8,required=False) ##Defines volumeSize
        p.add_argument('--VolumeType', default='standard',required=False) ##Defines volumeType
        p.add_argument('--InstanceType', default='t2.micro', required=False) ##Defines InstanceType
        p.add_argument('--ImageId', default='ami-97785bed', required=False) ##Defines ImageID
        p.add_argument('--AZ', default='us-east-1a', required=False) ##Defines AZ Zone
        p.add_argument('--SubnetId', default='', required=False) ##Defines Subnet
        p.add_argument('--SecurityGroupIds', default='', required=False) ##Defines list of Security Groups
        p.add_argument('--UseConfig', action='store_true', default=False)
        a = p.parse_args() ##Parses the arguments as a namespace
        print 'Setting up instance with the following arguments: '
        for key,value in vars(a).iteritems(): ##Converts namespace to Dict
            print "{} : {}".format(key, value) #Prints Dict key value pairs
        return a ##Returns the parsed arguments

    def EC2Config(self,args):
        if args.UseConfig == False:  ##If user does not specifies to Use Config
            region = args.AZ ##Defines the region
            session = boto3.Session(aws_access_key_id='YOUR_KEY', aws_secret_access_key='YOUR_KEY', region_name=region[:-1]) ##input the connection credentials
            inst = session.resource('ec2')  ##createing the session and connecting to resource
        else:
            print "Using Credentials at ~/.aws/credentials"
            inst = boto3.resource('ec2')  ##Uses config at ~/.aws/credentials
        if args.SecurityGroupIds is None or args.SecurityGroupIds == '':
            secGroups = [] ##If there are no security groups defined, use empty list, which is equal to default parameter
        else:
            secGroups = args.SecurityGroupIds.split(',') ##Split the list given for Security Groups, convert to list
        bootstrap = """
                    #!/bin/bash 
                    yum -y update
                    yum -y install httpd
                    chkconfig httpd on
                    service httpd start;
                    echo "AWS Automation is Fun!" > /var/www/html/index.html
                    """ ##Boot Strap Script for installing necessary items (apache, updates, etc)
        inst.create_instances(
            ImageId=args.ImageId,
            InstanceType=args.InstanceType,
            BlockDeviceMappings=[{'DeviceName':'/dev/xvda','Ebs':{'VolumeSize':int(args.VolumeSize), 'VolumeType':args.VolumeType}}],
            Placement={'AvailabilityZone':args.AZ},
            UserData=bootstrap,
            SubnetId=args.SubnetId,
            SecurityGroupIds=secGroups,
            MinCount=1,
            MaxCount=1
        ) ##Start the provisionsing

c = EC2().createInstance() ##Creating objects and calling the functions