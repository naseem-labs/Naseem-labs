print("=== Naseem labs calculator ===")
num1 = float(input("First number: "))
num2 = float(input("second number: "))
op = input ("operation (+, -, /, *): ")

if op == "+":
    result = num1 + num2
elif op == "_":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "can not divide by zero"
else:
    result = "invalid operation"
print(f"{num1} {op} {num2} = {result}")
