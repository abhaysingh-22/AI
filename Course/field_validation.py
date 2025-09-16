from pydantic import BaseModel, Field, ValidationError, model_validator, field_validator

class User(BaseModel):
    username: str
    
    @field_validator('username')  # this field validator ensures username is not empty
    def username_must_not_be_empty(cls, v):
        if len(v) < 4:
            raise ValueError('Username must be at least 4 characters long')
        return v
    
class SignupData(BaseModel):
    password: str
    confirm_password: str
    
    @model_validator(mode='after')  # this model validator ensures passwords match and mode after means after field validation is done
    def passwords_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values