import json
import mycon as mc
import uuid

def lambda_handler(event, context):
    token=""
    try:
        dbmy=mc.confunc()
	mycursor = dbmy.cursor()	
        body = json.loads(event['body'])

        this_email = body['email']
        this_password = body['password']
        mycursor.execute("select * from user where email = %s",(this_email,))
        user = mycursor.fetchone()
        
        if user:
            email = user[1]
            password = user[2]
            if this_password == password:
                token = str(uuid.uuid1())
                mycursor.execute('insert into Token (email, token) values(%s, %s)', (email,token,))
                dbmy.commit()
                message = "Successfully Sign in and Token Generated!!"
            else:
                message = "Invalid Password!!"
        else:
            message = "User's not registered!!"
        
    except Exception as e:
        message = e
    
    data = {
            "message" : message,
            "token" : token
        }
 
    return{
        'statusCode': 200,
        'body': json.dumps(data)
    }
