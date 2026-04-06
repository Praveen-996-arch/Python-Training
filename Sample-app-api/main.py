import os
API_KEY = os.environ.get("PYTHON_API_KEY")
APP_ID = os.environ.get("PYTHON_API_ID")

import requests
from datetime import datetime

# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY, 
# }
# parameters={
#     "query":"ran 3 miles and swam"
# }
# response = requests.post(url="https://app.100daysofpython.dev/v1/nutrition/natural/exercise", headers=headers, json=parameters)
# response.raise_for_status()
# print(response.text)
current_date = datetime.now().date().strftime("%d-%m-%Y")
sheet_parameters = {
        "Date": current_date,
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Exercise": "ran 3 miles and swam",
        "Duration": 30,
        "Calories": 300
}
sheet_response = requests.post(url="https://api.sheetbest.com/sheets/4ebeff04-67b6-42e6-bde7-c5df9b7c462b",json=sheet_parameters)
sheet_response.raise_for_status()
print(sheet_response.text)