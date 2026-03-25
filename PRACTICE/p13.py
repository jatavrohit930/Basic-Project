# a =  int(input("Enter the 1 no. :-"))
# b =  int(input("Enter the 2 no. :-"))
# c =  int(input("Enter the 3 no. :-"))
# if(a==b==c):
#     print("your type numbers are equal ")
# else:
#     if a > b and a > c :
#         if b > c:
#              print(b,"is second greater")
#         else:
#               print(c,"is second greater")
#     elif b>c:
#         if c>a :
#             print (c,"is second greater")
#         else:
#             print(a, "is second greater")
            
#     else:
#         if b>a:
#             print(b, "is second greater")
#         else:
#             print(a, "is second greater")

#or
a =  int(input("Enter the 1 no. :-"))
b =  int(input("Enter the 2 no. :-"))
c =  int(input("Enter the 3 no. :-"))
if (a>b and a<c) or (a>c and a<b):
    print(a, "is second greater")
elif(b>a and b<c) or (b>c and b<a):
    print(b, "is second greater")
else:
    print(c,"is second greater")


