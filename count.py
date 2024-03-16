# write the recursive function to count the number od digits of number
def count(n):
    if(n==0):
        return 0
    return 1+count(n//10)
n=int(input())
print(count(n))