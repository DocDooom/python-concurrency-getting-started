import threading
import time


class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        balance = self.balance
        # time.sleep(1)
        self.balance = balance - amount

    def deposit(self, amount):
        balance = self.balance
        time.sleep(1)
        self.balance = balance + amount


b = BankAccount()
t1 = threading.Thread(target=b.deposit, args=(100,))
t2 = threading.Thread(target=b.withdraw, args=(50,))
t1.start()
t2.start()

print(b.balance)
