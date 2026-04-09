class Bank:

    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
acc = Bank(100)

print(acc.get_balance())