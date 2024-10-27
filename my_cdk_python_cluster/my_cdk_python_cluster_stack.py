from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
import constants
from constructs import Construct

class MyCdkPythonClusterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self,
            "MyVpc",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public-subnet",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                )
            ],
        )
        
        sec_group = ec2.SecurityGroup(
            self, "MySecurityGroup", vpc=vpc, allow_all_outbound=True
        )
        
        sec_group.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "allow SSH access"
        )
        
        key_pair = ec2.KeyPair(self, "KeyPair",
            type=ec2.KeyPairType.ED25519,
            format=ec2.KeyPairFormat.PEM
        )
        
        num_instances = 3
        for n in range(0, num_instances):
            num_str = str(n)
            suffix = num_str.zfill(2)
            instance = ec2.Instance(
                self,
                'MyInstance{}'.format(suffix),
                instance_type=ec2.InstanceType(constants.INSTANCETYPE),
                machine_image=ec2.MachineImage.generic_linux(
                    ami_map={
                        "us-east-1": constants.AMIID
                    }
                ),
                vpc=vpc,
                security_group=sec_group,
                associate_public_ip_address=True,
                key_pair=key_pair
            )