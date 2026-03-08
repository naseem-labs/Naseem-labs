# # # # # # # Multiplication table
# # # # # # # num = int(input(" i need table of : "))
# # # # # # # for i in range (1, 11):
# # # # # # #     print (f"{num} x {i} = {num * i}")

# # # # # #     # sum of numbers
# # # # # # total = 0
# # # # # # for i in range(1, 101):
# # # # # #     total += i
# # # # # # print (f"sum of 1-100 = {total}")

# # # # # # # FizzBuzz — classic coding challenge
# # # # # # for i in range (1, 51):
# # # # # #     if i % 3 == 0 and i % 5 == 0:
# # # # # #         print("Fizzbuzz")
# # # # # #     elif i % 3 == 0:
# # # # # #         print ("Fizz")
# # # # # #     elif i % 5 == 0:
# # # # # #         print ("Buzz")
# # # # # #     else:
# # # # # #         print (i)

# # # # # # Build a to-do list
# # # # # todos = []
# # # # # todos.append("learn python")
# # # # # todos.append("Build project")
# # # # # todos.append("push to github")
# # # # # todos.append("post on instagram")
# # # # # todos.insert(0, "watch mosh video")
# # # # # print ("my day 2 to do list")
# # # # # for i, task in enumerate(todos, 1):
# # # # #     print(f"{i}. {task}")

# # # # # Find max and min

# # # # scores = [85, 92, 78, 95, 88, 73, 91]
# # # # print (f"highest: {max(scores)}")
# # # # print (f"lowest: {min(scores)}")
# # # # print (f"avarage: {sum(scores) / len(scores):.1f}")

# # # # # # List comprehension (bonus — advanced trick)
# # # # doubled = [x * 2 for x in scores]
# # # # print (f"doubled: {doubled}")

# # # # number = .21
# # # # print(type(number))

# # # # count = 1
# # # # while count <= 20 :
# # # #     print (count)
# # # #     # count += 3
# # # #     break
# # # #     # count += 

# # # # cmd = ""
# # # # while True:
# # # #     cmd = input("han vi kaka bol ")
# # # #     if cmd == "quit":
# # # #         break
# # # #     else:
# # # #         print("quit likhde chup karke pakai na mar")

# # # # for char in "Naseem" :
# # # #     print(char)

# # # # for x in range(25):
# # # #     for y in range(2):
# # # #       print(f"({x} ({y}))")

# # # # naseem labs profile
# # profile = {
# #     "name": "naseem bajwa",
# #     "brand": "naseem labs",
# #     "age": 27 ,
# #     "day": 2 ,
# #     "total_days": 106 ,
# #     "skill": ["python", "variables", "data type"],
# #     "project": 3,
# #     "is_filmmaker": True
# # }
# # for key,  value in profile.items():
# #     print(f"{key}: {value}")

# # # Update progress
# # profile["day"] = 2
# # profile["skill"].append(" main nahi dasda")
# # profile["project"] += 3
# # pct = (profile["day"] / profile["total_days"]) * 100

# # print (f"\n Progress: day {profile["day"]} / {profile["total_days"]} = {pct:.1f}%")
# # print (f"skills: {','.join(profile['skill'])}")
# # print (f"projects: {profile['project']}")

# sentence = "python is great, python is fun and python is easy"
# words = sentence.split()
# freq = {}
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
# print (freq)

