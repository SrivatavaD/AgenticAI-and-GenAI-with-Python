# from pydantic import Optional
# from pydantic import BaseModel, Field

# class Employee(BaseModel):
#     id: int
#     name: str = Field(
#         ...,
#         min_length=3,
#         max_length=50,
#         description="The employee's full name"
#         example="John Doe"
#     )
#     department: Optional[str] = 'general'
#     salary: float = Field(
#         ...,
#         ge = 10000,
#     )      
# 
# from pydantic import BaseModel, field_validator
# class User(BaseModel):
#     username: str
#     @field_validator('username')
#     def username_length(cls, v):
#         if len(v) < 4:
#             raise ValueError("Username must be atleast 4 characters")
#         return v
    
# class SignupData(BaseModel):
#     password: str
#     confirm_password: str
#     @model_validator(mode="after")
#     def passwords_match(cls, values):
#         if values.password != values.confirm_password:
#             raise ValueError("Passwords do not match")
#         return values

from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime
class Person(BaseModel):
    first_name: str
    last_name: str
    @field_validator('first_name', 'last_name')
    def names_must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError('Names must be capitalized')
        return v
    
    class User(BaseModel):
        email:str

        @field_validator('email')
        def normalize_email(cls, v):
            return v.lower().strip()
        
class Product(BaseModel):
    price: str #$4.44

    @field_validator('price', mode ='before')
    def parse_price(clas, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v

class DateRange(BaseModel):
    start_date: datetime
    end_data: datetime

    @model_validator(mode="after")
    def validate_date_range(cls, values):
        if values.start_date>=values.end_data:
            raise ValueError("start_date must be before end_date")
        return values