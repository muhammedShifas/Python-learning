def alternatingSum(numbers):
    res=0
    for i, x in enumerate(numbers):
        if i%2!=0:
            res=res-x
        else:
            res=res+x    
        
    return res    
 