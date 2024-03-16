def passcheck(x):
    if(len(x)>=8):
        l,u,d,s=0,0,0,0
        for i in x:
            if(i.islower()):
                l=l+1
            elif(i.isupper()):
                u=u+1
            elif(i.isdigit()):
                d=d+1
            else:
                s=s+1
        if(l>=1 and u>=1 and d>=1 and s>=1):
            return True
        else:
            return False
                
            


def withdraw():
    print("enter the amountL:")
    amount=int(input())
    print("enter your unique pin")
    pc=int(input())
    if(pc!=pin[i]):
        print("invalid pin")
        print("end")
    else:
        if(amount>bal[i]):
            print("insufficient balance")
            print("end")
        else:
            bal[i]-=amount
            print("collect ur amount")
            print("do you want to display balance? (y/n)")
            a=input()
            if(a=='y'):
                print("ur avaialble balance is:",bal[i])
                print("thank you for banking with us")
            else:
                print("thank you for banking with us")
 def deposit():
     
        

def cse(i):
    print("enter password:")
    pc=input()
    if(pc!=pc[i]):
        print("wrong passwords,more 2 attempts")
        pc=input()
        if(pc!=pc[i]):
            print("wrong password,more 1 attempt")
            pc=input()
            if(pc!=pc[i]):
                print("wrong password,account blocked")
            else:
                flag=1
        else:
            flag=1
    else:
        flag=1
     if(choice in [1,2,3,4]):
         break
     else:
         print("wrong choice:reenter:")
         
user=["safu","ruhi","zoya","saff"]
passcode=["safu1","ruhi1","zoya1","anita"]
pin=[2014,2015,2023,2024]
bal=[500,600,700,800]
print("enter username:")
user_name=input()
if(user_name in user):
    i=user.index(user_name)
    cse(i)
else:
    print("user doesnt exist")

    