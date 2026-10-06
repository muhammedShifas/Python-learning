def consecutiveDifferences(numbers):
    arr=[]
    diff=0
    if len(numbers)<2:
        return arr
    for i in range(0,len(numbers)-1):
        diff=numbers[i+1]-numbers[i]
        arr.append(diff)
    return arr    
            
