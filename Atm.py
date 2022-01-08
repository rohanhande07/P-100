class Atm(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    def cashWithdrawal(self):
        print("Cash has been withdrawn")
    def balanceEnquiry(self):
        print("Your balance will be checked")
    def forgottenDetails(self):
        print("Please contact your bank to recieve your details")

Lloyds = Atm("1346", "876")
Lloyds.cardNumber

def main():
    Card_number = input("insert your card number:- ")
    pin_number  = input("enter your pin number:- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()