#write a program to find the second smallest negative number from the list without using min,max or sort
a=[-1,42,65,1,-4,6]
mini=a[0]
for i in range(len(a)):
    while a[i]<0 and a[i]>mini:
        mini=a[i]
        print(mini)
