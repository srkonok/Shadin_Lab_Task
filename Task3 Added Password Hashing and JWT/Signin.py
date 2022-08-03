import json
import mycon as mc
import datetime,time
import hashlib,hmac
import jwt

def lambda_handler(event, context):
    token=""
    try:
        dbmy=mc.confunc()

        body = json.loads(event['body'])

        this_email = body['email']
        this_password = body['password']
        
        hash_pass=hashlib.md5(this_password.encode('utf-8')).hexdigest()
        print(hash_pass)
        
        mycursor = dbmy.cursor()
        mycursor.execute("select * from user where email = %s",(this_email,))
        user = mycursor.fetchone()
        
        if user:
            email = user[1]
            password = user[2]
            print(password)
            if hash_pass == password:
                token=jwt.encode({'Auth':'Allow',"exp": datetime.datetime.utcnow()+ datetime.timedelta(seconds=2)}, "secret", algorithm="HS256")
                mycursor.execute('insert into Token (email, token) values(%s, %s)', (email,token,))
                dbmy.commit()
                message = "Successfully Sign in and Token Generated!!"
            else:
                message = "Invalid Password!!"
                 
        else:
            message = "User's not registered!!"
        
    except :
        message = "Can't signin!!"
    
    data = {
            "message" : message,
            "token" : token
        }
    
    

    return{
        'statusCode': 200,
        'body': json.dumps(data)
    }