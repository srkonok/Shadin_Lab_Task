import json
import mycon as mc
import hashlib,hmac
import jwt

def lambda_handler(event, context):
    try:
        dbmy=mc.confunc()
        body = json.loads(event['body'])
        this_name = body['name']
        this_email = body['email']
        this_password = body['password']
        
        hash_password=hashlib.md5(this_password.encode('utf-8')).hexdigest()
        
        print("hash_pass", hash_password)
        mycursor=dbmy.cursor()
        mycursor.execute("select * from user where email = %s", (this_email,))
        user= mycursor.fetchone()
        
        if (user):
            message = "Email already taken!"
        else:
            try:
                mycursor.execute('insert into user (name, email, password) values(%s, %s, %s)', (this_name,this_email,hash_password,))
                dbmy.commit()
                message = "Congratulation!! Registration Successfull"
            except Exception as e:
                message="Not included in Database"
    except Exception as e:
        message = "Problem occured"
        

    data = {
           "msessage":message 
        }

    return{
        'statusCode': 200,
        'body': json.dumps(data)
    }