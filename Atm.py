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