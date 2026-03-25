# #Print Fibonacci Series up to N terms
# n=12
# sum=0
# for i in range(0,n+1):
#     sum=i+sum
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b