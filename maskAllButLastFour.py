def maskAllButLastFour(digits):
    if len(digits)<=4:
        return digits
    res=""    
    for i in range(0, len(digits)):
        if i <= len(digits)-5:
            res=res+"*"
        else:
            res=res+digits[i]
    
    return res                
