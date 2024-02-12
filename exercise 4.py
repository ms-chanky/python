print("Grades calculator.")
maths = int(input("Maths: "))
eng = int(input("English: "))
phyc = int(input("Physics: "))
kisw = int(input("Kiswahili: "))
hist = int(input("History: "))
total_score = maths + eng + phyc + kisw + hist
average = total_score / 5

if average>=71 and average<=100:
    print("A")
elif average>=61 and average<=70:
    print("B")
elif average>=51 and average<=60:
    print("C")
elif average>=41 and average<=50:
    print("D")
elif average>=0 and average<=40:
    print("E")
else:
    print("Invalid")

