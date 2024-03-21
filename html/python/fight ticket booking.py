class ticket:
    def __init__(self):
     self. pas="midhun"
    def booking(self):
       self.email=(input("Email: "))
       self.psw=(input("Password: "))
       while '@' not in self.email:
          print("invalid email")
          self.email=(input("Email: "))         
       if self.pas != self.psw:
          print("pasword incurect")
          self.psw=(input("Password: "))
       while True:
              if self.pas == self.psw:
                print("select your flight")
                print("1.Air india")
                print("2.Singapore Airline")
                print("3.Cancel")
                self.selt=int(input("Select your flight: "))
                if self.selt >=4:
                   print("invalid selection")
                   self.selt=int(input("Select your flight: "))
                elif self.selt ==1:
                   print("Air india facilitys")
                   print("1.Leaxuary(500.Rs)")
                   print("2.Generel(200.Rs)")
                   self.opt=int(input("Select your option: "))
                   if self.opt>=3:
                      print("invalid option")
                      self.opt=int(input("Select your option: "))
                   elif self.opt ==1:
                      self.amt=int(input("Pay Amount: "))
                      while self.amt!=500:
                         print("Pay curect Amount")
                         self.amt=int(input("Pay Amount: "))
                      else:
                         print("Paid Succusfuly")
                         print("Air india")
                         print("class: Leaxuary")
                         print(f"Paid Amount:{self.amt}.Rs")
                         print(f"Deatils: {self.email}")
                         print("Thankyou")
                   if self.opt==2:
                       self.amt=int(input("Pay Amount: "))
                       while self.amt!=200:
                         print("Pay curect Amount")
                         self.amt=int(input("Pay Amount: "))
                       else:
                         print("Paid Succusfuly")
                         print("Air india")
                         print("class: Generel")
                         print(f"Paid Amount:{self.amt}.Rs")
                         print(f"Deatils: {self.email}")
                         print("Thankyou")
               # next brand
              if self.selt ==2:
                   print("Singapor Airline facilitys")
                   print("1.Leaxuary(700.Rs)")
                   print("2.Generel(500.Rs)")
                   self.opt=int(input("Select your option: "))
                   if self.opt>=3:
                      print("invalid option")
                      self.opt=int(input("Select your option: "))
                   elif self.opt ==1:
                      self.amt=int(input("Pay Amount: "))
                      while self.amt!=700:
                         print("Pay curect Amount")
                         self.amt=int(input("Pay Amount: "))
                      else:
                         print("Paid Succusfuly")
                         print("Singapore Airline")
                         print("class: Leaxuary")
                         print(f"Paid Amount:{self.amt}.Rs")
                         print(f"Deatils: {self.email}")
                         print("Thankyou")
                   if self.opt==2:
                       self.amt=int(input("Pay Amount: "))
                       while self.amt!=500:
                         print("Pay curect Amount")
                         self.amt=int(input("Pay Amount: "))
                       else:
                         print("Paid Succusfuly")
                         print("Singapor Airline")
                         print("class: Generel")
                         print(f"Paid Amount:{self.amt}.Rs")
                         print(f"Deatils: {self.email}")
                         print("Thankyou")   
              elif self.selt == 3:
                break
              cun=(input("you wanna continue our service(yes/no)"))
              if cun == 'yes':
                continue
              else:
                break                                                      
car=ticket()
car.booking()
                                 