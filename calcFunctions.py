def add(no1, no2):
    result = no1 + no2
    return result

def subtract(no1, no2):
    result = no1 - no2
    return result

def multiply(no1, no2):
    result = no1 * no2
    return result

def divide(no1, no2):
    result = no1 / no2
    return result

def display(result):
    print("The result of this operation is " + str(result))
##str(result) is done because the sum of the function is an integer. When put in
##front of a string, It confused the terminal. So str in front changes the
## result into a string to be displayed in one sentence. 
