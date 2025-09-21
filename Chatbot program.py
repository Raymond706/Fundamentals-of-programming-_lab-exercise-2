# Chat with me program

# Ask for the user's name
user_name = input("Hi there! What's your name? ")

# Greet them
print("Hey " + user_name + "! Nice to meet you.")

# Ask how they feel today
mood = input("How are you feeling today? (good/bad) ").lower()

# Respond based on their answer
if mood == "good":
    print("Cool! Glad you're feeling good.")
elif mood == "bad":
    print("Oh, that's too bad. Hope things get better soon.")
else:
    print("Thanks for telling me how you feel!")
