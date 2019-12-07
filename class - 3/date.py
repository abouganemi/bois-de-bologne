import datetime
from datetime import date

today = date.today().strftime("%d-%m-%Y")

print(today)


x = datetime.datetime(2018, 6, 1)
print(x.strftime("%d-%m-%Y"))
