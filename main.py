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

def ritprijs(age, weekend, distance):
    standardPrice = standaardprijs(distance)

    if age >= 12 and age < 65:
        if weekend:
            return standardPrice * 0.6

        return standardPrice
    else:
        if weekend:
            return standardPrice * 0.65
        else:
            return standardPrice * 0.7


# !TESTS!
print(ritprijs(int(input("Age: ")), bool(input("Weekend: ")), int(input("Distance: "))))