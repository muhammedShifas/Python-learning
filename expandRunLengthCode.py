def expandRunLengthCode(code):
    alph=[]
    digits=[]
    num=0
    count=0
    res=""
    found=False
    for i in range(0,len(code)):
        if code[i].isdigit()!=True:
            alph.append(code[i])
            found=True
            count=count+1
            
        else:
            num=num*10+int(code[i]) 
            
        if found==True and count>1:
            digits.append(num)
            num=0
        elif len(code)<3:
            num=1
            digits.append(num)       
            
            
          
    for j in range(0,len(alph)):
        for k in range(0,digits[j]):
            res=res+alph[j]
    return res        
                        
