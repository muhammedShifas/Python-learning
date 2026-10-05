def invertDictionary(mapping):
    obj={}
    for x,y in mapping.items():
        obj[str(y)] = x
    return obj   
