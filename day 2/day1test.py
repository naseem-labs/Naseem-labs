
# Q1: Apna naam, age, te brand name 3 variables mein store kar.
#     Fer ik f-string naal teeno ik line mein print kar.
print()
print(" answer 1 ")
print()
name ="naseem"
age = 25
brand = "naseem labs"
print(f"{name}  {age}  {brand}")

# Q2: "naseem labs" nu ALL CAPS mein print kar using method.
print()
print(" answer 2 ") 
print()
print(brand.upper())

# Q3: String "FILMMAKER" da last character print kar
#     using negative index.
print()
print(" answer 3 ") 
print()
work = "FILMMAKER"
print (work[-1])
# Q4: User ton ik number input le. 
#     Uss number da square (power of 2) print kar.
#     HINT: input() string denda ae — convert kari.
print()
print(" answer 4 ") 
print()
number = int (input ("enter your number "))
result = number ** 2
print (result)

# Q5: 17 nu 5 naal divide kar te sirf REMAINDER print kar.
#     Kahra operator ae?
print()
print(" answer 5 ") 
print()
 
reminder = 17 % 5
print (reminder)
# Q6: Ik variable bana x = 50.
#     Check kar: agar x 40 ton vadda ae TE 100 ton chhota ae
#     te print kar "Sahi range mein ae".
#     (HINT: and use kar)
print()
print(" answer 6 ") 
print()
x = 50
if x > 40 and x < 100:
    print ("its in the right range")
else:
    print ("not defined")
# Q7: User ton temperature input le.
#     Agar 35 ton vadda ae: print "Garmi ae!"
#     Agar 15 ton chhota ae: print "Thand ae!"
#     Otherwise: print "Mast mausam!"
print()
print(" answer 7 ") 
print()
tempreture = int(input("enter the tempreture = "))
if tempreture > 35 :
    print ("its hot day ")
elif tempreture < 15:
    print ("its a cold day")
else:
    print("nice weather")


# Q8: Word "PYTHON" de pehle 3 characters print kar
#     using slicing.
print()
print(" answer 8 ") 
print()
word = "python"
print(word[0:3])
# Q9: Ik string le: "Hello World"
#     Iss mein "World" nu "Naseem" naal replace kar.
#     Fer result print kar.
print()
print(" answer 9 ") 
print()
text = "hello world"
print (text.replace("world","naseem"))

# Q10: User ton naam puchh.
#      Agar naam "Naseem" ae te print "Boss aa gaya!"
#      Otherwise print "Welcome [naam]!"
print()
print(" answer 10 ") 
print()
name = input ("enter your name: ")
if name == "naseem" :
    print ("boss aa gea!")
else:
    print(f"welcome {name}")