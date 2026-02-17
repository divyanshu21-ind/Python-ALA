print("Marks Distribution Analyzer")
students = int(input("Enter student count: "))
i = 0
distinction = 0
first = 0
second = 0
fail = 0

while i < students:
    marks = int(input("Enter marks: "))

    if marks >= 75:
        distinction = distinction + 1
    elif marks >= 60:
        first = first + 1
    elif marks >= 35:
        second = second + 1
    else:
        fail = fail + 1

    i = i + 1  # Corrected from i = i + i

print("Distinction:", distinction)
print("First Class:", first)
print("Second Class:", second)
print("Fail:", fail)  # Added closing parenthesis

total = distinction + first + second + fail

if total != students:
    print("Counting error")