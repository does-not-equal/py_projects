# opens file in write mode
def write_to_file(file_name, text):
    with open(file_name, 'w') as file_obj:
        file_obj.write(text)

# opens file in append mode
def append_to_file(file_name, text):
    with open(file_name, 'a') as file_obj:
        file_obj.write(text)

def read_from_file(file_name):
    with open(file_name, 'r') as file_obj:
        return file_obj.read()


write_to_file('greet.txt', 'Hello!\n')
append_to_file('greet.txt', 'Goodbye!\n')
assert read_from_file('greet.txt') == 'Hello!\nGoodbye!\n'