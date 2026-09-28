def initialsFromFullName(fullName):
    result=""
    name=fullName.split(" ")
    for i in range(0, len(name)):
        result=result+name[i][0].upper()+"."
    
    
    return result      
        
