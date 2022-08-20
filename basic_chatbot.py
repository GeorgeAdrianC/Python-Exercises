import random


user_greetings_prompts = [
    "Hi!",
    "Hello!",
    "Alloha!"
]

user_info_prompts = [
    "What's your age? ",
    "How old are you? ",
    "Please tell me your age. "
]

user_shopping_list_prompts = [
    "What's on your shopping list? ",
    "What would you like to buy? ",
    "What can I get you? "
]

user_closing_remarks_prompts = [
    "Thank you for your purchase!",
    "Thanks! Please come again.",
    "Thank you!"
]

print(random.choice(user_greetings_prompts))

age = int(input(random.choice(user_info_prompts)))

if age < 18:
    print("We do not server underaged customers.")
else:
    print(random.choice(user_shopping_list_prompts))
    number_of_shopping_items = 0
    while True:
        shopping_item = input("Current item: ")
        if shopping_item == "":
            break
        number_of_shopping_items += 1
    print(f"Your waiting time is {number_of_shopping_items * 30} seconds.\n 30 seconds for every product.")
    print(random.choice(user_closing_remarks_prompts))
