import random

def sum_list(numbers):
    """
    Calculate the sum of a list of numbers.
    
    Args:
    numbers (list of int): List of numbers to sum up.
    
    Returns:
    int: Sum of the numbers.
    """
    return sum(numbers)

def count_vowels(string):
    """
    Count the number of vowels in a given string.
    
    Args:
    string (str): String to check for vowels.
    
    Returns:
    int: Number of vowels in the string.
    """
    vowels = "aeiouy"
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

def even_numbers(numbers):
    """
    Filter even numbers from a list.
    
    Args:
    numbers (list of int): List of numbers to filter.
    
    Returns:
    list of int: List containing only even numbers.
    """
    return [num for num in numbers if num % 2 == 0]

def count_letters(words):
    """
    Count the occurrences of each letter in a list of words.
    
    Args:
    words (list of str): List of words to analyze.
    
    Returns:
    dict: Dictionary with letters as keys and their counts as values.
    """
    letter_count = {}
    for word in words:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def count_palindromes(string):
    """
    Count the number of palindromic substrings in a given string.
    
    Args:
    string (str): String to check for palindromic substrings.
    
    Returns:
    int: Number of palindromic substrings.
    """
    count = 0
    n = len(string)
    for i in range(n):
        for j in range(i + 2, n + 1):
            if string[i:j] == string[i:j][::-1]:
                count += 1
    return count

def binary_addition(a, b):
    """
    Add two binary numbers represented as strings.
    
    Args:
    a (str): First binary number.
    b (str): Second binary number.
    
    Returns:
    str: Binary representation of the sum.
    """
    a_decimal = int(a, 2)
    b_decimal = int(b, 2)
    sum_decimal = a_decimal + b_decimal
    return bin(sum_decimal)[2:]

def play_rps():
    """
    Play the game of Rock, Paper, Scissors against the computer.
    """
    choices = ["rock", "paper", "scissors"]
    score = {"player": 0, "computer": 0, "tie": 0}

    while True:
        # Get the player's choice
        player = input("Choose rock, paper, or scissors (or 'quit' to exit): ")
        if player == "quit":
            break

        # Generate the computer's choice
        computer = random.choice(choices)

        # Determine the winner
        if player == computer:
            result = "tie"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            result = "player"
        else:
            result = "computer"

        # Update the score
        score[result] += 1

        # Display the result
        print(f"You chose {player}, the computer chose {computer}: {result} wins.")

    # Display the final score
    print(f"Final score: Player - {score['player']}, Computer - {score['computer']}, Tie - {score['tie']}.")

###### Exercise 1 ######
print("-----Exercise 1 :-----")
#### Q1 ####
print("Q1:")
my_list = [1, 5, 9, 23]
print("Sum of this list", my_list, "=", sum_list(my_list))
#### Q2 ####
print("Q2:")
string = "Hello, world!"
print("Total vowels =", count_vowels(string))
#### Q3 ####
print("Q3:")
numbers = [1, 2, 3, 4, 5, 6]
print("Even numbers are:", even_numbers(numbers))
#### Q4 ####
print("Q4:")
words_list = ['inas', 'computer', 'test']
print(count_letters(words_list))

###### Exercise 2 ######
print("-----Exercise 2 :-----")
string = "racecarannakayak"
print("Total palindromes =", count_palindromes(string))

###### Exercise 3 ######
print("-----Exercise 3 :-----")
a = "101011"
b = "1101"
print(a, "+", b, "=", binary_addition(a, b))

###### Exercise 4 ######
print("-----Exercise 4 :-----")
play_rps()
