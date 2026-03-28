# #Armstrong number=sum of digit raise to power of number of digit -original number
# limit = int(input("Enter the limit: "))
# print("Armstrong numbers up to", limit, "are:")
# for num in range(1, limit + 1):
#     order = len(str(num))  # number of digits
#     temp = num
#     sum = 0

#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
# print(sum)

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
    if sum==num:
        print(num)