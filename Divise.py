#take integer input from user,if it is divisible by 3 and 6 print good number , 2 and 7 as average number ,4 or 9 then print awesome number else print bad number
a=int(input("enter any number"))
if a%3==0 & a%6==0:
    print("good number")
elif a%2==0 & a%7==0:
    print("average number")
elif a%4==0 or a%9==0:
    print("awesome number")
else:
    print("bad number")