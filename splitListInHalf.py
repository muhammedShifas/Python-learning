def splitListInHalf(items):
    half= (len(items)//2)
    i=0
    items1=[]
    items2=[]
    res=[]
    while i < len(items):
        if i<half:
            items1.append(items[i])
        else:
            items2.append(items[i]) 
        i+=1
   
    res.append(items1)   
    res.append(items2)   
    return res 
               
        
