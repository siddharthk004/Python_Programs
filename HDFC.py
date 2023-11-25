
class HDFC:
    ROI = 9.5
    
    def __init__(self,name,amount):
        self.balance = amount
        self.AccountHolder = name 
        print("welcome : ",self.AccountHolder)
        print("account gets succesfully created with initial balance: ",self.balance)
    
    def displaybalance(self):
        print("hello",self.AccountHolder)
        print("your account balance is : ",self.balance)
        
    @classmethod    
    def displaybankinfo(cls):
        print("Welcome to hdfc bank portal")
        print("our bank is private limited bank")
        print("We provide rate of interest on saving account is : ",cls.ROI)

    @staticmethod
    def displayKYCinfo():
        print("according to the rules of RBI you should provide given KYU documents")
        print("your adhaar card")
        print("your pan card")
        print("your passport size photo")
    
    def windraw(self,amount):
        if self.balance < amount:
            print("theere is no sufficient balnace")
        else:
            self.balance = self.balance - amount
            print("amount withdrall successfullly...")
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("amount deposiit succesfully...")
            
def main():    
    
    print("ROI of hdfc bank is : ",HDFC.ROI)
    
    HDFC.displaybankinfo()
    HDFC.displayKYCinfo()
    
    print()
    print("creating new account...")
    siddharth = HDFC("siddharth",5000)
    
    print("craeting new account...")
    dnyaneshwari = HDFC("dnyaneshwari",3000)
    
    print("performing operations on obj1")
    siddharth.deposit(2000)
    siddharth.displaybalance()
    
    siddharth.windraw(1000)
    siddharth.displaybalance()
    print("Performing operations on dnyaneshwari's account")
    
    dnyaneshwari.deposit(4000)
    dnyaneshwari.displaybalance()
    
    dnyaneshwari.windraw(500)
    dnyaneshwari.displaybalance()
    
if __name__ == "__main__":
    main()