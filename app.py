#!/usr/bin/env python3
import os
import aws_cdk as cdk
from my_cdk_python_cluster.my_cdk_python_cluster_stack import MyCdkPythonClusterStack


app = cdk.App()
MyCdkPythonClusterStack(app, "MyCdkPythonClusterStack",
    env=cdk.Environment(
        account='559050253205',
        region='us-east-1'
    ),
)

app.synth()
