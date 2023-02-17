def add_lesson(list_lessons, chosen_lesson_title):
    if chosen_lesson_title not in list_lessons:
        list_lessons.append(chosen_lesson_title)
    return list_lessons


def insert_lesson(list_lessons, chosen_lesson_title, chosen_index):
    if chosen_lesson_title not in list_lessons:
        list_lessons.insert(chosen_index, chosen_lesson_title)
    return list_lessons


def remove_lesson(list_lessons, chosen_lesson_title):
    if chosen_lesson_title in list_lessons:
        lesson_index = list_lessons.index(chosen_lesson_title)
        if lesson_index+1 in range (len(list_lessons)):
            if "Exercise" in list_lessons[lesson_index + 1]:
                list_lessons.pop(lesson_index + 1)
        list_lessons.remove(chosen_lesson_title)
    return list_lessons


def swap_lesson(list_lessons, first_title, second_title):
    if first_title in list_lessons and second_title in list_lessons:
        first_title_index = list_lessons.index(first_title)
        second_title_index = list_lessons.index(second_title)
        first_title_exercise = False
        second_title_exercise = False
        if first_title_index + 1 in range(len(list_lessons)):
            first_title_exercise = "Exercise" in list_lessons[first_title_index + 1]
        if second_title_index + 1 in range(len(list_lessons)):
            second_title_exercise = "Exercise" in list_lessons[second_title_index + 1]
        if not first_title_exercise and not second_title_exercise:
            list_lessons[first_title_index], list_lessons[second_title_index] = list_lessons[second_title_index], \
                                                                                list_lessons[first_title_index]
        elif first_title_exercise and second_title_exercise:
            list_lessons[first_title_index], list_lessons[first_title_index + 1], list_lessons[second_title_index], \
            list_lessons[second_title_index + 1] \
                = list_lessons[second_title_index], list_lessons[second_title_index + 1], list_lessons[
                first_title_index], list_lessons[first_title_index + 1]
        elif first_title_exercise and not second_title_exercise:
            exercise_save = list_lessons.pop(first_title_index + 1)
            list_lessons[first_title_index], list_lessons[second_title_index] = list_lessons[second_title_index], \
                                                                                list_lessons[first_title_index]
            list_lessons.insert(second_title_index + 1, exercise_save)
        elif not first_title_exercise and second_title_exercise:
            exercise_save = list_lessons.pop(second_title_index + 1)
            list_lessons[first_title_index], list_lessons[second_title_index] = list_lessons[second_title_index], \
                                                                                list_lessons[first_title_index]
            list_lessons.insert(first_title_index + 1, exercise_save)
    return list_lessons


def exercise(list_lessons, chosen_lesson_title):
    if chosen_lesson_title in list_lessons:
        lesson_index = list_lessons.index(chosen_lesson_title)
        if lesson_index+1 in range(len(list_lessons)):
            if "Exercise" not in list_lessons[lesson_index + 1]:
                list_lessons.insert(lesson_index + 1, f"{chosen_lesson_title}-Exercise")
        else:
            list_lessons.append(f"{chosen_lesson_title}-Exercise")
    else:
        list_lessons.append(chosen_lesson_title)
        list_lessons.append(f"{chosen_lesson_title}-Exercise")
    return list_lessons


lessons = list(map(str, input().split(", ")))
command = input()
while command != 'course start':
    command_split = command.split(":")
    event = command_split[0]
    lesson_title = command_split[1]
    if event == "Add":
        lessons = add_lesson(lessons, lesson_title)
    if event == "Insert":
        index = int(command_split[2])
        lessons = insert_lesson(lessons, lesson_title, index)
    if event == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    if event == "Swap":
        swap_title = command_split[2]
        lessons = swap_lesson(lessons, lesson_title, swap_title)
    if event == "Exercise":
        lessons = exercise(lessons, lesson_title)
    command = input()
for index, course in enumerate(lessons):
    print(f"{index + 1}.{course}")
