import time 
import datetime


#time function being called by time module, returning time in epoch
seconds = time.time()

# ctime function called to convert epoch to local time
local_time = time.ctime(seconds)
print(
    "epoch: ", seconds
)
#creates delay of 5 seconds before printing local time
time.sleep(5)
print(
    "Local Time now: ", local_time
)

#shows the current date and time using now attribute
current = datetime.datetime.now()
print(str(current))
#shows time and date for a year from now using the timedelta attribute
one_year = current + datetime.timedelta(days = 365)
print(str(one_year))


