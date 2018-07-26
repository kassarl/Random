#Sleep Calculator 
#This is super basic I did this in 3 minutes. 
import time
import math
start =int(input("Input your sleep time in HHMM format (military time):"))
alarm =int(input("Input the time you want to wake up in HHMM format (military time): "))

timeAwake = start - alarm
timeAsleep = 2400 - timeAwake
print("You fall asleep at %d h and wake up at %d h you will have:" %(start, alarm))
hoursAsleep = math.floor(timeAsleep / 100)

minutesAsleep = (timeAsleep - 100* (hoursAsleep))

print("%dh %.0dm of sleep" % (hoursAsleep, minutesAsleep))
#print("%dh awake" %timeAwake)
