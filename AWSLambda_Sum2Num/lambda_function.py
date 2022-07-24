import json

def lambda_handler(event, context):
    try:
        http_method=event['httpMethod']
        if http_method=='GET':
        
            first_num=float(event['queryStringParameters']['first_num'])
            second_num=float(event['queryStringParameters']['second_num'])
            
        elif http_method=='POST':
            body=json.loads(event['body'])
       
            first_num=float(body['first_num'])
            second_num=float(body['second_num'])
        sum=first_num+second_num
    except ValueError as ex:
        sum=f"Not valid number.Error is: {ex}  Class : {type(ex)}"
            

    return {
        'statusCode': 200,
        'body': json.dumps({'sum': sum})
    }
