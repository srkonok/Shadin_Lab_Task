from jinja2 import Environment, FileSystemLoader
import boto3
import json
import logging
import signal
import requests

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def send_response(event, context, response_status, response_data):
    '''Send a resource manipulation status response to CloudFormation'''
    response_body ={
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

    response=requests.put(event['ResponseURL'], data=response_body)

    LOGGER.info("Status code: %s", response.status_code)
    LOGGER.info("Status message: %s", response.text)

def send_email(event,context):

  file_loader = FileSystemLoader('template')

  env = Environment(loader=file_loader)

  template = env.get_template('lms_contact_us.html')

  output = template.render(name='Konok')

  print(output)
  # Create SES client
  ses = boto3.client('ses')

  response = ses.create_template(
    Template = {
      'TemplateName' : 'test1',
      'SubjectPart'  : 'SUBJECT_LINE',
      'TextPart'     : 'TEXT_CONTENT',
      'HtmlPart'     : output
    }
  )

  print(response)
  send_response(event, context, "SUCCESS",
                          {"Message": "Resource creation successful!"})
def lambda_handler(event, context):
  print(event)
  
  send_email(event,context)