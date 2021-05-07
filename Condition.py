y=int(input())
x=int(input())
numbers = [1, 2, 3, 4, 5, 1, 4, 5, 6, 7, 98, 56]
Sum = sum(numbers)
print(Sum)
odd_square = [x**2 for x in range(1,11) if x%2==1]
print (odd_square)
if len(numbers)%2==0:
    print("Python is easy")
else:
    print("Python is hard")
