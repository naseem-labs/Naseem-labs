# ==============================================
# DAY 1 + DAY 2 FULL TEST
# Bina Google. Bina purana code dekhe.
# ==============================================


# Q1: Variable bana: name, age, brand
#     Ik f-string mein print kar:
#     "Main [naam] haan, [age] saal, [brand] da founder"

print()
print ("answer 1")
name ="naseem"
age = "27"
brand = "Naseem labs"
print (f"main {name} hann, {age} saal , {brand} da founder ")
# Q2: User ton ik word input le.
#     Oh word ULTA (reverse) karke print kar.
#     HINT: slicing naal hunda ae
# print()
# print ("answer 2 ")
# print ()
# word = input("enter the word: ")
# print(word[::-1])

# Q3: % operator use karke check kar:
#     User ton number le — agar EVEN ae te print "Even"
#     agar ODD ae te print "Odd"
#     HINT: even number nu 2 naal divide karo te remainder 0 hunda
# print()
# print ("answer 3 ")
# print ()

# number = int(input("Enter you number "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("odd")

# Q4: for loop naal 1 ton 10 tak SIRF ODD numbers print kar
#     Output: 1, 3, 5, 7, 9
#     HINT: range(start, stop, step)
print()
print ("answer 4 ")
print ()

for i in range(1, 10, 2):
    print(i)

# Q5: Ik list bana 5 fruits di.
#     .append() naal ik hor add kar
#     .sort() naal sort kar
#     for loop naal har fruit print kar number de naal:
#     "1. Apple"
#     "2. Banana" etc.



# Q6: Ik dictionary bana:
#     student = naam, age, city, marks (list of 3 numbers)
#     Student da average marks calculate kar te print kar

student = {
    "name": " "
}


# Q7: Function bana: is_even(number)
#     Agar even ae te return True
#     Agar odd ae te return False
#     Fer iss function nu 4 te 7 naal call kar te result print kar


# Q8: Function bana: calculate(a, b, operation="add")
#     operation "add" ae te a + b return kar
#     operation "sub" ae te a - b return kar
#     operation "mul" ae te a * b return kar
#     Default "add" ae — bina operation de call kare te add hove
a = int(input("enter you first number: "))
b = int(input("enter your secound number: "))

# Q9: try/except use kar:
#     User ton 2 numbers le te divide kar
#     Agar user "abc" jaisa kuj daale: "Number deo!" print kar
#     Agar dooja number 0 ae: "Zero naal divide nahi ho sakda!" print kar


# Q10: Nested loop naal eh pattern print kar:
#      *
#      **
#      ***
#      ****
#      *****


# Q11: Ik list mein 10 numbers pa: [45, 22, 88, 13, 67, 92, 5, 73, 38, 56]
#      Bina max() function use kare — APNE loop naal sabton vadda number labh


# Q12: While loop use kar:
#      User ton baar baar input le
#      Jdon "quit" likhe tab BAND hove
#      Har input ik list mein save kar
#      "quit" baad saari list print kar


# Q13: Class bana: BankAccount
#      __init__ mein: owner_name, balance (default 0)
#      Method: deposit(amount) — balance vadhaave
#      Method: withdraw(amount) — balance ghatave
#              (par agar balance ton zyada ae te "Paise nahi ne!" print kare)
#      Method: show() — naam te balance dikhaave
#      
#      Test kar: account bana, 5000 deposit, 2000 withdraw, show karo


# Q14: Ik function bana: count_vowels(text)
#      Jo text mein kitne vowels ne (a, e, i, o, u) count kare
#      return kare number
#      Test kar: count_vowels("Naseem Labs") — answer 3 auna chahida


# Q15: Dictionary use kar — word frequency counter:
#      sentence = "python is great and python is fun and python is easy"
#      Har word kitni vaari aaya — dictionary mein store kar
#      Output: {"python": 3, "is": 3, "great": 1, "and": 2, "fun": 1, "easy": 1}