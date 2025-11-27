import pandas as pd

# Sample flight data with added fields: Flight Time, Date, Class
flights_data = {
    'Flight Number': ['AI101', 'AI102', 'AI103', 'AI104', 'AI105'],
    'Source': ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore'],
    'Destination': ['London', 'New York', 'Dubai', 'Singapore', 'Paris'],
    'Flight Time': ['10:00', '14:00', '08:00', '12:00', '16:00'],
    'Date': ['2024-10-10', '2024-10-12', '2024-10-14', '2024-10-16', '2024-10-18'],
    'Total Economy Seats': [100, 120, 150, 110, 90],
    'Available Economy Seats': [100, 120, 150, 110, 90],
    'Total Business Seats': [20, 30, 20, 15, 10],
    'Available Business Seats': [20, 30, 20, 15, 10],
    'Passenger Name': [[] for _ in range(5)]  # List of passenger names for each flight
}

# Convert the data into a pandas DataFrame
flights_df = pd.DataFrame(flights_data)

# Function to display all flights
def display_flights():
    print("Available Flights:")
    print(flights_df[['Flight Number', 'Source', 'Destination', 'Flight Time', 'Date', 'Available Economy Seats', 'Available Business Seats']])

# Function to search flights by source location
def search_by_source(source):
    available_flights = flights_df[flights_df['Source'].str.lower() == source.lower()]
    if available_flights.empty:
        print(f"No flights found from {source}.")
    else:
        print(f"Flights from {source}:")
        print(available_flights[['Flight Number', 'Destination', 'Flight Time', 'Date', 'Available Economy Seats', 'Available Business Seats']])

# Function to check flight availability based on class (Economy or Business)
def check_flight_availability(flight_number, flight_class):
    flight = flights_df.loc[flights_df['Flight Number'] == flight_number]
    if flight.empty:
        print(f"Flight {flight_number} does not exist.")
    else:
        if flight_class.lower() == 'economy':
            if flight['Available Economy Seats'].values[0] > 0:
                print(f"Flight {flight_number} has {flight['Available Economy Seats'].values[0]} economy seats available.")
            else:
                print(f"Economy class on flight {flight_number} is fully booked.")
        elif flight_class.lower() == 'business':
            if flight['Available Business Seats'].values[0] > 0:
                print(f"Flight {flight_number} has {flight['Available Business Seats'].values[0]} business seats available.")
            else:
                print(f"Business class on flight {flight_number} is fully booked.")
        else:
            print("Invalid class. Please choose either 'Economy' or 'Business'.")

# Function to book a seat based on class
def book_seat(flight_number, passenger_name, flight_class):
    flight = flights_df.loc[flights_df['Flight Number'] == flight_number]
    if flight.empty:
        print(f"Flight {flight_number} does not exist.")
    else:
        index = flights_df.index[flights_df['Flight Number'] == flight_number].tolist()[0]
        if flight_class.lower() == 'economy':
            if flights_df.at[index, 'Available Economy Seats'] > 0:
                flights_df.at[index, 'Passenger Name'].append(f"{passenger_name} (Economy)")
                flights_df.at[index, 'Available Economy Seats'] -= 1
                print(f"Economy seat successfully booked for {passenger_name} on flight {flight_number}.")
            else:
                print(f"No available economy seats on flight {flight_number}.")
        elif flight_class.lower() == 'business':
            if flights_df.at[index, 'Available Business Seats'] > 0:
                flights_df.at[index, 'Passenger Name'].append(f"{passenger_name} (Business)")
                flights_df.at[index, 'Available Business Seats'] -= 1
                print(f"Business seat successfully booked for {passenger_name} on flight {flight_number}.")
            else:
                print(f"No available business seats on flight {flight_number}.")
        else:
            print("Invalid class. Please choose either 'Economy' or 'Business'.")

# Function to cancel a reservation
def cancel_reservation(flight_number, passenger_name):
    flight = flights_df.loc[flights_df['Flight Number'] == flight_number]
    if flight.empty:
        print(f"Flight {flight_number} does not exist.")
    else:
        index = flights_df.index[flights_df['Flight Number'] == flight_number].tolist()[0]
        if passenger_name in flights_df.at[index, 'Passenger Name']:
            flights_df.at[index, 'Passenger Name'].remove(passenger_name)
            if 'Economy' in passenger_name:
                flights_df.at[index, 'Available Economy Seats'] += 1
            elif 'Business' in passenger_name:
                flights_df.at[index, 'Available Business Seats'] += 1
            print(f"Reservation for {passenger_name} on flight {flight_number} has been cancelled.")
        else:
            print(f"No booking found for {passenger_name} on flight {flight_number}.")

# Main program
def flight_reservation_system():
    while True:
        print("\nFlight Reservation System")
        print("1. Display All Flights")
        print("2. Search Flights by Source")
        print("3. Check Flight Availability")
        print("4. Book a Seat")
        print("5. Cancel a Reservation")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            display_flights()
        elif choice == 2:
            source = input("Enter source city: ")
            search_by_source(source)
        elif choice == 3:
            flight_number = input("Enter flight number to check availability: ")
            flight_class = input("Enter class (Economy/Business): ")
            check_flight_availability(flight_number, flight_class)
        elif choice == 4:
            flight_number = input("Enter flight number to book: ")
            passenger_name = input("Enter passenger name: ")
            flight_class = input("Enter class (Economy/Business): ")
            book_seat(flight_number, passenger_name, flight_class)
        elif choice == 5:
            flight_number = input("Enter flight number to cancel: ")
            passenger_name = input("Enter passenger name: ")
            cancel_reservation(flight_number, passenger_name)
        elif choice == 6:
            print("Exiting Flight Reservation System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the flight reservation system
flight_reservation_system()
