# Movie Ticket Booking System - Version 1.0
# Feature: book and cancel tickets
def book_ticket(movie_id, customer_id):
    print("Ticket for movie", movie_id, "booked by customer", customer_id)

def cancel_ticket(movie_id):
    print("Ticket for movie", movie_id, "cancelled")

# Movie Ticket Booking System - Version 1.1
# Features: book and cancel tickets, price calculation

def book_ticket(movie_id, customer_id):
    print("Ticket for movie", movie_id, "booked by customer", customer_id)

def cancel_ticket(movie_id):
    print("Ticket for movie", movie_id, "cancelled")

def calculate_price(seats, rate=150):
    price = seats * rate
    print("Total Price = Rs.", price)
    return price
