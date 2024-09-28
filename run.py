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
    while True:
        try:
            print("\nPlease, choose your category:")
            for idx, division in enumerate(divisions.keys(), start=1):
                print(f"{idx}. {division}")

            choice = int(input("Enter the category number: "))
            if 1 <= choice <= len(divisions):
                return list(divisions.keys())[choice - 1]
            else:
                print("Invalid selection.Please Choose a valid category number.")
        except ValueError:
            print("Please enter valid number.")

"""
System randomly choosing the word from chosen division
"""
def choose_word(division):
    words = divisions.get(division)
    if words:
        return random.choice(words).lower()
    else:
        print(f"No words available in the division '{division}'")
        return None

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
          ------
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
        """,
         
    ]
    return stages[tries]

def play_game(word, max_tries, hint):
    if word is None:
        print("No word was selected.Exiting game.")
        return

    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = max_tries
    score = 0
    hints_used = 0

    print("\nWelcome to Hangman!")
    print(f"You have {tries} attempts to guess the word.")
    print (display_hangman(0))
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
                print(f"Good job! '{guess}' is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)

                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                score += 10

                if "_" not in word_completion:
                    guessed = True   

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print (f"You already guessed the word '{guess}'.")
            elif guess != word:
                print(f"'{guess}' is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

                score += 20

        else:
            print("Invalid input, Please guess a single letter or the entire word.")

        if tries == max_tries  // 2 and hints_used == 0:
            use_hint = input (f"Would you like a hint? (Y/N):").strip().lower()
            if use_hint == 'y':
                print(f"Hint: {hint}")
                hints_used += 1

        print(display_hangman(tries))
        print(word_completion)
        print(f"Tries left: {tries}")
        print("\n")


    if guessed:
        score += (tries * 6)
        print(f"Congratulations! You guessed the word '{word}!Your score: {score}")
    else:
        print(f"Sorry, you ran out of tries.The word was '{word}'.Your score: {score}")


def main():
    max_tries = 7
    while True:
        division = choose_division(divisions)
        word = choose_word(division)
        hint = hints.get(word)
        play_game(word, max_tries, hint)

        if input("Do you want to play again? (Y/N):").strip().upper() != 'Y':
            print("Thank you for playing Hangman! Goodbye!")
            break


if __name__ == "__main__":
    main()

        