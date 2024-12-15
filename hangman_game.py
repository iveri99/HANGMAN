import random

word_list = [
    "astronaut", "banana", "chocolate", "dinosaur", "elephant", "giraffe", "harbor", "igloo", "jungle",
    "kitchen", "lemonade", "mountain", "notebook", "octopus", "pencil", "quilt", "robot", "sunflower",
    "tornado", "umbrella", "vampire", "wizard", "xylophone", "yacht", "zebra", "adventure", "blueberry",
    "courage", "diamond", "envelope", "frostbite", "guitar", "hurricane", "invisible", "jigsaw", "kaleidoscope",
    "lighthouse", "marshmallow", "nebula", "opal", "puzzle", "quicksand", "rainbow", "sapphire", "tulip",
    "unicorn", "vortex", "whisper", "xenon", "yellow", "zombie", "appreciate", "believe", "cobblestone",
    "delicious", "elephant", "fascinate", "geometry", "heartbeat", "inspire", "journey", "knowledge",
    "lemon", "mystery", "nostalgia", "oxygen", "paradox", "quicksilver", "resilience", "symphony", "treasure"
]

chosen_word = random.choice(word_list) # Chooses a word from the list at random

print ("WELCOME TO THE HANGMAN GAME!")

hangman_stages = [
    """
       ------
       |    |
            |
            |
            |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
            |
    ---------
    """
]

guessed_word = ["_"] * len(chosen_word) # Converts length of chosen word into underscores

print(hangman_stages[0]) # Prints first stage (0 index) of hangman
guesses = 0 # Guesses will be counted, starts from 0

while "_" in guessed_word and guesses < len(hangman_stages) -1: # Main while loop 
    print("Current word: " + " ".join(guessed_word)) # Prints the word in underscores
    guess = input("Guess a letter: ") # Asks user for input

    if guess in chosen_word: # Conditional statement
        for i in range(len(chosen_word)): # For loop
            if chosen_word[i] == guess: # If user's guess is same as an index within chosen_word,
                guessed_word[i] = guess # guessed_word index (underscores) is changed to user's guess
        print("CORRECT!") # Print statement
    else:
        print("Incorrect guess, try again.") # Else if user's guess is wrong, print statement
        guesses += 1 # Guesses variable is increased by 1 

    print(hangman_stages[guesses]) # Prints the stage of hangman based on num of guesses

if guesses == len(hangman_stages) -1: # If the number of guesses reaches the final stage of hangman,
    print(f"GAME OVER! The word was {chosen_word}.") # Print statement
else:
    print(f"CONGRATULATIONS! You guessed the word {chosen_word} correctly.") # Print statement