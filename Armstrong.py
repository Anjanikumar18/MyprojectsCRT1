def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
def sod(num, n):
    if num == 0:
        return 0
    else:
        return power(num % 10, n) + sod(num // 10, n)
def armstrong(number):
    n = len(str(number))
    sumofdigits = sod(number, n)
    return sumofdigits == number
number = int(input("Enter a number: "))
if armstrong(number):
    print(" is an Armstrong number.")
else:
    print(" is not an Armstrong number.")
