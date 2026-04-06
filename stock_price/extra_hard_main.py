STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "W5P1PW4YHX9YB1RP"
NEWS_ORG_API_KEY = "0746e54a61dd46e1a0e45327516b997e"
import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import os

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

parameters = {
    "symbol":STOCK,
    "function":"TIME_SERIES_DAILY",
    "apikey":STOCK_API_KEY,
    "datatype":"json"
}
# current_date = datetime.now().date() - timedelta(days=1)
current_date = datetime.now().date()
# print(current_date)
response = requests.get(url = STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
closing_price = [stock_data[key]["4. close"] for key,value in stock_data.items()]
yesterday_closing_price = float(closing_price[0])
# print(yesterday_closing_price)
day_before_yes_closing_price =  float(closing_price[1])
# print(day_before_yes_closing_price)
difference = (yesterday_closing_price - day_before_yes_closing_price)*10/yesterday_closing_price
print(difference)
up_down_arrow = None
if difference > 0:
    up_down_arrow = "🔺"
elif difference < 0:
    up_down_arrow = "🔻"


if abs(difference) > 0:
    news_parameters = {
        "apiKey":NEWS_ORG_API_KEY,
        "q":COMPANY_NAME,
        "language": "en",
        "sortBy":"publishedAt",
        "page":1

    }
    news_response = requests.get(url = "https://newsapi.org/v2/everything",params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    three_articles = news_data[:3]
    formatted_data = [f"{STOCK}:{up_down_arrow}{difference}%\nHeadline:{article['title']}\nBrief:{article['description']}" for article in three_articles]



    account_sid = os.environ.get("ACC_SID")
    auth_token = os.environ.get("AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    for article in formatted_data:
        print(article)
        client.api.account.messages.create(
                to="whatsapp:+12055099890",
                from_="whatsapp:+14155238886",
                body=article)
