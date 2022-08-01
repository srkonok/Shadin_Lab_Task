# Auth_function
import json
import mycon as mc

def lambda_handler(event, context):
# DB connection
    dbmy=mc.confunc()
    
    this_token = event['authorizationToken']
    mycursor = dbmy.cursor()
    mycursor.execute("select * from Token where token = %s", (this_token,))
    Token = mycursor.fetchone()

    if Token:
        auth = 'Allow'
    else:
        auth = 'Deny'
    auth_Response = {
        "principalId": this_token,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement":
            [
                {
                    "Action": "execute-api:Invoke",
                    "Resource": ["arn:aws:execute-api:us-west-2:618758721119:15qjku1k9c/*/*"],
                    "Effect": auth
                }
            ]
        }
    }
    return auth_Response
