scores={'a': 3, 'b': 9, 'c': 5}
items=list(scores.items())
for i in range(0,len(items)):
    highest=i
    for j in range(i+1,len(items)):
        if items[j][1]>items[highest][1]:
            highest=j
        if items[j][1]==items[highest][1]:
            if items[j]>items[highest]:
                highest=j
    items[i],items[highest]=items[highest],items[i]
result=[]
for i in range(0,len(items)):
    result.append(items[i][0])    
print(result)                    
