def twoSumIndices(numbers, target):
    arr=[]
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                arr.append(i)
                arr.append(j)
    return arr            
            
                 
