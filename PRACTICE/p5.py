#polindrome serise
num=int(input("Enter the series:-"))
org=num
rev=0

while num >0:
    digit = num%10
    rev = rev*10 + digit
    num//=10

if org == rev:
      print("polindrome series")
else:
      print("is not polindrome series")

