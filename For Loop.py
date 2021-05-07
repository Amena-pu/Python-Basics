import constant
print(constant.pi)
if constant.pi%2==0:
    print("It's a even value")
else:
    print("It's a odd value")
list = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for val in list:

 sum = sum+val
 mul = constant.pi*sum
print(sum)
print(mul)
print(len(list))



