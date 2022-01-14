for i in range(int(input())):
    Dd,Td,DMd=map(int,input().split())
    Ds,Ts,DMs=map(int,input().split())
    Md=Dd+Td+DMd
    Ns=Ds+Ts+DMs
    if(Md==Ns):
        if(Dd>Ds):
            print("DRAGON")
        elif(Dd==Ds):
            if(Td>Ts):
                print("DRAGON")
            elif(Td==Ts):
                print("TIE")
            else:
                print("SLOTH")
        else:
            print("SLOTH")
    elif(Md>Ns):
        print("DRAGON")
    else:
        print(SLOTH)
    
        
    