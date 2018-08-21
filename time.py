import time;

curTime = time.time()

def secToMin():
    return curTime/60;

def secToHour():
    return secToMin()/60;

def secToDay():
    return secToHour()/24;

def secToMonth():
    return secToDay()/30;

def secToYear():
    return (secToMonth()/12);


    

print ("Times since epoc not including leap years")
print ("Time in seconds since 1970",curTime)
print ("Time in Minutes since 1970",secToMin())
print ("Time in Hour since 1970",secToHour())
print ("Time in Days since 1970",secToDay())
print ("Time in Months since 1970",secToMonth())
print ("Time in Years since 1970",secToYear())



