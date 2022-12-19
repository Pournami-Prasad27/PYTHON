a=[]
n=int(input("Enter the size of list"))
for i in range(1,n+1):
    print("Enter the",i,"element")
    inp=input()
    a.append(inp)
max_1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max_1):
        max_1=len(i)
        temp=i
print("The word with the longest lenghth is",temp,"with",max_1)