def number_request():   
       
    while True:
        request = input("Please enter an integer: ")
        try:
            request_int = int(request)
            break
        except ValueError:
            print("This is not a integer. Please enter a valid integer.")                
    
    return request_int

def collatz():

    number = number_request()

    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)

    return number

collatz()