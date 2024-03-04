print("\n","  "*5 ,"WELCOME TO CANARA ATM")
bal=50000
corr_pin=2004
print("\n"," "*5,"plese enter your pin numbere\n\n","   "*6,end="")
user_pin=int(input())


#atm method
def atm():
    if corr_pin==user_pin:
        
        print("  "*5,"press '1' for balance equiry\n","  "*5,"press '2' for withdraw\n","  "*5,"press '3' for pin change\n\n","  "*5,end="")
        opt=int(input())
        #for balancr enquiry
        if opt==1:
            print("  "*5,"\nyour balance is :",bal)
            print("  "*5,"\ndo you want to perform any other operation (y/n):",end="")
            a=input()
            
            if a=="y":
                atm()
            else:
                print("\n","  "*5,"Thanks for visit")
        #for withdraw
        if opt==2:
            #option two method
            def amount():
                print("\n","  "*5,"enter how much want to withdraw :",end="")
                wi_am=int(input())
                if bal>=wi_am:
                    def note():
                        if wi_am%100==0:
                    
                            print("\n","  "*5,"prossesing \n ","  "*5,"please collect the cash............")
                            global bal
                            bal=bal-wi_am
                            
                            print("\n","  "*5,"do you want to perform any other operation (y/n):",end="")
                            b=input()
                
                            if b=="y":
                                atm()
                            else:
                                print("\n"," "*5,"Thanks for visit")
         
                        else:
                            print("\n","  "*5,"sorry! this note is not available so plese enter valid amount")
                            amount()
                    note()   
                        
                else:
                    print("\n,","  "*5,"sorry! insufficiant balance")
                    amount()
            amount()
         #fro pin change
        if opt==3:
            #third option method
            def pin():
                global cp
                print("\n"," "*5,"plese enter your new pin:",end="")
                cp=int(input())
                print("\n"," "*5,"plese re-enter your new pin:",end="")
                cp2=int(input())
                if cp==cp2:
                    corr_pin=cp
                    print("\n","  "*5,"your pin successfully changed")
                    print("\n","  "*5,"do you want to perform any other operation (y/n):",end="")
                    c=input()
                    if c=="y":
                        atm()
                    else:
                        print("\n","  "*5,"Thaks for visit")
                else:
                    print("\n","  "*5,"both pin are not matched so plese try again")
                    pin()
                 
            pin()
        else:
            print("please enter valid option")
            atm()
       
    else:
        print("  "*5,"\nsorry! you enter wrong pin")
atm()