# fizz buzz program

def fizz_buzz(up_to):
    for number in range(1, up_to + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz",end='')
        elif number % 3 == 0:
            print("Fizz",end='')
        elif number % 5 == 0:
            print("Buzz",end='')
        else:
            print(number, end='')
            
fizz_buzz(35)