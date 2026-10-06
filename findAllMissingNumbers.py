def findAllMissingNumbers(numbers, limit):
    res=[]
    for i in range(1,limit+1):
        found=False
        for j in range(0,len(numbers)):
            if i==numbers[j]:
                found=True
        if found==False:
            res.append(i)
    return res        
