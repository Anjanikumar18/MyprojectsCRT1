from abc import ABC, abstractmethod

class Ticket(ABC):
    @abstractmethod
    def book_ticket(self):
        pass

class MakeMyTrip(Ticket):
    def book_ticket(self, name, phone_no, email_id, journey_date):
        print(f"Thank you for booking with Make My Trip, {name}. Your journey date is {journey_date}.")

class IRCTC(Ticket):
    def book_ticket(self, name, phone_no, email_id, journey_date):
        trip_type = input("Is this a 1-way or round trip? Enter '1' for 1-way or '2' for round trip: ").strip()
        if trip_type == '2':
            return_date = input("Please enter your return date: ").strip()
            print(f"Thank you for choosing IRCTC, {name}. Your journey dates are from {journey_date} to {return_date}.")
        else:
            print(f"Thank you for choosing IRCTC, {name}. Your journey date is {journey_date}.")

class Indigo(Ticket):
    def book_ticket(self, name, phone_no, email_id, journey_date):
        mode_of_transport = input("Which mode of transport do you want to go in? (train/flight/bus): ").strip().lower()
        print(f"Thank you for choosing Indigo, {name}. Your chosen mode of transport is {mode_of_transport} and your journey date is {journey_date}.")

# Example usage
make_my_trip = MakeMyTrip()
make_my_trip.book_ticket("Alice", "1234567890", "alice@example.com", "2024-04-01")

irctc = IRCTC()
irctc.book_ticket("Bob", "0987654321", "bob@example.com", "2024-05-01")

indigo = Indigo()
indigo.book_ticket("Charlie", "1122334455", "charlie@example.com", "2024-06-01")
