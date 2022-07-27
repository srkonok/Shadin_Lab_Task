# Auth_function
import mysql.connector
import json


def lambda_handler(event, context):
    # DB connection
    mydb = mysql.connector.connect(
        host="remotemysql.com",
        port="3306",
        user="1eQAzD8RMj",
        passwd="R9Uin6Sq5V",
        database="1eQAzD8RMj"
    )
    this_token = event['authorizationToken']
    findToken = "SELECT * FROM Token WHERE token = %s"
    mycursor = mydb.cursor()
    mycursor.execute(findToken, (this_token,))
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
