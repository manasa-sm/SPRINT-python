from dotenv import load_dotenv
import os
import requests	
import schedule
import time
import random
from plyer import notification

load_dotenv()
API_KEY = str(os.getenv("TOKEN"))
def News():
    query_params = {
	"sortBy": "top",
    "country": "in",
	"apiKey": API_KEY
	}
    main_url = " https://newsapi.org/v2/top-headlines?"
    res = requests.get(main_url, params=query_params)
    data = res.json()
    article = data["articles"]
    results = []

    for ar in article:
	    results.append(ar["title"])

    choice=random.randint(0, len(results))
    notification.notify(message=results[choice], timeout=10)
	
schedule.every().second.do(News)

while True:
    schedule.run_pending()
    time.sleep(1)
