def maxAbsoluteValue(numbers):
    largest=0
    for i in numbers:
        if abs(i)>largest:
            largest=abs(i)
    return largest        
