firstNumber = int(input("first number: "))
print("")
pemdas = input("PEMDAS: ")
print("")
secondNumber = int(input("second number: "))

if pemdas == "-":
    print("")
    print("The answer is :",firstNumber - secondNumber)
    print("")
elif pemdas == 'times' or pemdas == 'x' or pemdas == '*':
    print('')
    print("The answer is :",firstNumber * secondNumber)
    print('')
elif pemdas == 'divide' or pemdas == "/":
    print("")
    print("The answer is :",firstNumber / secondNumber)
    print("")
elif pemdas == "+" or pemdas == "add" or pemdas == "plus":
    print("")
    print("The answer is :",firstNumber + secondNumber)
    print("")
else:
    print("")
    print("ERROR try entering PEMDAS such as 'x' or '+' or '-' or '/'. " )
    print("")