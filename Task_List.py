import random

def build_deck():
    new_deck = {}
    subject = input('Enter the name of the subject: ')

    more_cards = 'y'
    while more_cards == 'y':
        term_in = input("Enter a term: ")
        def_in = input("Enter the definition: ")
        new_deck[term_in] = def_in
        print("There are now {} cards in the deck".format(len(flashcards)))
        more_cards = input("Any more cards to add? y/n: ")

        file_name = subject + ".txt"
        with open(file_name, 'w') as dave:
            dave.write( str(new_deck) )

def quiz_time():
    saved_deck = {}
    subject = input('Enter the name of the subject: ')
    file_name = subject + ".txt"
    with open(file_name, 'r') as scarlet:
        contents = scarlet.read()
        saved_deck = eval(contents)
    more_quiz = 'y'
    print("Time for a quiz!")
    while more_quiz == 'y':
        term, definition = random.choice(list(flashcards.items()))
        input("Here is the term: {}\nPress Enter to see the definition when ready".format(term))
        print("Here's the definition: " + definition)
        more_quiz = input("Do you want to try another card? y/n: ")
        
while True:
    option = input('1) Create a new deck, 2) Open a saved deck, 3) Quit')
    if option == '1':
        build_deck()
    elif option == '2':
        quiz_time()
    elif option == '3':
        break
    else:
        print("Invalid Option!")