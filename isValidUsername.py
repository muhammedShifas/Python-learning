def isValidUsername(name):
    found=False
    for i in name:
        if i.islower() or i.isdigit() or i=='_':
            pass
        else:
             return False 
        if i=='_':
            found=True
    if found==True:
        return True
    else:
        return False    
                  
