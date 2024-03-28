import datetime, random

print('Hello world.')
print('Today is ' + str(datetime.date.today()))

continue_play = True

print("Welcome to your magic 8 ball")

while continue_play:
    print("Ask me a question:")
    question = input()
    answer = random.randint(1,3)
    if answer == 1:
        print("Yes")
    elif answer == 2:
        print("No") 
    else:
        print("Maybe")
    
    print("Would you like to ask another question? (y/n)")
    response = input()
    #print(response.lower())
    if response.lower() == 'n':
        continue_play = False
    elif response.lower() == 'y':
        continue_play = True
    else:
        print("Invalid entry")
        break
    