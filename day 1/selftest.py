# 1. Apna full naam variable mein store kar te print kar
name = "naseem bajwa"
print(name)

# 2. Number 42 da type print kar
number = 42
print(type(number))

# 3. String "100" nu int mein convert kar te 50 add kar

number = "100"
print(int(number))

number = int("100")
print(number)
# 4. Apna naam ALL CAPS mein print kar using method
name = "naseem bajwa"
print(name.upper())

# 5. "PYTHON" de pehle 3 characters print kar
word = "Python"
print (word[0:3])

# 6. 2 ki power 10 calculate kar (** use kar)
a = 2
b = 10
c = a ** b
print(c)
# 7. User ton naam puchh te f-string naal greet kar
name = input ("what is your name? ")
print (f"welcome to my world {name}")

# 8. Do numbers bana te check kar pehla vadda ae ya dooja
num1 = int(input("enter your first number: "))
num2 = int (input("enter your second number: "))
if num1>num2:
    print("First number is bigger")
else:
    print("second number is bigger")