a = int(input("Enter marks of Student 1: "))
b = int(input("Enter marks of Student 2: "))
avg = (a + b) / 2

print("Average Marks:", avg)

if a > b:
    print("Student 1 scored higher")
elif b > a:
    print("Student 2 scored higher")
else:
    print("Both students scored equal marks")