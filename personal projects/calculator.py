from sys import exit


def calculator():
    first_number = int(input("Please input first number: "))
    while first_number >= 0:
        operator_input = input("Please input operator: ")
        if operator_input == '*':
            second_number = int(input("Please input second number: "))
            if second_number >= 0:
                print(first_number * second_number)
                input("Do another calculation?")
                if input == 'y':
                    continue
                else:
                    exit()
        elif operator_input == '/':
            second_number = int(input("Please input second number: "))
            if second_number >= 0:
                print(first_number / second_number)
                input("Do another calculation?")
                if input == 'y':
                    continue
                elif input == 'n':
                    exit()
        elif operator_input == '+':
            second_number = int(input("Please input second number: "))
            if second_number >= 0:
                print(first_number + second_number)
                input("Do another calculation?")
                if input == 'y':
                    continue
                else:
                    exit()
        elif operator_input == '-':
            second_number = int(input("Please input second number: "))
            if second_number >= 0:
                print(first_number - second_number)
                input("Do another calculation?")
                if input == 'y':
                    continue
                else:
                    exit()
        else:
            exit()


calculator()
