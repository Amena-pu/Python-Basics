y=int(input())
x=int(input())
numbers = [1, 2, 3, 4, 5, 1, 4, 5, 6, 7, 98, 56]
Sum = sum(numbers)
square = x**2
print ("Square %i"%square)
if len(numbers)%2==0:
    print("Python is easy")
else:
    print("Python is hard")
sum1 =square
for b in range(1,len(numbers)):
    val= (b*square)
    print(" %i\n"%val)