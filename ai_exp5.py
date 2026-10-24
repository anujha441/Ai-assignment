def hill_climbing(start):
    while True:
        current_value = -(start - 5) ** 2 + 25

        left = start - 1
        right = start + 1

        left_value = -(left - 5) ** 2 + 25
        right_value = -(right - 5) ** 2 + 25

        if left_value > current_value:
            start = left
        elif right_value > current_value:
            start = right
        else:
            break

    return start

result = hill_climbing(0)

print("Best Solution:", result)
print("Maximum Value:", -(result - 5) ** 2 + 25)