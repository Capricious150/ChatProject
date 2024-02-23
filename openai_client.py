from openai_character import Character

bot = Character("You are a helpful assistant who will, rarely, shout about his hatred of seagulls", "Bot")

def prompt_message(bool = False, bool2 = False):
    print("======")
    message = input(f"Please enter a message for {bot.get_name()}: ")
    if message == "q": return False
    if bool == True and bool2 == False: return bot.cont(message)
    elif bool == True and bool2 == True: return bot.cont(message, True)
    else: return bot.create_new(message)

def prompt_description():
    print("======")
    print("Please tell the AI how to behave. Write in the form of a 'You Are' statement")
    desc = input("For example, 'You are a brave warrior from Atlantis'.: ")
    if desc == "q": return False
    name = input("Enter a name for this character: ")
    if name == "q": return False
    bot.update_character(desc, name)

print("You may enter 'q' to quit at any time.")
while True:
    print("What would you like to do? Please choose from the following options: ")
    print("1: Send a message to OpenAI")
    print("2: Send a message to OpenAI with conversation history enabled for this conversation")
    print("3: View history")
    print("4: View history length")
    print("5: Describe character")
    print("6: Update character")
    response = input("Your selection: ")
    
    if response == "q": break
    
    try:
        match float(response):
            case 1:
                reply = prompt_message()
                if reply == False: break
                else: 
                    print("======")
                    print(reply)

            case 2:
                reply = prompt_message(True, False)
                if reply == False: break
                else:
                    print("======")
                    print(reply)
            
            case 3:
                print("======")
                print(bot.get_history())
            
            case 4:
                print("======")
                print(bot.history_length())
            
            case 5:
                print("======")
                print(bot.describe_character())

            case 6:
                reply = prompt_description()
                if reply == False: break
                else: 
                    print("======")
                    print("Done")
                    
            
            case _: 
                print("Please enter a valid option")
                continue

    except Exception as e:
        print(f"ERROR: {e}")

    print("======")

