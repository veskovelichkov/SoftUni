a=float(input())
if a>0:
    if a<1:
        print("small positive")
    elif a>1000000:
        print("large positive")
    else:
        print("positive")
elif a<0:
    if a>-1:
        print("small negative")
    elif a<-1000000:
        print("large negative")
    else:
        print("negative")
else:
    print("zero")