import datetime
import time

for i in range(5):
    cur_time = datetime.datetime.now().strftime('%H:%M:%S')
    print(f"Текущее время: {cur_time}")
    time.sleep(1)
