def pairUpTwoLists(first, second):
    res=[]
    for x,y in zip(first, second):
        res.append([x,y])
    return res    
