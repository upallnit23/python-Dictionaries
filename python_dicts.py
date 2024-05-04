import copy
from copy import deepcopy

#Real World Python Dictionary Applications
#Task 1:Restaurant Menu Update

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

def add_category(menu, category):
    if category not in menu:
        menu[category] = []
        print(f"Category {category} added to menu." )
    else:
        print(f"Category {category} already in menu.")

def add_item(menu, category, item):
    if category in menu:
        if item not in menu:
            menu[category].append(item)
            print(f"Item {item} added to category {category}.")
        else:
            print(f"{item} already exists in {category}.")
    else:
        print(f"Category {category} does not exist.")
    
def update_item(menu, item, price):
    menu.update({item: price})
    print(f"Item {item} price updated to ${price}.")
    if item not in menu:
        print(f"Item {item} not found on menu.")

def rem_item(menu, category, item):
    if item in category:
        del menu[category][item]
        print(f"Item {item} removed from menu.")
    else:
        print(f"Item {item} was never in the menu.")

add_category(restaurant_menu, "Beverages")    
add_item(restaurant_menu, "Beverages", "Water")
add_item(restaurant_menu, "Beverages", "Iced tea")
update_item(restaurant_menu, "Steak", 17.99)
rem_item(restaurant_menu, "Starters", "Bruschetta")

#Advanced Data Handling with Python
#Task 2:Hotel Room Booking Tracker

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}
def is_available(hotel, roomnum):
    print(f"Getting room number {roomnum}.")
    return hotel.get(roomnum)

"""def customer_name():
    try:
        customer = input("Enter customer name: ")
        if customer.isalpha():
            return customer
    except ValueError as e:
        print(e)
    except Exception:
        print("Customer name invalid. ")"""

def book_room(hotel, roomnum, customer):
    if is_available(hotel, roomnum):
        print(f"Room number {roomnum} is booked for {customer}.")
        hotel_rooms
    else:
        print(f"Room number {roomnum} is not available.")

def check_out(hotel, roomnum, customer):
    print(f"Customer {customer} has checked out of room number {roomnum}.")
    if roomnum in hotel:
        hotel_rooms[roomnum]["status"] = "available"
        hotel_rooms[roomnum]["Customer"] = ""
        print(f"Room number {roomnum} is currently available.")
    else:
        print(f"Room number {roomnum} is not valid.")

def display_rooms(hotel):
    for key, value in hotel.items():
        print(f"Room {key} is at status {value}.")

book_room(hotel_rooms, 102, "Mina Lee")
check_out(hotel_rooms, 101, "")
display_rooms(hotel_rooms)

#Python Programming Challenges for Customer Service Data Handling
#Task 1:Customer Service Ticket Tracker

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(tickets, ticketnum):
    if ticketnum not in tickets:
        tickets[ticketnum] = []
        print(f"Ticket number {ticketnum} added to service tickets." )
    else:
        print(f"Ticket {ticketnum} already in service requests.")

def update_ticket(tickets, ticketnum, ti1, ti2, ti3):
    for ticketnum in tickets:
        tickets[ticketnum]["Customer"] = ti1
        tickets[ticketnum]["Issue"] = ti2
        tickets[ticketnum]["Status"] = ti3
    
def display_tickets(tickets, ticketnum):
    for ticketnum in tickets:
        for key, value in ticketnum.items():
            print(f"Ticket {key} is currently {value}.")

open_ticket(service_tickets, "Ticket001")
update_ticket(service_tickets, "Ticket003", "Millie Brown", "Hacked", "open")
#display_tickets(service_tickets)

#4. Python Essentials for Business Analytics
#Task 1:Sales Data Cloning and Modification

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

deep_weekly_sales = copy.deepcopy(weekly_sales)
print(deep_weekly_sales)

deep_weekly_sales["Week 2"]["Electronics"] = 18000
print(deep_weekly_sales)