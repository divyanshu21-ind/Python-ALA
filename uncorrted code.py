print("Marks Distribution Analyzer")
students = int(input("Enter student count: "))
i = 0
distinction = 0
first = 0
second = 0
fail = 0

while i < students:
    marks = int(input("enter marks: "))
    if marks >= 75:
        distinction = distinction + 1
    elif marks >= 60:
        first = first + 1
    elif marks >= 35:
        second = second + 1
    else:
        fail = fail + 1
        i = i + 1
        print("distinction: ", distinction)
        print("first: ", first)
        print("second: ", second)
        print("fail: ", fail)
              tottal = distinction + first + second + fail
              if total != students:
                  print("counting error")
