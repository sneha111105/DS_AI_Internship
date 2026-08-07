numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)
print("\nList:", numbers)5
print("Minimum Value:", min(numbers))
print("Maximum Value:", max(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Total Length:", len(numbers))
print("Sorted List:", sorted(numbers))