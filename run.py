import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    GET SALES FIGURES FROM DATA
    """
    print("Please enter sales data from the last market")
    print("Data should be 6 figures, separated by commas.")
    print("Example: 23,32,23,87,98,64\n")

    data_str = input("Enter your data here:")
    print(f"the data provided is {data_str}.")

get_sales_data()