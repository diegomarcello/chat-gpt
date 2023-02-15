import schedule
import time

from soccer_news_team_uol import generate_news


# schedule.every(15).seconds.do(generate_news())

while True:
    generate_news()
    time.sleep(15)
