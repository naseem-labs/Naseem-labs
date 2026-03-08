# # # # # # # # for item in ["nasem" , "bajwa" , "brand" , "naseem labs"]:
# # # # # # # #     print(item)

# # # # # # # # for i in range(5):
# # # # # # # #     print(i)

# # # # # # # # for i in range (1,6):
# # # # # # # #     print (i)

# # # # # # # # for i in range (1, 11, 2):
# # # # # # # #     print(i)

# # # # # # # # for char in "naseem":
# # # # # # # #     print(char)

# # # # # # # # number = [ 2, 2 , 2 , 2 , 9 , 9 ]
# # # # # # # # for bb in number:
# # # # # # # #     output = ''
# # # # # # # #     for count in range (bb):
# # # # # # # #         output += 'X'
# # # # # # # #     print (output)
# # # # # # # for x in range (4):
# # # # # # #     for y in range (3):
# # # # # # #         print (f"({x}) ({y})")

# # # # # # name = ['naseem' , 'bajwa' , 'kabir' , 'nanak']
# # # # # # print (name[0:-1])
# # # # # # name[3] = "naseem bajwa"
# # # # # # print (name)
# # # # # # print(name[3])

# # # # # # print ("naseem" in name)


# # # # # # numbers = ['2' , '5' , '7' , '1' , '9']
# # # # # # max = numbers[0]
# # # # # # for number in numbers:
# # # # # #     if number > max:
# # # # # #         max = number
# # # # # # print (max)

# # # # # matrix = [
# # # # #     [1, 2, 3,],
# # # # #     [4, 5, 6,],
# # # # #     [7, 8, 9,]
# # # # # ]
# # # # # for row in matrix:
# # # # #     for item in row:
# # # # #          print(item)

# # # # number = [ 3, 7, 13, 55, 10, 13, 3]
# # # # number2 = number.copy()
# # # # number.insert(3,20)
# # # # number.remove(13)
# # # # print (number)
# # # # print (number2)

# # # number = (1, 3, 5, )
# # # x, y, z, = number
# # # print (x)

# # customer = {
# #     "name": "naseem bajwa",
# #     "age" : "27",
# #     "is_verified": True
# # }
# # customer ["name"] = "bajwa saab"
# # customer ["pind"] = "ina bajwa"
# # print( customer.get("birthday", "13 oct. 1999") )
# # print (customer["pind"])

# phone = input ("phone: ")
# mapping  = {
#     "1": "one",
#     "2": "two" ,
#     "3": "three"
# }
# output = ""
# for ch in phone:
#    output += mapping.get(ch, "!") + " "
# print (output)
def emoji_converter(message):
    emojis = {
        ":)": "😊",
        ":(": "😞",
        ":D": "😀",
        ";)": "😉"
    }
    words = message.split(" ")
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("> ")
print(emoji_converter(message))