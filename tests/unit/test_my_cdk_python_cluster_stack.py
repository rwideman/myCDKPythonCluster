import aws_cdk as core
import aws_cdk.assertions as assertions

from my_cdk_python_cluster.my_cdk_python_cluster_stack import MyCdkPythonClusterStack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_cdk_python_cluster/my_cdk_python_cluster_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyCdkPythonClusterStack(app, "my-cdk-python-cluster")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
