import random

#divisions

divisions = {

    "Flowers": ['daisy', 'daffodil', 'hibiscus', 'lavander', 'primrose',
     'dandelion', 'calendula', 'geranium', 'petunia', 'snowdrop'],
    "Trees": ['birch', 'oak', 'larch', 'willow', 'maple', 'chesnut tree',
     'spruce', 'magnolia', 'cypress', 'juniper'],
    "Birds": ['stork', 'peacock', 'hummingbird', 'pigeon', 'penguin', 
    'woodpecker', 'swan', 'parrot', 'robin', 'blackbird']
}

hints = {

    "daisy": "'He loves me, he loves me not' a familiar rhyme associated with ",
    "daffodil": "Other name of Narcissus-one of the most popular flowers in the world, mainly due to the well-known myth of the Greek youth who fell in love with himself",
    "hibiscus": "This flower is the floral emblem of Haiti and Malaysia",
    "lavander": "Originally from the Latin word that means 'to wash'",
    "primrose": "In the United Kingdom, it is against the law to pick this flower growing in the wild",
    "dandelion": "This flower`s seeds can travel up to five kilometers from their original location",
    "calendula": "This flower is also known as the 'flower of the rains'",
    "geranium": "The essential oils in certain types of scented this flower help alleviate depression and stress",
    "petunia": "This flower is related to tobacco",
    "snowdrop": "They were named after earrings",
    "birch": "The most common tree all over the world",
    "oak": "These trees appeared on our planet about 65 million years ago",
    "larch": "Wood from this tree is very valuable because it is resistant and it grows quickly",
    "willow": "Raindrops falling from their drooping branches resemble tears",
    "maple": "Most colourful tree in the Autumn",
    "chesnut": "Middle Ages, this tree became a staple foodstuff in Europe, earning them the nickname 'bread of the woods'",
    "spruce": "The Wright brothers constructed their first aircraft, the Wright Flyer, using this wood",
    "magnolia": "In Japan, the this tree is associated with the sun goddess, Amaterasu",
    "cypress": "This tree is extensively used for decorating gardens",
    "juniper": "For more than 300 years, berries of this tree have been a popular flavoring agent for gin",
    "stork": "They are symbols of good luck and prosperity",
    "peacock": "This bird take three years to develop its tail plumage",
    "hummingbird": "Their wings beat about 70 times per second (200 times per second when diving!)",
    "pigeon": "This bird is renowned for its outstanding navigational abilities",
    "penguin": "They spend nearly 50 prcent of their lives in the water and the other 50 procent on land",
    "woodpecker": "Called as 'a doctor of the woods'",
    "swan": "This bird mate for life",
    "parrot": "It eats with its feet",
    "robin": "Angry Birds-they're so territorial that they often fight to the death defending their area",
    "blackbird": "Females usually are brown and males are in black colour"

}


"""
Player choosig the category to play
"""
def choose_division(divisions):
    print("Please, choose your category:")
    for idx, division in enumerate(divisions.keys(), start=1):
        print(f"{idx}. {division}")

    choice = int(input("Enter the category number: "))
    return list (divisions.keys())[choice - 1]

"""
System randomly choosing the word from chosen division
"""
def choose_word(division):
    return random.choice(divisions[division]).lower()

def display_hangman(tries):
    stages = [
        """
         -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / 
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |  
           |
        """,
        """
           -----
           |   |
           |   O
           |   |
           |  
           |
        """,
        """
           -----
           |   |
           |   O
           |   
           |  
           |
        """,
        """
           -----
           |   |
           |   
           |   
           |  
           |
        """
    ]
    return stages[tries]

def select_level():
    print("\nPlease, select your level:")
    print("1. Easy (12 tries)")
    print("2. Medium (8 tries)")
    print("3. Hard (6 tries)")


    choice = int(input("Enter difficulty level number:"))
    if choice == 1:
        return 12
    elif choice == 2:
        return 8
    else:
        return 6

def play_game(word, max_tries, hint):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = max_tries
    score = 0
    hints = 0

    print("Welcome to Hangman!\n")
    print(f"You have {tries} attempts to guess the word.")
    print (display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word:").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter '{guess}'.")
            elif guess not in word:
                print(f"'{guess}' is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! '{guess}'is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                score += 10

                if "_" not in word_completion:
                    guessed = True    


        