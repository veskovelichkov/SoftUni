tickets = input().split(", ")
tickets_stripped = [ticket.strip() for ticket in tickets]
winning_characters = ['@', '#', '$', '^']
for ticket in tickets_stripped:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    first_half = ticket[:10]
    second_half = ticket[10:]
    is_winning = False
    for character in winning_characters:
        for index in range(10, 5, -1):
            if character * index in first_half and character * index in second_half:
                if index == 10:
                    print(f'ticket "{ticket}" - {index}{character} Jackpot!')
                    is_winning = True
                    break
                else:
                    print(f'ticket "{ticket}" - {index}{character}')
                    is_winning = True
                    break
            if is_winning:
                break
    if not is_winning:
        print(f'ticket "{ticket}" - no match')
