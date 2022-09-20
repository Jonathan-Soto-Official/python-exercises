# 1. Define a function named is_two. It should accept one input and return True if the passed input
#    is either the number or the string 2, False otherwise.

def is_two(x):
    if x == 2 or x == '2':
        return True
        print("True")
    else:
        return False
        print("False")
is_two(input())


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(string):
        if string.lower() in 'aeiou':
            return True
        else:
            return False
is_vowel(input())


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, 
#    False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(string):
    string = string.lower()
    return not is_vowel(string)


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter
#    of the word if the word starts with a consonant.

def capitalize(string):
    if string[0].lower() in 'bcdfghjklmnpqrstvwxyz':
        return string.capitalize()
    else: 
        return string


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def tip_amt(tip_p, bill):
    #uses a conditional statement to test whether the function parameter tip_p (tip%) is between 0 and 1
    #if it is returns the product of the function parameters, tip_p and bill (amount of the bill)
    if 0 <= tip_p <= 1:
        return tip_p * bill
    else:
        return 'tip_p must be between 0 and 1 - Try again!'

tip_amt(.2, 10)


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage,
#    and return the price after the discount is applied.

def discount(price, percent):
    return price - (price * percent)

discount(10, .1)


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas
#    in it as input, and return a number as output.

def handle_commas(string):
    return int(string.replace(',', ''))


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated
#    with that number (A-F).

def get_letter_grade(num_grade):
    #takes the num_grade parameter and uses conditional statements to evaluate what letter grade to return
    #when the num_grade argument is entered below it will run the function
    if num_grade > 89:
        return 'A'
    elif num_grade > 79:
        return 'B'
    elif num_grade > 69:
        return 'C'
    elif num_grade > 59:
        return 'D'
    else:
        return 'F'


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    string = string.lower()

    for char in "aeiou":
        string = string.replace(char,'')
    return string


    # 10. Define a function named normalize_name. It should accept a string and return a valid python identifier,
#     that is:

# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# 
#   For example:
# - Name will become name
# - First Name will become first_name
# - % Completed will become completed

def normalize_name(string):
    string = string.lower()
    
    string = string.strip()

    string = string.replace(' ', '_')

    while not string[0].isalpha():
        string = string[1:] 

    return string

normalize_name('     @*&       here is same   ')


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is
#     the cumulative sum of the numbers in the list.

# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(list):

    sum_list = []
    
    i = 0

    for count in range(0, len(list)):
        i = i + list[count]
        sum_list.append(i)
    return sum_list

cumulative_sum([1, 1, 1])