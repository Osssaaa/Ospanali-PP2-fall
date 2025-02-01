class Owner():
    def __init__(self, balance=0):
        self.balance = balance
    def show_balance(self):
        print(f"Balance: {self.balance}₸")
    def deposite(self):
        self.balance += int(input('sum of replenishment: '))
    def withdraw(self):
        sum_of_it = int(input('sum of withdraw: '))
        if sum_of_it < self.balance:
            self.balance -= sum_of_it
        else:
            print("You don't have that kind of money ")
            #print('unavailable sum of withdraw ')
student1 = Owner()
student1.show_balance()
student1.deposite()
student1.show_balance()
student1.withdraw()
student1.show_balance()