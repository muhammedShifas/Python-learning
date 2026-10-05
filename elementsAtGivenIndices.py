def elementsAtGivenIndices(items, indices):
    result=[]
    for i in range(0,len(indices)):
        for j in range(0,len(items)):
            if j==indices[i]:
                result.append(items[j])
    return result            
                
