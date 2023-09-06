def get_smallest(numbers):
    if len(numbers) == 0:
        return None
    
    smallest = numbers[0]
    
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

# verify with assert statements
assert get_smallest([1, 2, 3]) == 1
assert get_smallest([3, 2, 1]) == 1
assert get_smallest([28, 25, 42, 2, 28]) == 2
assert get_smallest([1]) == 1
assert get_smallest([]) == None