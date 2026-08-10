seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]

# Display all seats
print("--- Bus Seat Status ---")

for i in range(len(seats)):
    print("Seat", i + 1, ":", seats[i])

# Ask user for seat number
seat_number = int(input("\nEnter seat number: "))

# Check seat availability
if seats[seat_number - 1] == "Available":
    seats[seat_number - 1] = "Booked"
    print("Seat booked successfully.")
else:
    print("Seat is already booked.")

# Count booked and available seats
booked_seats = 0
available_seats = 0

for seat in seats:
    if seat == "Booked":
        booked_seats += 1
    else:
        available_seats += 1

# Display final summary
print("\n--- Seat Summary ---")
print("Total Seats:", len(seats))
print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)