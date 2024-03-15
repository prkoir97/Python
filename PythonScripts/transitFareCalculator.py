# A39
# Copenhagen Transit Fare Calculator


# Function to compute the fare based on the number of zones and ticket type
def computeFare(zone, ticketType):
    fare = 0

    # Compute the fare based on the given zone and ticket type
    if zone <= 2 and ticketType == "adult":
        fare = 23
    elif zone <= 2 and ticketType == "child":
        fare = 11.5
    elif zone == 3 and ticketType == "adult":
        fare = 34.5
    elif (zone == 3 or zone == 4) and ticketType == "child":
        fare = 23
    elif zone == 4 and ticketType == "adult":
        fare = 46
    else:
        fare = -1  # Return -1 if the input is invalid

    return fare


# Main function
def main():
    # Prompt the user to enter the number of zones and the ticket type
    z = int(input('Enter the number of zones: '))
    t = input('Enter the ticket type (adult/child): ').lower()

    # Compute the fare using the computeFare function
    fare = computeFare(z, t)

    # Print the calculated fare
    print('The fare is', fare)


# Entry point of the program
if __name__ == "__main__":
    main()
