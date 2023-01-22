lines=int(input())
is_balanced=True
sentance=''
for _ in range(lines):
    string=input()
    if string=='(' or string==')':
        sentance+=string
for i in range(len(sentance)-1):
    if sentance[i]=='(' and sentance[i+1]!=')':
        is_balanced=False
if sentance[0]==')':
    is_balanced=False
if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')