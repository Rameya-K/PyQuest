print("List Operations")

numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = float(input("Enter a number: "))
    numbers.append(num)

if len(numbers) > 0:
    print("List:", numbers)
    print("Largest number:", max(numbers))
    print("Smallest number:", min(numbers))
    print("Average:", sum(numbers) / len(numbers))
else:
    print("List is empty")