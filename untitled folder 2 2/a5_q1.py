"""
CISC-121
Name:   Marcela Rojas
Student Number: 20365657
Email:  22mr6@queensu.ca
Date: 2023-03-30
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
from hotel_classes import *

#Create all the rooms
for i in range(1, 20):
    globals()[f"Suite{i}"] = Suite(i)
for i in range(1, 90):
    globals()[f"StandardRoom{i}"] = StandardRoom(i)
for i in range(1, 14):
    globals()[f"TaylorSuite{i}"] = TaylorSuite(i)

# get number of guests
print("Welcome to Marcela's hotel!")
num_guests = int(input("How many guests are checking in? "))

#Check in
for i in range(1, num_guests + 1):
    name = input("\nEnter your name: ")
    valid_room = False

    #room number and type until a valid one is entered
    while not valid_room:
        room_num = int(input("Enter your room number: "))
        room_type = input("Enter your room type ('Suite', 'StandardRoom', 'TaylorSuite'): ")
        if room_type == "Suite":
            valid_room = Suite(room_num).availability
        elif room_type == "StandardRoom":
            valid_room = StandardRoom(room_num).availability
        elif room_type == "TaylorSuite":
            valid_room = TaylorSuite(room_num).availability
        else:
            print("Invalid room type. Please try again.")
    #guest object
    globals()[f"guest{i}"] = Guest(name, room_num, room_type)
    guest = globals()[f"guest{i}"]

    room = globals()[f"{room_type}{room_num}"]
    room.checkIn(guest)
    #availability
    available_date = room.available_date
    print(f"{room_type} {room_num} will be available for check-in on day {available_date}.")

    # number of services then add sevices to bill
    num_services = int(input("How many services are you getting? "))
    for j in range(num_services):
        service_name = input("What service is it: ")
        service_cost = int(input("cost of service: $"))
        guest.addService(service_name, service_cost)
    print(f"\nThank you for staying with us, {name}!")
    guest.sendBill()
