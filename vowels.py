l=[]
s=input("the word is")
vowels=("a","e","i","o","u")
for i in s:
    if i in vowels:
        l.append(i)
print("the vowels:",l)        
