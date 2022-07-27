#Registration in mySql
import mysql.connector
import json


def lambda_handler(event, context):
    try:
        # DB connection
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            port="3306",
            user="1eQAzD8RMj",
            passwd="R9Uin6Sq5V",
            database="1eQAzD8RMj"
        )
# Perse
        body = json.loads(event['body'])
        this_name = body['name']
        this_email = body['email']
        this_password = body['password']
# Query
        sql = "SELECT * FROM user WHERE email = %s"
        mycursor = mydb.cursor()
        mycursor.execute(sql, (this_email,))
        user = mycursor.fetchone()

        if user:
            message = "Already registered in the database."
        else:
            mycursor.execute('insert into user (name, email, password) values(%s, %s, %s)', (
                this_name, this_email, this_password,))
            mydb.commit()
            message = "Congratulation! Successfully Sign Up!! 😃 "
            message = "User's signup failed!!"
    except:
        message = "User's signup failed!!"

    data = {
        "message": message,
        "status": "status"
    }
    return{
        'statusCode': 200,
        'body': json.dumps(data)
    }
