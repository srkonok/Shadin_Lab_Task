#Login from with mySql info
import uuid #Token creation
import mysql.connector
import json


def lambda_handler(event, context):
    auth_token=""
 #DB connection
    try:
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            port="3306",
            user="1eQAzD8RMj",
            passwd="R9Uin6Sq5V",
            database="1eQAzD8RMj"
        )
#parse
        body = json.loads(event['body'])
        this_email = body['email']
        this_password = body['password']
        this_email = (email,)
        findUser = "SELECT * FROM user WHERE email = %s"
        mycursor = mydb.cursor()
        mycursor.execute(findUser, this_email)
        user = mycursor.fetchone()
        if user:
            if this_password == user[2]:
                auth_token = str(uuid.uuid1())
                mycursor.execute('INSERT INTO Token (email, token) values(%s, %s)', (user[1], auth_token,))
                mydb.commit()
                message = "Successfully Sign in and Token Generated!!"
            else:
                message = "Invalid Password!!"
        else:
            message = "User's not registered!!"
    except:
        message = "Sign in unsuccessful!"
        data = {
            "Message": message,
            "Token": auth_token
        }
    
    return{
        'statusCode': 200,
        'body': json.dumps(data)
    }
