def clockToTwelveHour(hour24):
    res=""
    hour=[13,14,15,16,17,18,19,20,21,22,23]
    if hour24<12:
        if hour24==0:
            res="12"+" "+"AM"
    elif hour24==12:
        res="12"+" "+"PM"    
    else:
        for i in range(0, len(hour)):
            if hour24==hour[i]:
                res=str(i+1)+" "+"PM"
    
    return res        
