from pydantic import ValidationError,BaseModel
from typing import List, Optional 


class User(BaseModel):
    name: Optional[str]
    email: str
    password: str
    
