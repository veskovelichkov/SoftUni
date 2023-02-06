def loading_bar(perc):
    if perc == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{perc}% [{'%' * (perc // 10)}{'.' * (10 - perc // 10)}]\nStill loading..."


percentage = int(input())
print(loading_bar(percentage))
