#check the perfect number
n = int(input("Enter the no. :-"))
sum = 0
for i in range(1 , n):
   if n%i==0:
       sum+=i
print("sum of divisor",sum,"=",n)
print("So,")
if sum == n:
    print(n,"is perfect no.")
else:
    print(n,"is not perfect no.")

