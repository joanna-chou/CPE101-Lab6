# Lab 6
#  
# Name: Joanna Chou
# Instructor: S. Einakian 
# Section: 07

# Rangeless Functions - Do not use range function.
# Function 1 - This function takes a given string and returns a string of vowels that occur in the given string, in the order which they appear.
def vowel_extractor (string: str) -> str:
    new_string = ''
    vowel = "aeiouAEIOU"
    for letter in string:
        if letter in vowel:
            new_string = new_string + letter
    return(new_string)

# Function 2 - This function takes a given string and returns a string where the first letter of each word in the string start with an uppercase.
def str_captalize(string: str) -> str:
    new_string = ''
    new_word = True
    for letter in string:
        if letter == ' ':
            new_word = True
            new_string = new_string + ' '
        else:
            if new_word == True:
                if "A" <= (letter) <= "Z":
                    new_string = new_string + letter
                else:
                    new_string = new_string + chr(ord(letter)-32)
            else:
                new_string = new_string + letter
            new_word = False
    return new_string


# Function 3 - This function takes a given string and returns the ROT-13 encoding of the given characters.
def str_rotate(string: str) -> str:
    new_string = ''
    new_letter = ''
    for letter in string:
        new_letter = (chr(ord(letter)+13))
        if "A" <= (letter) <= "Z" and (new_letter) > "Z":
            new_letter = chr(ord(new_letter)-26)
        elif "a" <= (letter) <= 'z' and (new_letter) > "z":
            new_letter = chr(ord(new_letter)-26)
        elif ord(letter) == 32:
            new_letter = letter
        new_string = new_string + new_letter
    return new_string


# Range Functions - Use range function.
# Function 4 - This function takes a string and three integer numbers (an inclusive start index, an exclusive stop index, and a step) and returns a substring that begins from the start idex and ends at stop index and increasing step characters.
def make_substring (string: str, start: int, end: int, step: int) -> str:
    new_string = ''
    for num in range(start,end,step):
            new_string = new_string + string[num]
    return new_string

# Function 5 - This function takes a string and returns True if the string is a palidrome and false otherwise.
def is_palindrome (string: str) -> bool:
    new_string = ''
    for idx in range(-1, -(len(string)+1),-1):
        new_string = new_string + string[idx]
    if new_string == string:
        return True
    else:
        return False

# Function 6 - This function takes a string and a character and returns how many times the character was repeated in the string. Return -1 if the character is not used.
def count_characters (string: str, charac: str) -> int:
    new_string = ''
    count = 0
    for idx in range(len(string)):
        if string[idx] == charac:
            count += 1
    if count == 0:
        return -1
    else:
        return count
