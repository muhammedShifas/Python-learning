def hoursAndMinutesFromMinutes(totalMinutes):
    clock=[]
    time=totalMinutes//60
    clock.append(time)
    time=totalMinutes%60
    clock.append(time)
    return clock
