#program to check the type of triangle where input taken from user and classify it accordingly into equi
a=int(input("enter 1st side:"))
b=int(input("enter 2nd side:"))
c=int(input("enter 3rd side:"))
if a==b or b==c or a==c :
    print("isosceles triangle")
elif a==b==c:
    print("eqilateral triangle")
else:
    print("scalene triangle")


