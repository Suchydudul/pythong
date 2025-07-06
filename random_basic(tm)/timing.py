import time
from datetime import datetime

current_date = time.asctime()
print(current_date[11:19])
current_time =  datetime.strptime(current_date,"%a %b %d %H:%M:%S %Y")
print(current_time)