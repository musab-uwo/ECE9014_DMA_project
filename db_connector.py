import mysql.connector
from dotenv import load_dotenv
load_dotenv(dotenv_path='/.env')
import os


# Function to create a connection to MySQL database
def create_connection():
    connection = mysql.connector.connect(
        host=os.getenv('HOST'),  
        user=os.getenv('USERNAME'),     
        password=os.getenv('PASSWORD'), 
        database=os.getenv('DBNAME'),
        port = os.getenv('PORT')
    )
    return connection
