# ECE9014_DMA_project
Repo for  ECE 9014 001: DATA MANAGEMENT &amp; APPLICATIONS Project

Steps to follow to insert data into the Database

0. Create a .env file and fill in the credentials
1. Create a database called financial_data manually in the MySql database
2. In the database, run the income_earnings_info_queries.sql script, statement by statement
3. check if the correct tables are created with the commands at the end of the script
4. then from the Querys.sql script run the commands one by one
5. check if the correct tables are created with the commands at the end of the script
6. once the tables are created, run the read_yahoo_data.py script, this will fetch data from yfinance and push it into the database.
