# Exercise 4: Train Ticket Calculator

name = input("Enter passenger name: ")
destination = input("Enter destination: ")
ticket_count = int(input("Enter number of tickets: "))
passenger_type = input("Enter passenger type (child/student/senior/adult): ")

# Fare table
if destination.lower() == "dhaka":
    fare = 500
elif destination.lower() == "chittagong":
    fare = 800
elif destination.lower() == "sylhet":
    fare = 700
else:
    print("Invalid destination")
    fare = 0

# Discount
if passenger_type.lower() == "child":
    discount = 50
elif passenger_type.lower() == "student":
    discount = 20
elif passenger_type.lower() == "senior":
    discount = 15
else:
    discount = 0

# Calculate fare
discount_amount = fare * discount / 100
final_fare = fare - discount_amount
total_fare = final_fare * ticket_count

# Print ticket
print("\n----- TRAIN TICKET -----")
print("Passenger Name:", name)
print("Destination:", destination)
print("Ticket Count:", ticket_count)
print("Passenger Type:", passenger_type)
print("Fare per Ticket:", fare)
print("Discount:", discount, "%")
print("Total Fare:", total_fare)
print("------------------------")