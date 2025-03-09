# import mysql.connector
# from dotenv import load_dotenv
# load_dotenv(dotenv_path='/.env')
# import os


# # Function to create a connection to MySQL database
# def create_connection():
#     connection = mysql.connector.connect(
#         host=os.getenv('HOST'),  
#         user=os.getenv('USERNAME'),     
#         password=os.getenv('PASSWORD'), 
#         database=os.getenv('DBNAME'),
#         #port = os.getenv('PORT')
#         port=int(os.getenv("PORT", 3306))
#     )
#     return connection


#####EDITED######


import mysql.connector

# Function to create a connection to MySQL database
def create_connection():
    connection = mysql.connector.connect(
        host="127.0.0.1",  # Replace with your MySQL server address
        user="root",  # Replace with your MySQL username
        password="",  # Replace with your MySQL password
        database="financial_data",  # Replace with your MySQL database name
        port=3306,  # Default MySQL port, change if needed
        use_pure=True
    )
    return connection

