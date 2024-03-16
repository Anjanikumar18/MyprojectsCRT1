#FUNC WITH TWO arguments a and b ,typecast the value of 2nd argument into integer,then multiply both arguments and print the last digit of result
def func(a,b):
    b=int(b)
    c=a*b
    d=str(c)
    print(d[-1])
func(5,4)

def check(a,b):
    print(b)
check(b=11,a=12)

def city(name="praveen",place="vizag"):
    print("My name is",name,"I'm From ",place)
city()
city(name="ramana gadu",city="Bheemunipatnam")
    