def multiplicationTableRow(n, upTo):
    res= list(range(1, upTo+1))
    for i in range(0, len(res)):
        res[i]=res[i]*n
    return res    