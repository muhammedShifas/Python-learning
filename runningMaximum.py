def runningMaximum(numbers):
    import math
    largest=-math.inf
    for i in range(0,len(numbers)):
        if numbers[i]>=largest:
            largest=numbers[i]
        else:
            numbers[i]=largest
    return numbers            
