from random import randint

def draw_letters(): # No parameters
    
    # This letter pool should reflect the distribution of letters as described in the Readme file Wave 1
    distribution_of_letters = { "A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1 }
    
    letter_pool = [] # This represents the pool of letters that the player can draw from

    for letter, frequency in distribution_of_letters.items():
        for i in range(frequency):
            letter_pool.append(letter)


    # Each string should contain exactly one letter
    # There are only 2 available C letters, so draw_letters cannot ever return more than 2 Cs
    # Since there are 12 Es but only 1 Z, it should be 12 times as likely for the user to draw an E as a Z
    # Invoking this function should not change the pool of letters
    # Imagine that the user returns their hand to the pool before drawing new letters

    hand = [] # These represent the hand of letters that the player has drawn
    random_index = 0
    for i in range(10):
        random_index = randint(0, len(letter_pool) - 1) # The letters should be randomly drawn from a pool of letters
        

        while letter_pool[random_index] == 0: # If the randomly drawn letter has already been drawn, then draw again
            random_index = randint(0, len(letter_pool) - 1)
        hand.append(letter_pool[random_index])
        letter_pool[random_index] = 0 # Once a letter is drawn, it cannot be drawn again until the pool is reset

        #  alternative approach without setting to 0:
        # hand.append(letter_pool.pop(random_index))


    return hand # Returns an array of ten strings

def uses_available_letters(word, letter_bank): # Has two parameters:
    """
    Checks if the input word can be formed from the letters in the letter bank.
    
    Parameters:
        word (string): describes some input word.
        letter_bank (list): describes an array of drawn letters in a hand.

    Returns:
        type: True of False.
    """
    # Returns True if every letter in the input word is available (in the right quantities) in the letter_bank
    # Returns False if not; if there is a letter in input that is not present in the letter_bank or has too much of compared to the letter_bank
    list_of_available_letters = []
    for letter in letter_bank:
        list_of_available_letters.append(letter.upper())
    
    for letter in word:
        if letter.upper() in list_of_available_letters:
            
            # list_of_available_letters.remove(letter.upper())
            
            # alternative approach without using remove():
            for i in range(len(list_of_available_letters)):
                if list_of_available_letters[i] == letter.upper():
                    list_of_available_letters[i] = 0
                    break
        else:
            return False
        
    return True

def score_word(word):
    """
    Returns the score of a given word as defined by the Adagrams game.
    
    Parameters:
        word (string): string of characters.

    Returns:
        int: number of points.
    """
    # Each letter's point value is described in the table below
    score_chart = { "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10 }
    
    score = 0

    # Each letter within word has a point value. The number of points of each letter is summed up to represent the total score of word
    for letter in word:
        if letter.upper() in score_chart:
            score += score_chart[letter.upper()]
    if len(word) >= 7:
                score += 8 # If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
    return score

def get_highest_word_score(word_list):
    """
    This function looks at the list of word_list and calculates which of these words has the highest score.
    
    Parameters:
        word_list (list): list of strings.

    Returns:
        tuple: a winning word and it's score.
    """

    highest_score = 0
    pool_of_words_with_scores = {}
    for word in word_list:
        score = score_word(word)
        pool_of_words_with_scores[word] = score

    for word, score in pool_of_words_with_scores.items():
        if score > highest_score:
            highest_score = score
    
    # In the case of tie in scores:
    # prefer the word with the fewest letters...
    # ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
    # If the there are multiple words that are the same score and the same length, pick the first one in the supplied list
    min_length = 11
    for word, score in pool_of_words_with_scores.items():
        if len(word) == 10 and score == highest_score:
            winning_word = word
            break
        elif len(word) < min_length and score == highest_score:
            min_length = len(word)
            winning_word = word
        
    # index 0 ([0]): a string of a word
    # index 1 ([1]): the score of that word
    return (winning_word, highest_score)