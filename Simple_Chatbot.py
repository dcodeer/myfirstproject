import random 

greetings = ["Hello", "Hi", "Hey", "Howdy", "Greetings", "Whatsup", "Salutations", "Bonjour", "Hola", "Ciao"]
farewell = ["Goodbye", "Bye", "See you later", "Take care", "Farewell", "Adios", "Ciao", "Sayonara", "Au revoir", "Later"]

print(random.choice(greetings),"!")

user = input("Say something or type bye to quit\n").strip().lower()

keywords =  ["music", "movie", "food", "weather", "sports", "news", "travel", "games", "books", "technology"]
responses = ["That's interesting!", "Tell me more!", "I see!", "Really?", "Oh, wow!", "That's cool!", "Fascinating!", "Wow, that's great!", "Sounds fun!", "Nice!"]

while user != "bye":
    keyword_found = False

    for index in range(len(keywords)):
        if keywords[index] in user:
            print(random.choice(responses))
            keyword_found = True

    if keyword_found == False:
        new_keyword = input("I don't understand. Can you tell me more How to respond to it?\n")
        keywords.append(new_keyword)
        responses.append("I see! I will remember that.\n")
        print("Thanks for teaching me!\n")

    user = input("Say something or type bye to quit\n").strip().lower()
print(random.choice(farewell), "!")