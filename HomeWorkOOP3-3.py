from datetime import datetime
import os
today_date = f"{datetime.date(year, month, day)}"
# past_date = f"{datetime.date(year, month, day-2)}"
# base_url = f'https://api.stackexchange.com/docs/questions#fromdate={today_date}&todate=2022-10-12&order=desc&sort=creation&tagged=Python&filter=default&site=stackoverflow'

print(today_date, past_date)


