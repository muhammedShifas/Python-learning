def longestAlternatingParityRun(numbers):
    count=1
    largest=1
    if len(numbers)==0:
        return 0
    for i in range(0, len(numbers)-1):
        if numbers[i]%2!=0 and numbers[i+1] %2==0:
            count=count+1
        elif numbers[i]%2==0 and numbers[i+1] %2!=0:
            count=count+1 
        else:
            count=0
        if count>largest:
            largest=count
    return largest                   
               
        
