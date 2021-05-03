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
    
    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you entered {len(values)}."
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")

get_sales_data()