a=[22,-1,42,65,1,-4,6]
m1=999
m2=999
for i in range(len(a)):
    if a[i]<m1:
        m2=m1
        m1=a[i]
print(m2)
#2nd method
a=[22,-1,42,65,1,-4,6]
mini=a[0]
mini2=a[0]
for i in range(len(a)):
    if mini>a[i]:
        mini=a[i]
for i in range(len(a)):
    if mini2>a[i] and a[i]!=mini:
        mini2=a[i]
print(mini2)
