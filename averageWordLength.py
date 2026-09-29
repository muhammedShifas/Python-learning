def averageWordLength(sentence):
    total=0
    words=sentence.split()
    for i in words:
        total+= len(i)
    average=total/len(words)
    return round(average, 2)