list=[]
limit=int(input('Enter the limit'))
for i in range(0,limit):
    print('Enter the elements')
    inp=int(input())
    list.append(inp)
s=0
for i in list:
    s=s+i
print("sum=",s)