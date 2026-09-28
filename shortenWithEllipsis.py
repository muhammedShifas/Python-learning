def shortenWithEllipsis(text, limit):
    res=""
    if len(text)<=limit:
        return text
        
    
    for i in range(0, limit):
        res=res+text[i]
    
    
    res=res+"..." 
    return res   
