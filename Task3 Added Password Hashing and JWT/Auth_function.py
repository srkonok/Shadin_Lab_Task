# Auth_function
import json
import mycon as mc
import jwt
import datetime,time

def lambda_handler(event, context):
# DB connection
    dbmy=mc.confunc()
    
    this_token = event['authorizationToken']
    mycursor = dbmy.cursor()
    mycursor.execute("select * from Token where token = %s", (this_token,))
    data = mycursor.fetchone()
    
    
    auth = 'Deny'
    if data:
        try:
            encoded_token=data[1]
            decoded_token=jwt.decode(encoded_token, "secret", leeway=datetime.timedelta(seconds=500), algorithms=["HS256"])
            auth = decoded_token['Auth']
        except jwt.ExpiredSignatureError:
            mycursor.execute("delete from Token where token = %s", (this_token,))
            dbmy.commit()
            
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
