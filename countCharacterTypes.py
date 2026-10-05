def countCharacterTypes(text):
    letter=0
    digit=0
    others=0
    result=[]
    for i in range(0,len(text)):
        if text[i].isalpha()!=True and text[i].isdigit()!=True:
            others=others+1
        elif text[i].isalpha()==True:
            letter=letter+1
        elif text[i].isdigit()==True:
            digit=digit+1
                    
    result.append(letter)        
    result.append(digit)        
    result.append(others)
    return result        
