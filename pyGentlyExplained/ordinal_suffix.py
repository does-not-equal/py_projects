def ordinal_suffix(number):
    number_str = str(number)
    
    if number_str[-2:] in ('11', '12', '13'):
        return number_str + 'th'
    if number_str[-1:] == '1':
        return number_str + 'st'
    if number_str[-1:] == '2':
        return number_str + 'nd'
    if number_str[-1:] == '3':
        return number_str + 'rd'
    return number_str + 'th'
        


assert ordinal_suffix(0) == '0th'
assert ordinal_suffix(1) == '1st'
assert ordinal_suffix(2) == '2nd'
assert ordinal_suffix(3) == '3rd'
assert ordinal_suffix(4) == '4th'
assert ordinal_suffix(10) == '10th'
assert ordinal_suffix(11) == '11th'
assert ordinal_suffix(12) == '12th'
assert ordinal_suffix(13) == '13th'
assert ordinal_suffix(14) == '14th'
assert ordinal_suffix(101) == '101st'