print("Student Marks Management")

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
elif average >= 40:
    print("Grade: E")
else:
    print("Grade: F")