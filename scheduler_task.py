import schedule
import time

def print_hello():
    print("Hello, World!")

schedule.every(2).seconds.do(print_hello)

while True:
    schedule.run_pending()
    time.sleep(1)