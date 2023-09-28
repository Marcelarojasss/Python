"""
CISC-121
Name:   Marcela Rojas
Student Number: 20365657
Email:  22mr6@queensu.ca
Date: 2023-03-30
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
# Create a hotel room class with different types of rooms
class HotelRoom:
    # Constructor initializes the room with room number, availability, cleaning days, and available date
    def __init__(self, roomNum):
        self.roomNum = roomNum
        self.availability = True
        self.cleaningDays = 0
        self.available_date = None

    # checks if guest is in room
    def checkIn(self, guest):
        # will set room as unavailable
        self.availability = False
        # will calculate availability date based on cleaning days and check out data
        self.availableDate = guest.checkOutDate + self.cleaningDays


class Suite(HotelRoom):
    def __init__(self, roomNum):
        HotelRoom.__init__(self, roomNum)
        self.cleaningDays = 1
        self.available_date = None

class StandardRoom(HotelRoom):
    def __init__(self, roomNum):
        HotelRoom.__init__(self, roomNum)
        # set cleaning days to 0
        self.cleaningDays = 0

class TaylorSuite(HotelRoom):
    def __init__(self, roomNum):
        # Call the parent constructor and set cleaning days to 2
        HotelRoom.__init__(self, roomNum)
        self.cleaningDays = 2

# Create a service class with a name and cost
class Service:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

#guest class with name, room number, check out date, services, and total bill
class Guest:
    def __init__(self, name, roomNum, roomType):
        self.roomType = roomType
        self.roomNum = roomNum
        self.name = name
        #Asks for check out date
        checkOutDate = int(input("When is your check out date? "))
        #services and total bill
        self.checkOutDate = checkOutDate
        self.services = []
        self.totalBill = 0

    #this can add a aservice at the end and will modify the final bill
    def addService(self, serviceName, serviceCost):
        # Service object with the service name and cost and add it to the list of services
        service = Service(serviceName, serviceCost)
        self.services.append(service)
        # Update the total bill
        self.totalBill += serviceCost

    # displays the guest's total bill
    def sendBill(self):
        print("Here is your total bill:")
        # Displays all the services from the services list
        for service in self.services:
            print(service.name)
        # total bill
        print("Total bill: $" + str(self.totalBill))