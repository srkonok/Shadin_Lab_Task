import json
import mycon as mc
import hashlib,hmac
import jwt
from ParserUser import User
from pydantic import ValidationError


def lambda_handler(event, context):
    try:
        dbmy=mc.confunc()
        body = json.loads(event['body'])
        try :
            data=User(**body)
            this_name = data.name
            this_email = data.email
            this_password = data.password
            hash_password=hashlib.md5(this_password.encode('utf-8')).hexdigest()
        
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
        except ValidationError as e:
            message =e.json()
            print(message)
      
       
    except Exception as e:
        message = "Problem occured"
        

    data = {
           "msessage":message 
        }

    return{
        'statusCode': 200,
        'body': json.dumps(data)
    }
