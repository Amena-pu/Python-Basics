y=int(input())
numbers = [1, 2, 3, 4, 5, 1, 4, 5, 6, 7, 98, 56]
Sum = sum(numbers)
average = Sum / len(numbers)
print ("average %i"%average)
if average%2==1:
    print("Average value Odd")
else:
    print("Average value Even")
sum1 =average
for b in range(1,9):
    value=(b+sum1)
    print(" %i"%value)

