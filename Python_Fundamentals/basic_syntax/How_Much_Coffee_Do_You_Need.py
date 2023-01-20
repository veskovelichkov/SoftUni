counter=0
while True:
    event=input()
    if event=="END":
        break
    if event=="coding" or event=="dog" or event=="cat" or event=="movie":
        counter+=1
    elif event=="CODING" or event=="DOG" or event=="CAT" or event=="MOVIE":
        counter+=2
if counter>5:
    print("You need extra sleep")
else:
    print(counter)