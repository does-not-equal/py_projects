# does not work, code checked
def get_square_colour(column, row):
    if column < 1 or column > 8 or row < 1 or row > 8:
        return ''
    if column % 2 == row % 2:
        return 'white'
    else:
        return 'black'
    
# Assertion Statements 
assert get_square_colour(0, 0) == 'white'
assert get_square_colour(1, 0) == 'black'
assert get_square_colour(0, 1) == 'black'
assert get_square_colour(7, 7) == 'white'
assert get_square_colour(0, 8) == ''
assert get_square_colour(2, 9) == ''

