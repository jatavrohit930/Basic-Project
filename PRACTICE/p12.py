#Find Factorial (without recursion first, then with recursion)
n = int(input("Enter the fact. value:-"))
fact=1
for i in range(1,n+ 1):
    fact *= i
print(n,"factorial is:-",fact)