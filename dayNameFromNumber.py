def dayNameFromNumber(dayNumber):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",]
    if dayNumber>0 and dayNumber<8:
        return days[dayNumber-1]
    else:
        return "Unknown"    
