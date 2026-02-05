# API → Excel Report Generator

This project is a Python automation script that fetches data from a public REST API, cleans and processes the data using pandas, and generates a structured Excel report.

## What the script does
- Sends an HTTP request to a REST API
- Validates the API response
- Cleans and renames columns for readability
- Categorizes records based on content length
- Sorts the data and exports it to an Excel file
- Logs execution steps and errors to a log file

## Technologies used
- Python
- requests
- pandas
- logging

## Output
- Excel report: `API_Analytics_Report.xlsx`
- Log file: `api_analiz.log`

## How to run
1. Install dependencies:
```bash
pip install -r requirements.txt
