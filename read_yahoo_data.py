import yfinance as yf
from db_connector import create_connection
import pandas as pd 
connection = create_connection()
cursor = connection.cursor()

# def insert_stock_data(symbol, company_name):
#     cursor.execute("INSERT INTO Stocks (symbol, company_name) VALUES (%s, %s)", (symbol, company_name))
#     stock_id = cursor.lastrowid
#     connection.commit()
#     return stock_id

def add_company_info(ticker, company_id):
    connection = create_connection()
    cursor = connection.cursor()
    apple = yf.Ticker(ticker)
    info = apple.info

    company_info_data = (
        ticker,
        info.get("longName"),
        info.get("sector"),
        info.get("industry"),
        info.get("country"),
        info.get("website")
    )

    cursor.execute("""
        INSERT INTO company_info (ticker, long_name, sector, industry, country, website)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            long_name = VALUES(long_name),
            sector = VALUES(sector),
            industry = VALUES(industry),
            country = VALUES(country),
            website = VALUES(website)
    """, company_info_data)

    cursor.execute("SELECT company_id FROM company_info WHERE ticker = %s", (ticker,))
    company_id = cursor.fetchone()[0]
    connection.commit()
    return company_id

def add_income_statement(ticker, company_id):
    apple = yf.Ticker(ticker)
    income_statement = apple.financials.T  # Transposed for row-wise iteration

    for date_index, row in income_statement.iterrows():
        end_date = pd.to_datetime(date_index, errors='coerce')

        if pd.isna(end_date):
            print(f"Skipping invalid date: {date_index}")
            continue
        else:
            end_date = end_date.date() 

        fields = ['company_id', 'end_date']
        values = [company_id, end_date]
        
        for column_name, value in row.items():
            if pd.notnull(value):
                #Change column names to be matched with db_col names
                field_name = column_name.replace(" ", "_").replace(".", "").replace("-", "_")
                fields.append(field_name)
                values.append(value)

        sql_query = f"""
            INSERT INTO income_statement ({', '.join(fields)})
            VALUES ({', '.join(['%s'] * len(values))})
        """
        cursor.execute(sql_query, values)
    connection.commit()


def insert_stock_price(stock_id, stock_data):
    for date, row in stock_data.iterrows():
        date = date.to_pydatetime()
        cursor.execute("""
        INSERT INTO StockPrices (stock_id, date, open_price, close_price, high_price, low_price, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            stock_id,
            date,
            float(row['Open']),
            float(row['Close']),
            float(row['High']),
            float(row['Low']),
            float(row['Volume'])
        ))
    connection.commit()

def insert_balance_sheet(stock_id, balance_sheet_data):
    for date, data in balance_sheet_data.items():
        ordinary_shares_number = data.get('Ordinary Shares Number', None)
        common_stock_equity = data.get('Common Stock Equity', None)
        stockholders_equity = data.get('Stockholders Equity', None)
        retained_earnings = data.get('Retained Earnings', None)
        
        net_debt = data.get('Net Debt', None)
        total_debt = data.get('Total Debt', None)
        total_liabilities_net_minority_interest = data.get('Total Liabilities Net Minority Interest', None)
        current_liabilities = data.get('Current Liabilities', None)
        long_term_debt_and_capital_lease_obligation = data.get('Long Term Debt And Capital Lease Obligation', None)
        
        total_assets = data.get('Total Assets', None)
        total_non_current_assets = data.get('Total Non Current Assets', None)
        net_ppe = data.get('Net PPE', None)
        accumulated_depreciation = data.get('Accumulated Depreciation', None)
        current_assets = data.get('Current Assets', None)
        inventory = data.get('Inventory', None)
        accounts_receivable = data.get('Accounts Receivable', None)
        cash_cash_equivalents_and_short_term_investments = data.get('Cash Cash Equivalents And Short Term Investments', None)
        
        invested_capital = data.get('Invested Capital', None)
        working_capital = data.get('Working Capital', None)
        total_capitalization = data.get('Total Capitalization', None)
        income_tax_payable = data.get('Income Tax Payable', None)
        other_current_liabilities = data.get('Other Current Liabilities', None)

        ordinary_shares_number = None if pd.isna(ordinary_shares_number) else ordinary_shares_number
        common_stock_equity = None if pd.isna(common_stock_equity) else common_stock_equity
        stockholders_equity = None if pd.isna(stockholders_equity) else stockholders_equity
        retained_earnings = None if pd.isna(retained_earnings) else retained_earnings
        
        net_debt = None if pd.isna(net_debt) else net_debt
        total_debt = None if pd.isna(total_debt) else total_debt
        total_liabilities_net_minority_interest = None if pd.isna(total_liabilities_net_minority_interest) else total_liabilities_net_minority_interest
        current_liabilities = None if pd.isna(current_liabilities) else current_liabilities
        long_term_debt_and_capital_lease_obligation = None if pd.isna(long_term_debt_and_capital_lease_obligation) else long_term_debt_and_capital_lease_obligation
        
        total_assets = None if pd.isna(total_assets) else total_assets
        total_non_current_assets = None if pd.isna(total_non_current_assets) else total_non_current_assets
        net_ppe = None if pd.isna(net_ppe) else net_ppe
        accumulated_depreciation = None if pd.isna(accumulated_depreciation) else accumulated_depreciation
        current_assets = None if pd.isna(current_assets) else current_assets
        inventory = None if pd.isna(inventory) else inventory
        accounts_receivable = None if pd.isna(accounts_receivable) else accounts_receivable
        cash_cash_equivalents_and_short_term_investments = None if pd.isna(cash_cash_equivalents_and_short_term_investments) else cash_cash_equivalents_and_short_term_investments

        invested_capital = None if pd.isna(invested_capital) else invested_capital
        working_capital = None if pd.isna(working_capital) else working_capital
        total_capitalization = None if pd.isna(total_capitalization) else total_capitalization
        income_tax_payable = None if pd.isna(income_tax_payable) else income_tax_payable
        other_current_liabilities = None if pd.isna(other_current_liabilities) else other_current_liabilities

        cursor.execute("""
        INSERT INTO BalanceSheet (
            stock_id, date, ordinary_shares_number, common_stock_equity, stockholders_equity, 
            retained_earnings, net_debt, total_debt, total_liabilities_net_minority_interest, 
            current_liabilities, long_term_debt_and_capital_lease_obligation, total_assets,
            total_non_current_assets, net_ppe, accumulated_depreciation, current_assets, 
            inventory, accounts_receivable, cash_cash_equivalents_and_short_term_investments, 
            invested_capital, working_capital, total_capitalization, income_tax_payable,
            other_current_liabilities
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            stock_id, date, ordinary_shares_number, common_stock_equity, stockholders_equity,
            retained_earnings, net_debt, total_debt, total_liabilities_net_minority_interest,
            current_liabilities, long_term_debt_and_capital_lease_obligation, total_assets,
            total_non_current_assets, net_ppe, accumulated_depreciation, current_assets,
            inventory, accounts_receivable, cash_cash_equivalents_and_short_term_investments,
            invested_capital, working_capital, total_capitalization, income_tax_payable,
            other_current_liabilities
        ))
    connection.commit()

def insert_cash_flow(stock_id, cash_flow_data):
    for date, data in cash_flow_data.items():
        operating_cash_flow = data.get('Operating Cash Flow', None)
        free_cash_flow = data.get('Free Cash Flow', None)
        depreciation_amortization = data.get('Depreciation Amortization Depletion', None)
        net_income_continuing_operations = data.get('Net Income From Continuing Operations', None)
        
        investing_cash_flow = data.get('Investing Cash Flow', None)
        capital_expenditure = data.get('Capital Expenditure', None)
        
        financing_cash_flow = data.get('Financing Cash Flow', None)
        repurchase_of_capital_stock = data.get('Repurchase Of Capital Stock', None)
        issuance_of_debt = data.get('Issuance Of Debt', None)
        repayment_of_debt = data.get('Repayment Of Debt', None)
        common_stock_issuance = data.get('Common Stock Issuance', None)
        
        interest_paid = data.get('Interest Paid Supplemental Data', None)
        income_tax_paid = data.get('Income Tax Paid Supplemental Data', None)

        operating_cash_flow = None if pd.isna(operating_cash_flow) else operating_cash_flow
        free_cash_flow = None if pd.isna(free_cash_flow) else free_cash_flow
        depreciation_amortization = None if pd.isna(depreciation_amortization) else depreciation_amortization
        net_income_continuing_operations = None if pd.isna(net_income_continuing_operations) else net_income_continuing_operations
        
        investing_cash_flow = None if pd.isna(investing_cash_flow) else investing_cash_flow
        capital_expenditure = None if pd.isna(capital_expenditure) else capital_expenditure
        
        financing_cash_flow = None if pd.isna(financing_cash_flow) else financing_cash_flow
        repurchase_of_capital_stock = None if pd.isna(repurchase_of_capital_stock) else repurchase_of_capital_stock
        issuance_of_debt = None if pd.isna(issuance_of_debt) else issuance_of_debt
        repayment_of_debt = None if pd.isna(repayment_of_debt) else repayment_of_debt
        common_stock_issuance = None if pd.isna(common_stock_issuance) else common_stock_issuance

        interest_paid = None if pd.isna(interest_paid) else interest_paid
        income_tax_paid = None if pd.isna(income_tax_paid) else income_tax_paid

        cursor.execute("""
        INSERT INTO CashFlow (
            stock_id, date, operating_cash_flow, free_cash_flow, depreciation_amortization,
            net_income_continuing_operations, investing_cash_flow, capital_expenditure,
            financing_cash_flow, repurchase_of_capital_stock, issuance_of_debt, repayment_of_debt,
            common_stock_issuance, interest_paid, income_tax_paid
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            stock_id, date, operating_cash_flow, free_cash_flow, depreciation_amortization,
            net_income_continuing_operations, investing_cash_flow, capital_expenditure,
            financing_cash_flow, repurchase_of_capital_stock, issuance_of_debt, repayment_of_debt,
            common_stock_issuance, interest_paid, income_tax_paid
        ))
    connection.commit()

def insert_dividends_data(ticker, company_id):
    stock = yf.Ticker(ticker)

    # Get dividends data
    dividends = stock.dividends

    if dividends.empty:
        print(f"No dividends data available for {ticker}")
        return

    for date, amount in dividends.items():
        # Ensure the date is in the correct format
        dividend_date = pd.to_datetime(date).date()

        # Prepare the data for insertion into the database
        dividend_data = (
            company_id,
            dividend_date,
            amount
        )

        # Insert data into the database
        cursor.execute("""
            INSERT INTO dividends_data (company_id, dividend_date, dividend_amount)
            VALUES (%s, %s, %s)
        """, dividend_data)

    # Commit the transaction to the database
    connection.commit()
    print(f"Dividends data for {ticker} inserted successfully.")

def main():
    symbol = "AAPL" # Company Name 
    ticker = yf.Ticker(symbol)
    company_id = add_company_info(symbol, None)
    stock_data = ticker.history(start="2020-01-01", end="2023-01-01")
    stock_id = add_company_info(symbol, None)\
    
    # Add Income Statement
    add_income_statement(symbol, company_id)

    # Balance Sheet Data
    balance_sheet_data = ticker.balance_sheet.T
    balance_sheet_data = balance_sheet_data.to_dict(orient="index")

    #Cash Flow 
    cash_flow_data = ticker.cash_flow.T
    cash_flow_data = cash_flow_data.to_dict(orient="index")

    insert_dividends_data(symbol,company_id)
    insert_stock_price(stock_id, stock_data)
    print("Stock Price inserted")
    insert_balance_sheet(stock_id, balance_sheet_data)
    print("Balance Sheet inserted")
    insert_cash_flow(stock_id, cash_flow_data)
    print("Cash Flow Inserted")
    print(f"Data for {symbol} inserted successfully into the databases.")


if __name__ == "__main__":
    main()

cursor.close()
connection.close()
