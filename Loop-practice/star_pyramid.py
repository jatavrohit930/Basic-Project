# #print star pyramid 
# n=int(input("Enter the rows:-"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# #print reverse pyramid by star
# n=int(input("Enter the rows:-"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# n=int(input("Enter the row:-"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()



# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# n=int(input("Enter the row:-"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



# 1 
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# n=int(input("Enter the row:-"))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


n=int(input("Enter the row:-"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()