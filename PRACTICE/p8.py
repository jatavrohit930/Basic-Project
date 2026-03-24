# #Count the number 
# n=int(input("Enter the no.:-"))
# count=0
# while n>0:
#     count+=1
#     n//=10
# print(count)

#count the number using for loop
num=int(input("Enter the no.:-"))
count=0
for dig in num :
    if dig>0:
        count+=1
        num//=10
print(count)