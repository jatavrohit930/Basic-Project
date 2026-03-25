#check the grade(marks)
n=int(input("Enter the marks:-"))

if n<30:
    print("fail,Grade-D")
elif n<50:
    print("pass,Grade-C")
elif n<75:
    print("Pass,Grade-B")
else:
    print("Pass with Dist,Grade-A")