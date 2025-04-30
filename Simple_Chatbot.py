import random 

greetings = ["Hello", "Hi", "Hey", "Howdy", "Greetings", "Whatsup", "Salutations", "Bonjour", "Hola", "Ciao"]
farewell = ["Goodbye", "Bye", "See you later", "Take care", "Farewell", "Adios", "Ciao", "Sayonara", "Au revoir", "Later"]

print(random.choice(greetings),"!")

user = input("Say something or type bye to quit\n").strip().lower()

keywords =  ["music", "movie"]
responses = ["That's interesting!", "Tell me more!"]

while user != "bye":
    keyword_found = False
    
    #for index in range(len(keywords)):
    #    print("keyword: ", keywords[index])
    #    print("response: ", responses[index])
    try:
        idx = keywords.index(user)
        keyword_found = True
        print("Bot: ", responses[idx])
    except ValueError:
        idx = -1
        keyword_found = False
    
    if keyword_found == False:
        print("Searching from predefined list...")
        try:
            with open("chatbot_memory.txt", "r") as f:
                for line in f:
                    user_f, response_f = line.strip().split(":")
                    keywords.append(user_f)
                    responses.append(response_f)
                    continue
        except FileNotFoundError:
            pass
        try:
            idx1 = keywords.index(user)
            keyword_found = True
        except ValueError:
            idx1 = -1

        if idx1 == -1:
            print("I don't know about that yet!\n")
            user_response = input("What would you like me to say next time?\n")
            keywords.append(user)
            responses.append(user_response)
            with open("chatbot_memory.txt", "a") as f:
                f.write(f"{user}:{user_response}\n")
        else:
            print("Bot: ", responses[idx1])
            keyword_found = True
    user = input("Say something or type bye to quit\n").strip().lower()
print(random.choice(farewell), "!")