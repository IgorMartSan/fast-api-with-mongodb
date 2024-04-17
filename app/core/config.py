
from dotenv import load_dotenv
import os
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    load_dotenv()
    JWT_SECRET_KEY:str=os.getenv('JWT_SECRET_KEY')
    JWT_REFRESH_SECRET_KEY:str=os.getenv('JWT_REFRESH_SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTE:int=os.getenv('ACCESS_TOKEN_EXPIRE_MINUTE')
    REFRESH_TOKEN_EXPIRE_MINUTE:int=os.getenv('REFRESH_TOKEN_EXPIRE_MINUTE')
    MONGO_CONNECTION_STRING:str=os.getenv('MONGO_CONNECTION_STRING')
    ALGORITHM:str=os.getenv('ALGORITHM')
    PROJECT_NAME:str=os.getenv('PROJECT_NAME')


settings = Settings()
