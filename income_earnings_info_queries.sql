-- CREATE DATABASE financial_data;

use financial_data;

CREATE TABLE IF NOT EXISTS company_info (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10) UNIQUE,
    long_name VARCHAR(255),
    sector VARCHAR(255),
    industry VARCHAR(255),
    country VARCHAR(255),
    website VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS income_statement (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT,
    end_date DATE,
    Tax_Effect_Of_Unusual_Items BIGINT,
    Tax_Rate_For_Calcs FLOAT,
    Normalized_EBITDA BIGINT,
    Net_Income_From_Continuing_Operation_Net_Minority_Interest BIGINT,
    Reconciled_Depreciation BIGINT,
    Reconciled_Cost_Of_Revenue BIGINT,
    EBITDA BIGINT,
    EBIT BIGINT,
    Net_Interest_Income BIGINT,
    Interest_Expense BIGINT,
    Interest_Income BIGINT,
    Normalized_Income BIGINT,
    Net_Income_From_Continuing_And_Discontinued_Operations BIGINT,
    Total_Expenses BIGINT,
    Total_Operating_Income_As_Reported BIGINT,
    Diluted_Average_Shares BIGINT,
    Basic_Average_Shares BIGINT,
    Diluted_EPS FLOAT,
    Basic_EPS FLOAT,
    Diluted_NI_Avail_to_Common_Stockholders BIGINT,
    Net_Income_Common_Stockholders BIGINT,
    Net_Income BIGINT,
    Net_Income_Including_Noncontrolling_Interests BIGINT,
    Net_Income_Continuous_Operations BIGINT,
    Tax_Provision BIGINT,
    Pretax_Income BIGINT,
    Other_Income_Expense BIGINT,
    Other_Non_Operating_Income_Expenses BIGINT,
    Net_Non_Operating_Interest_Income_Expense BIGINT,
    Interest_Expense_Non_Operating BIGINT,
    Interest_Income_Non_Operating BIGINT,
    Operating_Income BIGINT,
    Operating_Expense BIGINT,
    Research_And_Development BIGINT,
    Selling_General_And_Administration BIGINT,
    Gross_Profit BIGINT,
    Cost_Of_Revenue BIGINT,
    Total_Revenue BIGINT,
    Operating_Revenue BIGINT,
    FOREIGN KEY (company_id) REFERENCES company_info(company_id)
);

ALTER TABLE income_statement
RENAME COLUMN Net_Income_From_Continuing_And_Discontinued_Operations to Net_Income_From_Continuing_And_Discontinued_Operation;

ALTER TABLE income_statement
RENAME COLUMN Diluted_NI_Avail_to_Common_Stockholders to Diluted_NI_Availto_Com_Stockholders;

CREATE TABLE dividends_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT,            
    dividend_date DATE,                   
    dividend_amount DECIMAL(20, 4),      
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES company_info(company_id)
);


-- DROP TABLE earnings_data; 

SELECT * FROM company_info;
SELECT * FROM dividends_data;
SELECT * FROM income_statement;

-- TRUNCATE table earnings_data;
-- TRUNCATE table income_statement;

