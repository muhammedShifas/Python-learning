def daysInMonth(month, year):
    months=[1,2,3,4,5,6,7,8,9,10,11,12]
    days=[]
    if year%4==0 and year%100!=0:
        days=[31,29,31,30,31,30,31,31,30,31,30,31]
        num=month-1
        return days[num]
    elif year%4==0 and year%100!=0 and year%400!=0:
        days=[31,29,31,30,31,30,31,31,30,31,30,31]
        num=month-1
        return days[num]
    else:
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        num=month-1
        return days[num]   
            
        
