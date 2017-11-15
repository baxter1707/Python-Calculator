import calcFunctions as calculator

#from calcFunctions import add, subtract, mult

no1 = float(raw_input("Please enter your first number. "))
calc = raw_input("Please choose 1 - Addittion, 2 - Subtraction, 3 - Multiplication 4 - Division. " )
no2 = float(raw_input("Please enter your second number. "))

if calc == "1":

    #calculator.display(calculator.add(no1,no2))

    result = calculator.add(no1, no2)
    calculator.display(result)

elif calc == "2":
    result = calculator.subtract(no1, no2)
    calculator.display(result)

elif calc == "3":
    result = calculator.multiply(no1, no2)
    calculator.display(result)

elif calc == "4":
    result = calculator.divide(no1, no2)
    calculator.display(result)

else:
    print("invalid input")
