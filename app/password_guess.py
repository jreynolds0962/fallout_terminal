# import os
import random
import linecache


file = 'app/word_lists/five_letters.txt'

difficulty = {
    "HARD": 7,
    "MEDIUM": 6,
    "EASY": 5
}

def get_line_numbers(total_lines: int, amount_of_words: int) -> set:
    """This function should get a SET of numbers to grab unique lines
    from the text file

    Args:
        total_lines (_type_): Total number of lines in the text file
        amount_of_words (_type_): Amount of words wanted for difficulty

    Returns:
        _type_: SET of ints
    """
    numbers = set()
    
    # iterate throught amount of words wanted
    while len(numbers) < amount_of_words:
        random_line_number = random.randint(0, total_lines - 1)
        numbers.add(random_line_number)
    return numbers

def get_words(file_name, number_set) -> list:
    """This function returns a list of words to add to the
    hacking terminal

    Args:
        file_name (_type_): name of word count file
        number_list (_type_): set of random numbers for line
    
    Returns:
        _type_: LIST of strings
    """
    words = [linecache.getline(file_name, line_number).strip() 
             for line_number in number_set]
    return words
    

with open(file) as f:
    # head = [next(f).strip() for _ in range(10)]
    lines = len(f.readlines())

line_numbers = get_line_numbers(lines, difficulty["MEDIUM"])
words = get_words(file, line_numbers)
print(words)





# print(head)
# print(random.choice(head))
# password = random.choice(head)

# print(lines)