def ATM:
name=["safu","ruhi","zoya","saff"]
pw=["safu1","ruhi1","zoya1","anita"]
pin=[2014,2015,2023,2024]
balance=[500,600,700,800]
print("enter your username:",end=" ")
a=input()
if(a in name):
    print("enter your pw:")
    b=input()
else:
    print("invalid username")
if(b in pw):
    print("1.withdrwal 2.deposit 3.account balance 4.change pw")
else:
    for i in range(2,0,-1):
        print("incorrect password you have "+str(i)+"attempts left")

    