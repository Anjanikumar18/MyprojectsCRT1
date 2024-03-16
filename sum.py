# write a recurive function to calculate the sum of digits of a number
def sum(n):
    if n==0:
        return 0
    return n%10+sum(n//10)
n=int(input())
print(sum(n))