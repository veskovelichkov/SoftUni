command = input()
current_index = 0
new_message = ''
while True:
    if command == 'end of comments':
        break
    if current_index == 0:
        new_message += f"""<h1>
    {command}
</h1>
"""
    elif current_index == 1:
        new_message += f"""<article>
    {command}
</article>
"""
    else:
        new_message += f"""<div>
    {command}
</div>
"""
    current_index += 1
    command = input()
print(new_message)
