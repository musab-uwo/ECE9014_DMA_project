CREATE DATABASE financial_data;

USE financial_data;

CREATE TABLE Stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    company_name VARCHAR(100) NOT NULL
);

CREATE TABLE StockPrices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stock_id INT,
    date DATE,
    open_price DECIMAL(10, 2),
    close_price DECIMAL(10, 2),
    high_price DECIMAL(10, 2),
    low_price DECIMAL(10, 2),
    volume BIGINT,
    FOREIGN KEY (stock_id) REFERENCES company_info(company_id)
);

CREATE TABLE BalanceSheet (
    id INT PRIMARY KEY AUTO_INCREMENT,
    stock_id INT,
    date DATE,
    -- Equity and Share Information
    ordinary_shares_number BIGINT,
    common_stock_equity DECIMAL(15, 2),
    stockholders_equity DECIMAL(15, 2),
    retained_earnings DECIMAL(15, 2),

    -- Debt and Liabilities
    net_debt DECIMAL(15, 2),
    total_debt DECIMAL(15, 2),
    total_liabilities_net_minority_interest DECIMAL(15, 2),
    current_liabilities DECIMAL(15, 2),
    long_term_debt_and_capital_lease_obligation DECIMAL(15, 2),

    -- Assets
    total_assets DECIMAL(15, 2),
    total_non_current_assets DECIMAL(15, 2),
    net_ppe DECIMAL(15, 2),
    accumulated_depreciation DECIMAL(15, 2),
    current_assets DECIMAL(15, 2),
    inventory DECIMAL(15, 2),
    accounts_receivable DECIMAL(15, 2),
    cash_cash_equivalents_and_short_term_investments DECIMAL(15, 2),

    -- Additional Metrics
    invested_capital DECIMAL(15, 2),
    working_capital DECIMAL(15, 2),
    total_capitalization DECIMAL(15, 2),
    income_tax_payable DECIMAL(15, 2),
    other_current_liabilities DECIMAL(15, 2),
    FOREIGN KEY (stock_id) REFERENCES company_info(company_id)
);

ALTER TABLE BalanceSheet
ADD COLUMN stock_id INT,
ADD COLUMN date DATE,
ADD CONSTRAINT fk_stock_id FOREIGN KEY (stock_id) REFERENCES company_info(company_id);

CREATE TABLE CashFlow (
    id INT PRIMARY KEY AUTO_INCREMENT,
    stock_id INT,
    date DATE,
    
    -- Operating Cash Flow
    operating_cash_flow DECIMAL(15, 2),
    free_cash_flow DECIMAL(15, 2),
    depreciation_amortization DECIMAL(15, 2),
    net_income_continuing_operations DECIMAL(15, 2),
    
    -- Investing Cash Flow
    investing_cash_flow DECIMAL(15, 2),
    capital_expenditure DECIMAL(15, 2),
    
    -- Financing Cash Flow
    financing_cash_flow DECIMAL(15, 2),
    repurchase_of_capital_stock DECIMAL(15, 2),
    issuance_of_debt DECIMAL(15, 2),
    repayment_of_debt DECIMAL(15, 2),
    common_stock_issuance DECIMAL(15, 2),
    
    -- Supplemental Data
    interest_paid DECIMAL(15, 2),
    income_tax_paid DECIMAL(15, 2),

    -- Foreign key constraint (if stock_id references another table)
    FOREIGN KEY (stock_id) REFERENCES company_info(company_id);
);

SELECT * From CashFlow;
SELECT * FROM BalanceSheet order by date;