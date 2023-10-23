import random

# Define lists of characters
lowers = ['a', 'b', 'c' 'd', 'e', 'f', 'g'] # etc.
uppers = ['A', 'B', 'C', 'D', 'E','F','G'] # etc.
nums = ['0', '1', '2','3','4','5','6','7','8','9'] # etc.
specials = ['*', '&', '%'] # etc.
all_chars = lowers + uppers + nums + specials

# Combine all character options
all_characters = lowers + uppers + nums + specials

while True:
    # Start with an empty string
    password = ''

    # Ask the user how many characters long the password should be
    length = int(input('How many characters? '))

    # Loop until the password is long enough
    while len(password) < length:
        # Choose 1 random character from one of the lists above
        rand_char = random.choice(all_chars)

        # Add that one character to the password string
        password += rand_char

    # Output the resulting string
     print("Generated Password: {}".format(password))

    # Ask the user if they want to create another, or if they want to quit
    redo = input("Generate another password? (yes/no): ")
    if redo != "yes":
        break
