class address():
    def __init__(self, initRecipient, initCountry, initStreet, initCity, initState, initPostalCode):
        self.recipient = initRecipient
        self.city = initCity
        self.country = initCountry
        self.street = initStreet
        self.state = initState
        self.postalCode = initPostalCode

    def display(self):
        print(self.recipient)
        print(self.city)
        print(self.country)
        print(self.street)
        print(self.state)
        print(self.postalCode)

MyAddress = address("Bob", "Canada", "Boulevard 2", "Toronto", "Ontario", "J11 3h3")
MyAddress.display()

