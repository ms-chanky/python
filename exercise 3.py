# number = int(input("number: "))
# if number > 0:
#     print("Positive number")
# elif number < 0:
#     print("Negative number")
# elif number == 0:
#     print("Number is 0")
# else:
#     print("Invalid Input")

eng = 89
maths = -9

# if maths and eng > 0:
#     print("All are positive")
# else:
#     print("one or all of the numbers are negative or zero")

if maths > 0 or eng > 0:
    print("One is positive")
elif maths < 0 or eng < 0:
    print("Both are negative")
else:
    print("Both are positive")