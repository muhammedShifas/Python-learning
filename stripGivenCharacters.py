def stripGivenCharacters(text, chars):
    result=""
    for i in range(0, len(text)):
        found=False
        for j in range(0, len(chars)):
            if text[i]==chars[j]:
                found=True
        if found==False:
            result=result+text[i]    
    
    return result    
