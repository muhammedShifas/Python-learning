def ordinalSuffix(n):
    if n==11 or n==12 or n==13:
        return str(n)+"th"
    if n>110 and n<120:
        return str(n)+"th"    
    n=str(n)
    if n[-1]=='1':
        return n+"st"
    if n[-1]=='2':
        return n+"nd"
    if n[-1]=='3':
        return n+"rd"
    if int(n)>3:
        return str(n)+"th"
                   
