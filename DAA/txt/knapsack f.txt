def fractional_knapsack(values, weights, capacity):
    n = len(values)

    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i]))

    items.sort(reverse=True)

    total_value = 0

    for ratio, value, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            capacity = 0

    return total_value


# User input
n = int(input("Enter number of items: "))

values = []
weights = []

for i in range(n):
    value = int(input("Enter value: "))
    weight = int(input("Enter weight: "))

    values.append(value)
    weights.append(weight)

capacity = int(input("Enter knapsack capacity: "))

result = fractional_knapsack(values, weights, capacity)

print("Maximum value:", result)
