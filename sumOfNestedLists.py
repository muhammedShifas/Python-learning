def sumOfNestedLists(rows):
    sum=0
    for i in range(0,len(rows)):
        for j in range(0,len(rows[i])):
            sum=sum+rows[i][j]
    return sum        
