#program for checking the on road price of a bike under the conditions 
#if the price is greater than 72k,then tax will be 10% of original price,insurance will be 15% of actual price
#if the price is greater than 150000 and less than 200000,then tax would be 25% and insurance will be 20%
#if the price is greater than 200000 then tax will be 35% and insurance will be 28%
#otherwise print as " minimum bike value is 72000,please enter valid value"
#actual price + tax+ insurance
a= int(input("enter the price of the bike"))
if a>72000:
    b= 10/100 *a + 15/100 *a
    c=a+b
    print(c)
elif a>150000 & a<200000:
    b= 25/100 *a + 20/100 *a
    c=a+b
    print(c)
elif a>200000:
    b=35/100*a +28/100*a
    c=a+b
    print(c)
else:
    print("false")

