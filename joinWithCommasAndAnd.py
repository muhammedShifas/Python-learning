def joinWithCommasAndAnd(words):
    result=""
    for i in range(0, len(words)):
        if i==0:
            result=words[i]
        elif i!=len(words)-1:
            result=result+", "+words[i]
        else:
            result=result+" and "+words[i]    
         
    return result          
            
            
        
