# Authors: Andrew Apple, Nirmita Mehra

# ---------------------------------------------
def speedingTicket(mph, limit):
    print("-"*10)
    ticket = 0
    if isinstance(mph, int) and isinstance(limit, int):
        print("Speed: " + str(mph))
        print("Speed Limit: " + str(limit))

        if mph < limit - 10:
            print("Ticket - Under Speed Limit - $50.00")
            ticket = 50
        elif limit + 20 >= mph >= limit + 6:
            print("Ticket - Over Speed Limit - $75.00")
            ticket = 75
        elif limit + 40 >= mph > limit + 20:
            print("Ticket - Over Speed Limit - $150.00")
            ticket = 150
        elif mph > limit + 40:
            print("Ticket - Over Speed Limit - $300.00 - Whats wrong with you? Are you okay?")
            ticket = 300
        else :
            print("No Ticket!")

        return ticket
    else:
        print("Wrong Data Type!")
        print("MPH Data Type: " + str(type(mph)))
        print("Limit Data Type: " + str(type(limit)))

    print("")

# speedingTicket(26, 35)
# speedingTicket(200, 30)
# speedingTicket("200", 30)
# speedingTicket(200, "30")
# speedingTicket("200", "30")
# speedingTicket("",0)
# speedingTicket(None,None)

# ---------------------------------------------
# if avg temp < 60: then heating day
# if avg temp > 80: then cooling day
# end input when temp entered is < -459

def heatingCoolingDays():
    temp = int(input("Enter the average daily temperature:"))
    heating = 0
    cooling = 0
    while temp >= -459:
        if temp < 60:
            heating = heating + 1
        if temp > 80:
            cooling = cooling + 1
        temp = int(input("Enter the average daily temperature:"))

    print("Heating days: ", heating)
    print("Cooling days: ", cooling)

heatingCoolingDays()

# ---------------------------------------------
def countchars(st):
    count = 0
    for c in st:
        if c == " " or c == "." or c == "!" or c == ",":
            continue
        count +=1
    return count

countchars("Listen, Mr. Jones, calm down.")

# ---------------------------------------------
def maxProfit(prices):
    min, max, profit = 0, 0, 0
    min_i, max_i = 0, 0

    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]

    return profit

# print(maxProfit([7,1,5,3,6,4]))
# print(maxProfit([7,6,4,3,1]))
# print(maxProfit([7,1]))
# print(maxProfit([]))
# print(maxProfit([7,7,7,7,7]))