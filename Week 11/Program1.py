class Time:
    def __init__(self,time):
        self.hr=time.hour
        self.min=time.minute
        self.sec=time.second
     
from datetime import datetime

start = Time(datetime.now())
import time
time.sleep(5)
end = Time(datetime.now())

print(start.hr, start.min, start.sec)
print(end.hr, end.min, end.sec)
