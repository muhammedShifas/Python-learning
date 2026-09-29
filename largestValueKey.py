def largestValueKey(scores):
    largest= -10
    res=""
    for key,value in scores.items():
        if value>largest:
            largest=value
            res=key
    return res        
