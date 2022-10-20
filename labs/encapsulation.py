import random


class AccountError(Exception):
    pass

    # def __del__(self):
    #     if self.__number != 0:
    #         print("account can't get deleted please withdrawal all your money first")


class Account:

    def __init__(self, number):
        self.__balance = 0
        self.__number = number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise AccountError('invalid')

        if amount > 100_000:
            print("that's alot amount of money")

        print(f'your current balance is {self.balance}')
        self.__balance = amount

    def withdrawal(self, amount):
        Account.check_amount(amount)
        if self.balance < amount:
            raise AccountError("CAN'T CONTINUE THE OPERATION")
        self.balance -= amount
        print(f'your current balance is {self.balance}')

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, temp):
        raise AccountError("NOT ALLOWED")

    @number.deleter
    def number(self):
        if self.__number != 0:
            print("account can't get deleted please withdrawal all your money first")


x = Account()
'''
#test case 1
x = Account()

#test case 2
x = Account()

#test case 3
x= Account()
x.number = 1240

#test case 4
x = Account()
x.deposit(1000000)

#test case 5
x = Account()
del x

'''
