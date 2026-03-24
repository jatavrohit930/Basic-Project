#check the even and odd numbers with print which is odd and even
n=int(input("Enter the numbers :-"))

even=0
odd=0

for i in range(0,n+1):
    if i%2==0:
        print(i,"is even")
        even+=1
    else:
        print(i,"is odd")
        odd+=1

print("Even=",even)
print("Odd=",odd)

