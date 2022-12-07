def swap(string):
    start=string[-1]
    end=string[0]
    swapped_string=start+string[1:-1]+end
    print(swapped_string)
a=input("enter the string")
swap(a)
