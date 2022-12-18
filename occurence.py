def word_count(str):
    count=dict()
    words=str.split()
    for v in words:
        if v in count:
            count[v]+=1
        else:
            count[v]=1
    print(count)
a=input("enter the string")
word_count(a)
        
