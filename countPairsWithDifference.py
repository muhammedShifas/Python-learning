def countPairsWithDifference(numbers, k):
    count=0
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i]-numbers[j])==k:
                count+=1
    return count            
