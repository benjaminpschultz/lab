class Account:
    def __init__(self,name: str):
        '''
        Constructer to create initial state of Account object
        :param name: Name of the account holder
        '''
        self.__account_name = name
        self.__account_balance = 0.0
    def deposit(self,amount: float):
        '''
        Function to add money to account
        :param amount: Total amount of money to be added to the account
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
    def withdraw(self,amount: float):
        '''
        Function to take money out of account
        :param amount: Total amount of money to be taken out of the account
        '''
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    def get_balance(self):
        '''
        Function to retrieve the value of self.__account_balance
        '''
        return self.__account_balance
    def get_name(self):
        '''
        Function to retrieve the value of self.__account_name
        '''
        return self.__account_name