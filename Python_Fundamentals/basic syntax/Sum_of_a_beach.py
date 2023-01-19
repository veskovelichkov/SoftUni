word=input()
word=word.lower()
counter=0
for i in range(len(word)):
    if word[i:i+3]=="sun":
        counter+=1
    if word[i:i+4]=="sand" or word[i:i+4]=="fish":
        counter+=1
    if word[i:i+5]=="water":
        counter+=1
print(counter)