def grade(avg):
    if 90 <= avg <= 100:
        return "A+"
    elif 80 <= avg < 90:
        return "A"
    elif 70 <= avg < 80:
        return "B"
    elif 60 <= avg < 70:
        return "C"
    elif 50 <= avg < 60:
        return "D"
    else:
        return "F"
def student_result():
    name = input("Enter Student Name: ")
    marks = []
    while True:
        mark = input("Enter Mark (or type 'done' to finish): ")

        if mark.lower() == "done":
            break

        marks.append(float(mark))

    if len(marks) == 0:
        print("No marks entered.")
        return

    avg = sum(marks) / len(marks)
    g = grade(avg)

    print("\n----- Student Result -----")
    print("Name    :", name)
    print("Marks   :", marks)
    print("Average :", (sum(marks) / len(marks)))
    print("Grade   :", g)


student_result()
