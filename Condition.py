y=int(input())
x=int(input())
numbers = [1, 2, 3, 4, 5, 1, 4, 5, 6, 7, 98, 56]
Sum = sum(numbers)
odd_square = x**2
print ("Odd square %i"%odd_square)
if len(numbers)%2==0:
    print("Python is easy")
else:
    print("Python is hard")
sum1 =odd_square
for b in range(1,len(numbers)):
    val= (b*odd_square)
    print(" %i\n"%val)

