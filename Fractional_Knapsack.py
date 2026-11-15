# Fractional Knapsack Problem Using Greedy Method in Python

def fractional_knapsack():

    n = int(input("Enter number of items: "))

    weight = []
    profit = []

    for i in range(n):
        w = float(input("Enter weight: "))
        p = float(input("Enter profit: "))

        weight.append(w)
        profit.append(p)

    capacity = float(input("Enter capacity: "))
    total = 0

    # Calculate profit/weight ratio
    ratio = []

    for i in range(n):
        ratio.append(profit[i] / weight[i])

    # Sort items according to ratio
    for i in range(n): # The outer loop selects an item.
        for j in range(i + 1, n): # The inner loop compares it with the remaining items.
            if ratio[i] < ratio[j]:
                ratio[i], ratio[j] = ratio[j], ratio[i]
                weight[i], weight[j] = weight[j], weight[i]
                profit[i], profit[j] = profit[j], profit[i]

    # Select items
    for i in range(n): # Checks each item one by one.

        if capacity == 0: # If capacity becomes zero, break stops the loop.
            break

        if weight[i] <= capacity: # Checks whether the complete item fits inside the bag.
            total = total + profit[i] # If it fits, its full profit is added to total.
            capacity = capacity - weight[i] # Its weight is subtracted from the remaining capacity.

        else:
            
            total = total + profit[i] * capacity / weight[i]
            capacity = 0

    print("Maximum Profit =", total)
 

fractional_knapsack()