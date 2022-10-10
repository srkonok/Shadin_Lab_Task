from jinja2 import Environment, FileSystemLoader
import boto3
import json
import logging
import signal
import requests
import os
import botocore
# Create SES client
ses = boto3.client('ses')

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def send_response(event, context, response_status, response_data):
    '''Send a resource manipulation status response to CloudFormation'''
    response_body = {
        "Status": response_status,
        "Reason": "See the details in CloudWatch Log Stream: " + context.log_stream_name,
        "PhysicalResourceId": context.log_stream_name,
        "StackId": event['StackId'],
        "RequestId": event['RequestId'],
        "LogicalResourceId": event['LogicalResourceId'],
        "Data": response_data
    }

    LOGGER.info('ResponseURL: %s', event['ResponseURL'])
    LOGGER.info('ResponseBody: %s', response_body)

    # opener = build_opener(HTTPHandler)
    # request = Request(event['ResponseURL'], data=response_body)
    # request.add_header('Content-Type', '')
    # request.add_header('Content-Length', len(response_body))
    # request.get_method = lambda: 'PUT'
    # response = opener.open(request)

    response = requests.put(event['ResponseURL'], data=response_body)

    LOGGER.info("Status code: %s", response.status_code)
    LOGGER.info("Status message: %s", response.text)


def send_email(event, context):

    entries = os.listdir('templates/')

    file_loader = FileSystemLoader('templates')

    env = Environment(loader=file_loader)

    parent_dir = 'SubjectBody/'
                

    for entry in entries:
        entry_name = entry.split(".")[0]
        if entry_name != "header" and entry_name != "footer":
            loc = entry_name+'.json'
            path = os.path.join(parent_dir, loc)
            print(path)
            with open(path, 'r') as f:
                data = json.load(f, strict=False)
                template = env.get_template(entry)
                output = template.render()

                print(output)
                try:
                    # Create
                    response = ses.create_template(
                        Template={
                            'TemplateName': entry_name,
                            'SubjectPart': data[entry_name]['subject'],
                            'TextPart': data[entry_name]['text'],
                            'HtmlPart': output
                        }
                    )
                    try:
                        LOGGER.info('REQUEST RECEIVED:\n %s', event)
                        LOGGER.info('REQUEST RECEIVED:\n %s', context)
                        if event['RequestType'] == 'Create':
                            LOGGER.info('CREATE!')
                            send_response(event, context, "SUCCESS",
                                        {"Message": "Resource creation successful!"})
                        elif event['RequestType'] == 'Update':
                            LOGGER.info('UPDATE!')
                            send_response(event, context, "SUCCESS",
                                        {"Message": "Resource update successful!"})
                        elif event['RequestType'] == 'Delete':
                            LOGGER.info('DELETE!')
                            send_response(event, context, "SUCCESS",
                                        {"Message": "Resource deletion successful!"})
                        else:
                            LOGGER.info('FAILED!')
                            send_response(event, context, "FAILED",
                                        {"Message": "Unexpected event received from CloudFormation"})
                    except:  # pylint: disable=W0702
                        LOGGER.info('FAILED!')
                        send_response(event, context, "FAILED", {
                            "Message": "Exception during processing"})
                    print(response)
                except botocore.exceptions.ClientError as err:
                    if err.response['Error']['Code'] == 'AlreadyExists':
                        # Update
                        response = ses.update_template(
                            Template={
                                'TemplateName': entry_name,
                                'SubjectPart': data[entry_name]['subject'],
                                'TextPart': data[entry_name]['text'],
                                'HtmlPart': output
                            }
                        )
                        try:
                            LOGGER.info('REQUEST RECEIVED:\n %s', event)
                            LOGGER.info('REQUEST RECEIVED:\n %s', context)
                            if event['RequestType'] == 'Create':
                                LOGGER.info('CREATE!')
                                send_response(event, context, "SUCCESS",
                                            {"Message": "Resource creation successful!"})
                            elif event['RequestType'] == 'Update':
                                LOGGER.info('UPDATE!')
                                send_response(event, context, "SUCCESS",
                                            {"Message": "Resource update successful!"})
                            elif event['RequestType'] == 'Delete':
                                LOGGER.info('DELETE!')
                                send_response(event, context, "SUCCESS",
                                            {"Message": "Resource deletion successful!"})
                            else:
                                LOGGER.info('FAILED!')
                                send_response(event, context, "FAILED",
                                            {"Message": "Unexpected event received from CloudFormation"})
                        except:  # pylint: disable=W0702
                            LOGGER.info('FAILED!')
                            send_response(event, context, "FAILED", {
                                "Message": "Exception during processing"})
                        print(response)
                    elif err.response['Error']['Code'] == 'InvalidTemplate':
                        print("InvalidTemplateException")
                    elif err.response['Error']['Code'] == 'LimitExceeded':
                        print("LimitExceededException")
                    else:
                        print(err.response)
               
            

def lambda_handler(event, context):
    print(event)

    send_email(event, context)
