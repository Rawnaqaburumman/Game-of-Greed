class Banker:
   def __init__(self,balance=0,shelved=0)  :
     self.balance =balance
     self.shelved=shelved


   def shelf(self,input):
       self.shelved+=input
       return self.shelved


   def bank(self):
       deposited = self.shelved
       self.balance+=self.shelved
       self.shelved=0
       return deposited

   def clear_shelf(self):
       self.shelved=0









