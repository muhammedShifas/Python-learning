words = ["pear", "fig", "apple", "kiwi"]

for i in range(len(words)):
    smallest=i
    for j in range(i+1,len(words)):
        if len(words[j])<len(words[smallest]):
            smallest=j
        elif len(words[j])==len(words[smallest]):
            if words[j]<words[smallest]:
                smallest=j
    words[i],words[smallest]=words[smallest],words[i] 
print(words)                   



# for i in range(len(words)):
#     smallest = i

#     for j in range(i + 1, len(words)):
#         if len(words[j]) < len(words[smallest]):
#             smallest = j
#         elif len(words[j]) == len(words[smallest]):
#             if words[j] < words[smallest]:
#                 smallest = j

#     words[i], words[smallest] = words[smallest], words[i]

# print(words)