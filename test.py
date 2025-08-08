from datetime import datetime
import pytz

UTC = pytz.utc
timezone = pytz.timezone('Europe/London')

dt_1 = datetime.now(timezone)
time = dt_1.strftime("%H:%M:%S")
time_range = ""
if (time >= "07:00:00" and time < "12:00:00"):
    time_range = "morning"
elif (time >= "12:00:00" and time <= "17:00:00"):
    time_range = "afternoon"
elif (time > "17:00:00" and time <= "18:00:00"):
    time_range = "evening"
else:
    time_range = "night"
    


name = input("What is your name?")
print("Hi",name,"The current time is", time, "and it is", time_range,".")