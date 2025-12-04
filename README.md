# Currency API Automation (USD → All Currencies)
## What it does
- Fetches live exchange-rate JSON data
- Cleans and transforms it into a DataFrame
- Uploads data to Google Sheets automatically
- Includes try/except, logging, regex cleaning, modular structure

## Tech
Python, Requests, Pandas, Regex, Google Sheets API, gspread

## How to run
1. Add credentials.json
2. pip install -r requirements.txt
3. python main.py
