#sum of divisor is equal to no. then it is called perfect no.
n=int(input("Enter the no.:-"))
sum=0

for i in range(1,n):
    if (n%i==0):
        sum+=i
if sum==n:
    print(n,"is a perfect num")
else:
    print(n,"is not a perfect num")

  