1. Create a word library -------- done
    - Create different libraries of specific word lengths 
    - Ex. library where all words are 4 letters, another where all are 6 letters



2. Randomly select 10 words from single library
    - Have a "answer" that is randomly selected from those five words
        - use random module to pick out 10 unique lines from the file
        - use set to make sure values are unique

3. Have Windows and Pads to seperate "Welcome", Columns, and Entries submitted
    - Attemps Remianing to be in Columns Window, shows after all chars printed

4. Create two columns that have characters and words choices in them
    - 16 rows per column
        - each row needs to have the hex code in front
        - each show should be a continuation of the previous row in case of word overlay
        - the top of column two should be a continuation of the bottom of column 1
    - may need to seperate hex code and characters, but make them display each row the same time
        - this is because we dont want the user being able to select the hex code


5. Let a user select any word from the randomly selected list
    - create menu style layout with cursers library
    - you will use while loop with keystrokes
        - *while True take keystroke?
            - break loop if Attempts Remaining is 0?
            - break loop if found == true?


6. If the selection is correct "let them in"
7. If the selection is incorrect, lose 1 try and allow the user to select a word again
    - Let the user select a word until all 3 uses are up
    - Make it to where User can only guess the items in the list (if guess not in list, try again)
    - Take out a guess from list if already tried that word
    
8. Add arguments to the cli command ------ done