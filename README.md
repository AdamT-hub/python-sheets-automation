# Python Google Sheets Survey Automation Project

## A Python automation script that collects user responses and automatically logs them into a Google Sheet for easy data tracking and analysis.

## Tech Stack:
- Python 3
- gspread (Google Sheets API)
- oauth2client (Google API Authentication)

## Features:
- Collects multiple types of user input:
  - Favorite color
  - Random number (processed automatically)
  - Personal information (name, phone number, age, email)
- Stores user information in a `my_person` class
- Automatically appends responses to a Google Sheet
- Presents basic API integration, automation, and OOP concepts

## How to Run:
1. Install the required Python dependencies: `pip install -r requirements.txt`
2. Create your own Google Service Account:
   - Go to Google Cloud Console -> Service Accounts
   - Create a new service account
   - Generate a JSON key and download it (e.g., creds.json)
3. Prepare your Google Sheet:
   - Create a sheet named exactly "Automation_Spreadsheet"
   - Share the sheet with your service account email (found in creds.json)
4. Place creds.json in the same folder as the script
5. Run the script: `python python_sheets_automation.py`
6. Follow the on-screen prompts (data automatically appended to Google Sheets)
