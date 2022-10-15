import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_HOST=os.getenv('DATABASE_HOST')
DATABASE_USERNAME=os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD=os.getenv('DATABASE_PASSWORD')
DATABASE_PORT=os.getenv('DATABASE_PORT')
DATABASE_NAME=os.getenv('DATABASE_NAME')