# ECE9014 Data Management & Applications Project

## 📊 Financial Data Management System

A comprehensive financial data management system that fetches, stores, and manages financial data from Yahoo Finance API. This project is designed for ECE 9014 001: Data Management & Applications course.

## 🚀 Features

### Core Functionality
- **Stock Data Retrieval**: Fetches real-time and historical stock data using Yahoo Finance API
- **Financial Statement Management**: Stores and manages income statements, balance sheets, and cash flow statements
- **Company Information**: Comprehensive company profile storage including sector, industry, and website
- **Dividend Tracking**: Historical dividend data collection and storage
- **Stock Price History**: Daily stock price data with OHLCV (Open, High, Low, Close, Volume) metrics

### Data Storage Capabilities
- **Income Statements**: Revenue, expenses, profits, EPS, and various financial metrics
- **Balance Sheets**: Assets, liabilities, equity, debt, and financial position data
- **Cash Flow Statements**: Operating, investing, and financing cash flows
- **Stock Prices**: Historical price movements and trading volumes
- **Dividends**: Dividend payment history and amounts

### Data Visualization
- **Tableau Integration**: Interactive dashboards and visualizations for financial data analysis
- **Business Intelligence**: Visual insights into financial trends and performance metrics

## 🛠️ Tech Stack

### Backend
- **Python 3.x**: Core programming language
- **MySQL**: Primary database for financial data storage
- **yfinance**: Yahoo Finance API wrapper for financial data retrieval

### Python Libraries
- **mysql-connector-python**: MySQL database connectivity
- **pandas**: Data manipulation and analysis
- **python-dotenv**: Environment variable management
- **yfinance**: Yahoo Finance data fetching

### Database
- **MySQL**: Relational database management system
- **Structured Schema**: Normalized database design with proper relationships

### Data Visualization
- **Tableau**: Business intelligence and data visualization platform
- **Interactive Dashboards**: Real-time financial data analysis and reporting

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.7 or higher
- MySQL Server installed and running
- MySQL Workbench (optional, for database management)
- Tableau Desktop or Tableau Public (for data visualization)

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ECE9014_DMA_project
```

### 2. Install Required Python Packages
```bash
pip install yfinance mysql-connector-python pandas python-dotenv
```

### 3. Database Setup

#### Create MySQL Database
```sql
CREATE DATABASE financial_data;
```

#### Environment Configuration
Create a `.env` file in the project root with your MySQL credentials:
```env
HOST=localhost
USERNAME=your_mysql_username
PASSWORD=your_mysql_password
DBNAME=financial_data
PORT=3306
```

### 4. Database Schema Setup

#### Step 1: Run Income Statement Schema
Execute the commands in `income_earnings_info_queries.sql` one by one in your MySQL client:
- Creates `company_info` table
- Creates `income_statement` table
- Creates `dividends_data` table
- Includes necessary alterations and constraints

#### Step 2: Run Additional Tables Schema
Execute the commands in `Querys.sql` one by one:
- Creates `Stocks` table
- Creates `StockPrices` table
- Creates `BalanceSheet` table
- Creates `CashFlow` table
- Sets up foreign key relationships

#### Step 3: Verify Table Creation
Run the verification queries at the end of each SQL script to ensure tables are created correctly.

### 5. Data Population
```bash
python read_yahoo_data.py
```

This will fetch Apple (AAPL) financial data and populate all tables in the database.

### 6. Tableau Visualization Setup
1. Open Tableau Desktop or Tableau Public
2. Connect to your MySQL database using the same credentials from your `.env` file
3. Import the financial data tables for analysis and visualization
4. Create interactive dashboards to analyze financial trends and performance metrics

## 📊 Database Schema

### Tables Overview

| Table | Purpose | Key Fields |
|-------|---------|------------|
| `company_info` | Company profiles | ticker, long_name, sector, industry |
| `income_statement` | Profit & Loss data | revenue, expenses, net_income, EPS |
| `BalanceSheet` | Financial position | assets, liabilities, equity |
| `CashFlow` | Cash movement | operating_cash_flow, free_cash_flow |
| `StockPrices` | Price history | open, close, high, low, volume |
| `dividends_data` | Dividend payments | dividend_date, dividend_amount |

### Entity Relationships
- `company_info` is the central table with primary key `company_id`
- All other tables reference `company_info` via foreign keys
- Supports multiple companies and their complete financial data

## 💡 Usage Examples

### Fetching Different Company Data
Modify the `symbol` variable in `read_yahoo_data.py`:
```python
symbol = "MSFT"  # For Microsoft
symbol = "GOOGL" # For Google
symbol = "TSLA"  # For Tesla
```

### Custom Date Ranges
Adjust the date range for historical data:
```python
stock_data = ticker.history(start="2020-01-01", end="2024-01-01")
```

## 📁 Project Structure

```
ECE9014_DMA_project/
├── db_connector.py              # Database connection utilities
├── read_yahoo_data.py           # Main data fetching and insertion script
├── income_earnings_info_queries.sql  # Income statement and company tables
├── Querys.sql                  # Additional financial tables
├── README.md                   # Project documentation
└── .env                        # Environment variables (not included)
```

## 🔍 Key Functions

### Database Operations
- `create_connection()`: Establishes MySQL database connection
- `add_company_info()`: Inserts/updates company profile data
- `add_income_statement()`: Processes and stores income statement data

### Financial Data Processing
- `insert_stock_price()`: Historical stock price data insertion
- `insert_balance_sheet()`: Balance sheet data processing
- `insert_cash_flow()`: Cash flow statement data handling
- `insert_dividends_data()`: Dividend history management

## 🚦 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Verify MySQL server is running
   - Check `.env` file credentials
   - Ensure `financial_data` database exists

2. **Table Creation Errors**
   - Run SQL scripts in the correct order
   - Check for existing tables with same names
   - Verify foreign key relationships

3. **Data Insertion Failures**
   - Ensure all required tables exist
   - Check data type compatibility
   - Verify internet connection for Yahoo Finance API

### Data Validation
- Check table contents using the SELECT statements in SQL files
- Verify data integrity with foreign key constraints
- Monitor for NULL values in critical fields

## 📈 Future Enhancements

- Support for multiple stock symbols in batch processing
- Enhanced Tableau dashboard templates and automated report generation
- RESTful API for data access
- Automated data refresh scheduling with Tableau Server integration
- Portfolio management capabilities
- Advanced financial metrics calculation and predictive analytics
- Real-time data streaming to Tableau dashboards

## 🤝 Contributing

This project is part of ECE 9014 coursework. For contributions:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is created for educational purposes as part of ECE 9014: Data Management & Applications course.

## 📞 Support

For questions or issues related to this project, please contact the course instructor or teaching assistants.

---

**Note**: This project uses live financial data from Yahoo Finance. Market data availability and API limitations may affect data retrieval.