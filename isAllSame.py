def isAllSame(items):
    
    for i in items:
       for j in items:
           if i!=j:
               return False
    return True            
