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

running = True