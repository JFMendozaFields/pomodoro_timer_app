import time, datetime

#Stopwatch

#Timer starter
starttime = time.time()
lasttime = starttime
lapnum = 1
value = ''


print("Press ENTER for each lap. \n Type Q and press ENTER to stop.")

while value.lower() != 'q':

    # Input for the ENTER key press
    value = input()

    # Current lap time

    laptime = round((time.time() - lasttime), 2)

    # Total time since timer started
    total_time = round((time.time() - starttime), 2)

    #Printing the lap number, lap itme, and total time
    print("Lap No. "+str(lapnum))
    print("Lap Time: "+str(laptime))
    print("Total Time: "+str(total_time))

    #Updating the previous total time and lap number
    lasttime = time.time()
    lapnum += 1
print("Excersice complete!")
