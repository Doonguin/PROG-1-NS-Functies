# Calculate standard price for the current travel
def standaardprijs(distance):
    # If the number given is less than 0 than default to 0
    if distance < 0:
        distance = 0
    
    # Check if the distance is equal to or more than 50km and calculate accordingly
    if distance >= 50:
        price = 15 + ((distance - 50) * 0.60)
    else:
        price = distance * 0.80

    # Return the calculated price of the travel
    return price

# !TESTS!
print(standaardprijs(int(input("Travel Distance: "))))