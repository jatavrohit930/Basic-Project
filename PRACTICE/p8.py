n=int(input("Enter the no.:-"))
count=0
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
    count+=1
print(count)