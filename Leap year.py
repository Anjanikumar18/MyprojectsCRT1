#checking if a given year is leap year or not i.e your year is divisible by 4 and not divisible by 100 or if it is divisible by 400 then it is called leap year
a=int(input("enter the year:"))
if ((a%4==0 and a%100!=0)) or (a%400==0):
    print("year is leap year")
else:
    print("this is not leap year")
    
    