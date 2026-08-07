def table(num):
    for i in range(1, 11):
        print(num, "*", i, "=", num * i)

number = int(input("Enter the table number: "))
table(number)