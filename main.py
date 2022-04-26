import requests
import os
from twilio.rest import Client

STOCK_NAME = "HDFC.BSE"
COMPANY_NAME = "HDFC"

account_sid = "ACb94aeac263260b9956e1d42435d52bdf"
auth_token = "51931fb8245d82c73552398ab224e924"
api_key = "ICSNQDW1IG2KERW2"
news_Api = "c9f9c3fb0e75455b8f5b5c823037aaad"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : api_key,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing = yesterday_data["4. close"]
print(yesterday_closing)

day_before_yesterday = data_list[1]
day_before_yesterday_closing = day_before_yesterday["4. close"]
print(day_before_yesterday_closing)

difference = abs(float(yesterday_closing) - float(day_before_yesterday_closing))
print(difference)

diff_percent = (difference/float(yesterday_closing)) * 100
print(diff_percent)

if diff_percent > 0.3:
    news_params = {
        "apiKey" : news_Api,
        "qInTitle" : COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    three_Articles = articles[:3]
    print(three_Articles)

    formatted_articles = [f"Headline : {article['title']}. \nBrief: {article['description']}" for article in three_Articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_= "+1 845 671 3542",
            to="+919354034429",

        )



