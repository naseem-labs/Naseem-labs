import random
print ("=== number guessing game===")
print ("i am thinking of a number between 1 to 100")
secret = random.randint(1, 100)
attempt = 0

while True:
    guess = int(input("Your guess: "))
    attempt += 1
    if guess < secret:
        print("to lower! try higher")
    elif guess > secret:
        print ("too higher, try little low")
    else:
        print(f"correct! number was {secret}")
        print(f"you got in {attempt} attempts")
        if attempt <= 5 :
            print ("amazing! you are genius")
        elif attempt <= 10:
            print ("its good ")
        else:
            print (" keep practicing")
        break