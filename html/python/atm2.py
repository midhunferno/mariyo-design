print("ATM")
class bank():
    def __init__(self):
        self.name ="Midhun"
        self.balance = 2000
        self.pin = 2002
        
    def check(self):
       pin1 =int(input("enter your pin: "))
       while self.pin != pin1:
                print("invalid pin")
                pin1 =int(input("enter your pin again: "))

       if self.pin == pin1:
            #      print(f"select your choice Mr:{self.name} \
            #      1.Withdrow \
            #      2.Deposit \
            #      3.Balance \
            #      4.Cancel")
            #      choice=int(input("enter your need: "))

        while True:
         
         print(f"select your choice Mr:{self.name} \
                 1.Withdrow \
                 2.Deposit \
                 3.Balance \
                 4.Cancel")
         choice=int(input("enter your need: "))

         if choice == 1:
               amt=int(input("enter Rs:"))
               self.balance = self.balance - amt
               print(f"{amt}.Rs withdrowed")
               print(f"Curent balance :{self.balance}.Rs") 

         elif choice == 2:
                 dep=int(input("enter deposit amount: "))
                 self.balance = self.balance + dep
                 print(f"{dep}.Rs deposited")
                 print(f"Curent balance :{self.balance}.Rs") 

         elif choice == 3:
               print(f"Curent balance :{self.balance}.Rs")

         elif choice == 4:
               print("Tnx for using our service")
               break
         
         cun=(input("you wanna continue (yes/no)"))
         if cun== 'yes':
               continue  
         else:
               break  
                 
use = bank()
use.check()        
           