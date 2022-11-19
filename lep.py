year=int(input("enter the current"))
future=int(input("enter the future"))
for year in range (year,future):
      if year%4==0 and year%100!=0 or year%400==0:
          print(year)
    
        
