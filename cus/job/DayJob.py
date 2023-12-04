import logging
import time

import schedule


def job():
    logging.info("[DayJob]:start Job")


class MyJob():
    schedule.every().day.at("* * * * * ").do(job)
    schedule.run_pending()
    time.sleep(1)
