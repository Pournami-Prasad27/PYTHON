l=[]
s=input("the word is")
vowels=("a","e","i","o","u","A","E","I","O","U")
for i in s:
    if i in vowels:
        l.append(i)
print("the vowels:",l)        
