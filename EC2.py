import boto3
import argparse
import sys

class EC2():
    def __init__(self):
        pass

    def createInstance(self):
        if len(sys.argv) < 1:
            print "There are no arguments specified, using the default parameters"
        self.args = self.argParse()
        self.EC2Config(self.args)

    def argParse(self):
        p = argparse.ArgumentParser()
        p.add_argument('--VolumeSize', default=8,required=False)
        p.add_argument('--VolumeType', default='standard',required=False)
        p.add_argument('--InstanceType', default='t2.micro', required=False)
        p.add_argument('--ImageId', default='ami-97785bed', required=False)
        p.add_argument('--AZ', default='us-east-1a', required=False)
        p.add_argument('--SubnetId', default='', required=False)
        p.add_argument('--SecurityGroupIds', default='', required=False)
        a = p.parse_args()
        print 'Setting up instance with the following arguments: '
        for key,value in vars(a).iteritems():
            print "{} : {}".format(key, value)
        return a

    def EC2Config(self,args):

        if args.SecurityGroupIds is None or args.SecurityGroupIds == '':
            secGroups = []
        else:
            secGroups = args.SecurityGroupIds.split(',')
        print args.SecurityGroupIds
        bootstrap = """
                    #!/bin/bash 
                    yum -y update
                    yum -y install httpd
                    chkconfig httpd on
                    service httpd start;
                    echo "AWS Automation is Fun!" > /var/www/html/index.html
                    """
        inst = boto3.resource('ec2')
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
        )

c = EC2().createInstance()