def findMissingNumberInRange(numbers):
    for i in range(1,10):
        found=False
        for j in range(0,len(numbers)):
            if i==numbers[j]:
                found=True
        if found==False:
            return i        
        
       
