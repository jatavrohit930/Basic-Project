# #print no. from 1 to n
# n=int(input("Enter the no."))
# # for i in range(n+1):
# #     print(i)

# #sum of digit no.
# n=int(input("Enter the no."))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("sum of digit is",sum)

# #Reverse number 
# n=int(input("Enter the no."))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print(rev)

#count of digit
# n=int(input("Enter the no."))
# count=0
# # while n>0:
# #     n//=10
# #     count+=1
# # print(count)

# #factorial calculatev
# n=int(input("Enter the no."))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# #fibonacci series
# n= int(input("Enter the no."))
# a=0
# b=1
# print("fibnocci series")
# for i in range(1,n+1):
#     print(a, end=",")
#     c=a+b
#     a=b
#     b=c

#Armstrong number=sum of digit raise to power of number of digit -original number
# Armstrong series up to a given number

limit = int(input("Enter the limit: "))

print("Armstrong numbers up to", limit, "are:")

for num in range(1, limit + 1):
    order = len(str(num))  # number of digits
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

print(sum)