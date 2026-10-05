def roundToTwoDecimals(numbers):
    for i in range(0,len(numbers)):
        numbers[i]=round(numbers[i], 2)
    return numbers    
