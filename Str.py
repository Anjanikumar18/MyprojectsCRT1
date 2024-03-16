#calculate sum of first and last digit of a number
def fun(a):
    b=str(a)
    c=str(b[-1]+str(b[0]))
    sum=0
    for i in c:
        sum=sum+int(i)
    print(sum)
a=int(input("enter a no:"))
fun(a)

