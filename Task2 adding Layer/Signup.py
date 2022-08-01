import json
import mycon as mc
 
def lambda_handler(event, context):
    try:
        dbmy=mc.confunc()
	  mycursor=dbmy.cursor()
        body = json.loads(event['body'])
        this_name = body['name']
        this_email = body['email']
        this_password = body['password']
        
        mycursor.execute("select * from user where email = %s", (this_email,))
        user= mycursor.fetchone()
        
        if (user):
            message = "already registered!"
        else:
            mycursor.execute('insert into user (name, email, password) values(%s, %s, %s)', (this_name,this_email,this_password,))
            dbmy.commit()
            message = "Congratulation!! Registration Successfull"

    except Exception as e:
        message = e

    data = {
           "msessage":message 
        }

    return{
        'statusCode': 200,
        'body': json.dumps(data)
    }
