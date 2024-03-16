a=input()
u,d,s,l,c=0,0,0,0
for i in a:
    if(i.isupper()):
        u[0]=1
    elif(i.islower()):
        u[1]=1
    elif(i.isdigit()):
        u[2]=1
    else:
        u[3]=1
z=4-sum(u)
if(len(a)>=8):
    print(z)
else:
    print(max(z,8-len(a)))
