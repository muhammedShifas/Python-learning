def countItemsAbove(numbers, limit):
    count=0
    for i in numbers:
        if i>limit:
            count+=1
    return count        
