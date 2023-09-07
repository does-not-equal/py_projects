def calculate_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def calculate_product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

# verify with assert statements
assert calculate_sum([]) == 0
assert calculate_sum([2, 4, 6, 8, 10]) == 30
assert calculate_product([]) == 1
assert calculate_product([2, 4, 6, 8, 10]) == 3840