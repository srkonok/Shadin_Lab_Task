from pydantic import ValidationError, BaseModel, validator
from typing import List, Optional
import re


class User(BaseModel):
    name: Optional[str]
    email: str
    password: str

    @validator("email")
    def email_validator(cls, v):
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat, v):
            return v
        raise ValueError("Not Valid Email!")

    @validator("password")
    def pass_must_be_8_digit(cls, v):
        if(len(v) != 8):
            raise ValueError("Password must be 8 digit!")
        return v


#userDetails = {
#   "name": "Konok",
#   "email": "srkonok20@gmail.com",
#    "password": "12345678"
#}
# try:
#     user = User(**userDetails)
#     this_name = user.name
#     this_email = user.email
#     this_password = user.password
#     print(user)
# except ValidationError as e:
#     print(e)    

