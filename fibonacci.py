limit=int(input('Enter the limit'))
f1=int(input('Enter the number'))
f2=int(input('Enter the number'))
print("Fibonacci is:")
print(f1,f2, end="  ")
for i in range(2,limit+1):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3, end="  ")