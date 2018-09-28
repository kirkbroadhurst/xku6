import os


def handle_event(event, context):
    "Return the variable specified in cloudformation template"
    return os.environ['TestValue']
