# import os
import random
import linecache
import sys
from time import sleep
from argparse import ArgumentParser, Namespace

parser = ArgumentParser(description="Fallout Terminal -- select diffifculty level")
parser.add_argument("-d", "--difficulty", metavar="difficulty", 
                    type=str, choices=["easy", "medium", "hard"],
                    default="medium",
                    help="select difficulty level"
                    )

# first int is count of words displayed on screen, second int is count of letters in word
DIFFICULTY: dict[str, list] = {
    "HARD": [7, 7, 'app/word_lists/seven_letters.txt'],
    "MEDIUM": [6, 5, 'app/word_lists/five_letters.txt'],
    "EASY": [5, 4, 'app/word_lists/four_letters.txt']
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

def get_words(file_name: str, number_set: set) -> list:
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

def likeness(solution: str, password: str) -> int:
    likeness = 0
    for letter_x, letter_y in zip(solution, password):
        if letter_x == letter_y:
            likeness += 1
    return likeness

def guess(solution: str, password: str) -> bool:
    if solution == password:
        return True

def typing(phrase: str) -> None:
    for char in phrase:
        sleep(random.uniform(0.1,0.5))
        sys.stdout.write(char)
        sys.stdout.flush()

def main():
    
    parsed_args: Namespace = parser.parse_args()
    
    #cli difficulty argument
    user_difficulty = parsed_args.difficulty.upper()
    
    file = DIFFICULTY[user_difficulty][2]
    
    with open(file) as f:
        lines = len(f.readlines())

    line_numbers = get_line_numbers(lines, DIFFICULTY[user_difficulty][0])
    words = get_words(file, line_numbers)
    print(words)

    attempt_count = 4

    password = random.choice(words)

    while attempt_count > 0:
        print(f"{attempt_count} attempt(s): {attempt_count * '*'}")
        print("-" * 25)
        
        solution = input("Password Guess: ")
        if len(solution) != DIFFICULTY[user_difficulty][1]:
            print(f"Solution must be {DIFFICULTY[user_difficulty][1]} characters long")
        else:
            if guess(solution, password):
                typing("Password Correct")
                break
            else: 
                print(likeness(solution, password), "/", len(password), " likeness")
                attempt_count -= 1

if __name__ == "__main__":
    main()