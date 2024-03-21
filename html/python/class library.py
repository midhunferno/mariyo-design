class lib:
    def __init__(self):
        self. name=(input("enter your name: "))
        self. email=(input("enter your email: ")) 
            
        self.spot={
           "book1":"Football",
           "book2":"Boxing",
        }
        self.socl={
            "book1":"History",
            "book2":"KGF",
        }
    def chek(self):
        while '@' not in self.email:
            print("type curect email")
            self. email=(input("enter your email: "))
        # else:
            # print("select option")
            # print("1.spots")
            # print("2.science")
            # print("3.cancel")
            # chois=int(input("select your option: "))
        while True:
          print("select option")
          print("1.spots")
          print("2.science")
          print("3.cancel")
          self.chois=int(input("select your option: ")) 
          if self.chois >4:
                print("invalid selection")
                self.chois=int(input("select your option: "))   
          elif self.chois == 1:
                print("1.football(300.Rs)")
                print("2.Boxing(200.Rs)")              
                self.selt=int(input("select book: "))
                if self.selt >3:
                  print("invalid") 
                  self.selt=int(input("select book: "))
                elif self.selt == 1:
                  self.amt=int(input("Amount: "))

                  while self.amt != 300:
                    print("pay curect amount")
                    self.amt=int(input("Amount: "))
                  else:
                   print("paid succesfuly")
                   print(f"Name: {self.name}")
                   print(f"Email: {self.email}")
                   print(f"BOOK: "+self.spot["book1"])
                   print(f"paid amount: {self.amt}")
                 
          
          
                if self.selt == 2:
                  self.amt=int(input("Amount: "))
               
                  while self.amt != 200:
                   print("pay curect amount")
                   self.amt=int(input("Amount: "))
                  else:
                   print("paid succesfuly")
                   print(f"Name: {self.name}")
                   print(f"Email: {self.email}")
                   print(f"BOOK: "+self.spot["book2"])
                   print(f"paid amount: {self.amt}")
                   
                #  jhhhd
          if self.chois == 2:
                print("1.History(500.Rs)")
                print("2.KGF(400.Rs)")              
                self.selt=int(input("select book: "))
                if self.selt >3:
                  print("invalid selection") 
                  self.selt=int(input("select book: "))
                elif self.selt == 1:
                  self.amt=int(input("Amount: "))
                  while self.amt != 500:
                   print("pay curect amount")
                   self.amt=int(input("Amount: "))
                  else:
                   print("paid succesfuly")
                   print(f"Name: {self.name}")
                   print(f"Email: {self.email}")
                   print(f"BOOK: "+self.socl["book1"])
                   print(f"paid amount: {self.amt}")
                
                if self.selt == 2:
                  self.amt=int(input("Amount: "))
                  while self.amt != 400:
                   print("pay curect amount")
                   self.amt=int(input("Amount: "))
                  else:
                   print("paid succesfuly")
                   print(f"Name: {self.name}")
                   print(f"Email: {self.email}")
                   print(f"BOOK: "+self.socl["book2"])
                   print(f"paid amount: {self.amt}")
                
          elif self.chois == 3:
                break
          cun=(input("you wanna continue our service(yes/no)"))
          if cun == 'yes':
                continue
          else:
                break         


use = lib()
use.chek()