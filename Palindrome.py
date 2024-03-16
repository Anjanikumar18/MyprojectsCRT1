#write a python program to find sum of digits of the number 1578 ,also while adding sum each digit is multiplied by its position in that number ranging from 1st to 4th positions,use only while loop and functions should not be used
num = 1578
sod= 0
pos= 1
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
num = rev
while num > 0:
    digit = num % 10
    sod += digit * pos
    num = num // 10
print("The sum of digits of the number 1578, with each digit multiplied by its position, is:")
