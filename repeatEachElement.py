def repeatEachElement(items, times):
    count=0
    result=[]
    for i in range(0,len(items)):
        count=0
        while count<times:
            result.append(items[i])
            count+=1
    return result        
            
