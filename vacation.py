# A function that takes the no. of days you book for vacation return total cost,
# with the coniditions being:
# 7 or more days you apply a discount of £50
# alternatively, 3 or more days you apply a discount of £20


def rental_car_cost(d):
    # your code
    totalCost = d * 40
    if d >= 7:
        totalCost -= 50
    elif d >= 3:
        totalCost -= 20
    print(totalCost)
    return totalCost
    


if __name__ == "__main__":
    d = int(input("Days Booked: "))
    rental_car_cost(d)