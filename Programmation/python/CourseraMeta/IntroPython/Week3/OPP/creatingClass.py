class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    def __init__(self, num_rooms, num_bathrooms):
        self.rooms = num_rooms
        self.bathrooms = num_bathrooms
    def cost_evaluation(self):
        rate = 500
        cost = rate * (self.rooms + self.bathrooms / 2)
        print("For a {} rooms and {} bathrooms, the price is {} $ by months.".format(self.rooms, self.bathrooms, cost))
        pass
        #Functionality to calculate the cost from the area of the house

myhouse = House(5, 2)
myhouse.cost_evaluation()