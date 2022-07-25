def lambda_handler(event, context):
    
    print(event)
    
    if event['authorizationToken'] == 'abc123':
        auth = 'Allow'
    else:
        auth = 'Deny'
    
    auth_Response = {
        "principalId": "abc123", 
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