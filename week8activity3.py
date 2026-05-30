# Parent Class
class Flight:

    def __init__(self, flight_number, destination):
        self.flight_number = flight_number
        self.destination = destination

    def show_flight(self):
        print("Flight Number:", self.flight_number)
        print("Destination:", self.destination)


# Child Class (inherits from Flight)
class DomesticFlight(Flight):

    def __init__(self, flight_number, destination, baggage_allowance):
        # Inherit attributes from Flight
        super().__init__(flight_number, destination)

        # Domestic flight specific attribute
        self.baggage_allowance = baggage_allowance

    def show_baggage(self):
        print("Baggage Allowance:", self.baggage_allowance, "kg")


# Create object of DomesticFlight
flight1 = DomesticFlight("NZ101", "Wellington", 23)

# Inherited method from Flight
flight1.show_flight()

# Method from DomesticFlight
flight1.show_baggage()