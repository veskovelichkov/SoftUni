times_string=input().split(" ")
times_integers=[]
for value in times_string:
    times_integers.append(int(value))
times_left=[]
times_right=[]
events_left=(len(times_integers)-1)//2
for event_left in range(0,events_left):
    times_left.append(times_integers[event_left])
for event_right in range((len(times_integers)+1)//2,len(times_integers)):
    times_right.append(times_integers[event_right])
left_finished=0
right_finished=0
for i in times_left:
    if i!=0:
        left_finished+=i
    else:
        left_finished=left_finished*0.8
for j in range(len(times_right)-1,-1,-1):
    if times_right[j]!=0:
        right_finished+=times_right[j]
    else:
        right_finished=0.8*right_finished
if right_finished<left_finished:
    print(f'The winner is right with total time: {right_finished:.1f}')
elif left_finished<right_finished:
    print(f'The winner is left with total time: {left_finished:.1f}')