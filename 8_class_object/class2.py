

# class Bank:
#     bank_name = "SBI"

#     def __init__(self,name,acc_num):
#         self.account_name=name
#         self.account_number=acc_num
#         self.balance=0

#     def deposit(self,amount):
#         if amount>0:
#             self.balance=self.balance+amount
#             print('current balance is',self.balance)

#     def withdraw(self,amount):
#         if amount>0:
#             if self.balance>amount:
#                 self.balance=self.balance-amount
#                 print('current balance is',self.balance)



# b1=Bank('sam',101)
# print(b1.balance)
# b1.deposit(1000)
# Bank.deposit(b1,1000)
# print(b1.balance)


# b2=Bank('sunil',561)
# b2.deposit(10000)
# Bank.deposit(b2,10000)



class Broker:
    stock_prices={'tsla':500,'goog':900,'amzn':680}

    def __init__(self,name,money):
        self.name=name
        self.wallet=money
        self.portfolio={}
    
    def display_porfolio(self):
        if not self.portfolio:
            for i,j in self.portfolio.items():
                print(i,j)
    
    def buy(self,stock_name):
        pass

    def sell(self,stock_name):
        pass

trader1=Broker('sanjay',10_000)
trader1.buy('tsla')
trader1.buy('amzn')
trader1.portfolio()
