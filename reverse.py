# write recursion program to print the digits in reverse order
def reverse(n):
    if n==0:
        return 0
    print(n%10)
    return reverse(n//10)
n=int(input())
reverse(n)