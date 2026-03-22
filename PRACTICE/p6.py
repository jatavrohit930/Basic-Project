# #check prime number
# num=int(input("Enter the number:="))
# count=0
# for i in range(1,num+1):
#     if (num%i==0):
#         count += 1

# if(count==2):
#         print("prime num")   
# else:
#         print("not prime")

#OR
n=int(input("Enter the number:="))
for i in range(2, n):
      if(n%i==0):
            print("not prime")
            break
      else:
            print("prime ")



    