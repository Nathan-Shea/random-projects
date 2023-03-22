import math

while True:
    expression = input("Enter a math expression or 'q' to quit: ")
    if expression == 'q':
        break
    try:
        result = eval(expression)
        print("Result:", result)
    except:
        print("Invalid expression.")