def cartTotal(prices, quantities):
    sum=0
    for x, y in zip(prices, quantities):
        sum=sum+x*y
    return sum    
