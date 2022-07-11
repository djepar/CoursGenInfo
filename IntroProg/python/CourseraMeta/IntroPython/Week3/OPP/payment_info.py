

class Payslip:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"
        
robert = Payslip("Robert", "no", "1000")

robert2 = Payslip("Robert", "yes", "9000")
print(robert.status())
print(robert2.status())