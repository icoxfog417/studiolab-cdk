import aws_cdk as core
import aws_cdk.assertions as assertions

from studiolab_cdk.studiolab_cdk_stack import StudiolabCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in studiolab_cdk/studiolab_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StudiolabCdkStack(app, "studiolab-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
