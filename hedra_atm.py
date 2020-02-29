class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        # allowed papers: 100, 50, 10, 5, and cents
        print("Welcome to " , self.bank_name)
        print("Current balance = ", self.balance)
        result = self.balance
        
        if request > self.balance:
            print("Can't give you all this money !!")
            
        elif request < 0:
            print("More than zero plz!")
            
        else:
            while request > 0:
        
                if request >= 100:
                    request -= 100
                    print("give 100")
    
                elif request >= 50:
                    request -= 50
                    print("give 50")
        
                elif request >= 10:
                    request -= 10
                    print("give 10")
        
                elif request >= 5:
                    request -= 5
                    print("give 5")
    
                elif request < 5:
                  print("give " + str(request))
                  request = 0
            
            result = self.balance - request
                  
        return result

    
balance1 = 500
balance2 = 1000
balance3 = 2000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")
atm3 = ATM(balance3, "Hedra Bank")
# For example, if I withdraw the same amounts from each atms
# Then, print out the rest on each atm after all withdrawals
atms = [atm1, atm2, atm3]
req = [252, 2050, 97, 305 ]
for atm in atms:
    for r in req:
        atm.withdraw(r)
        if atm.balance > r:
            atm.balance -= r
    print("The rest of the balance", ":" , atm.balance)
    print("The end of this atm --------------- ")