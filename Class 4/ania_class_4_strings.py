''' Class 4 Strings '''

# String operators

'''Concatenation'''
# operator_code = 'A987'
# part_id = '49Be'
# item_number = operator_code + part_id
# print(item_number)

# first_name = 'Gionni'
# last_name = 'Young'
# full_name = first_name + ' ' + last_name
# print(full_name)


''' Multiplication '''

# greeting = 'hip hop hurray ' * 3
# print(greeting)

# my_favColor = 'Pink ' * 5
# print(my_favColor)


# Reference vs Value equality == vs is
x = 'hello'
str2 = 'HELLO'.lower()
# print(x)
# print(str2)
# print(x == str2)
# print(x is str2)
# print(id(x))
# print(id(str2))


''' in - Returns True if a string appears inside another string (as a substring), and False otherwise.'''

# test_character = 'b'
# test_string = 'bananas'
# print(test_character in test_string) #?

''' create a quick test to see if the sub string 'spreh' can be found in the string 'Incomprehensibilities' '''
test_chars = 'spreh'
test_word = 'Incomprehensibilities'

# print(test_chars in test_word)

''' len() - Returns the length of a string, aka the number of characters in a string.'''

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# length_of_alphabet = len(alphabet)
# print(length_of_alphabet)

# animal = 'monkey'
# length_of_animal = len(animal)
# print(length_of_animal)



# String methods

word_1 = 'happy' #.capitalize
# print(word_1.capitalize()) 
# print('happy'.capitalize())

ex_1 = 'cereal' # capitalize me!
# print(ex_1.capitalize())
# print('cereal'.capitalize())


word_2 = 'SuPrISe' # .casefold
# print(word_2.casefold())
# print('SuPrISe'.casefold())

ex_2 = 'RuMMaGe' # make me lower case!
# print(ex_2.lower())
# print('RuMMaGe'.lower())

word_3 = 'ZOO'
# print(word_3.casefold())
# print('ZOO'.casefold())
# print(word_3.lower())
# print('ZOO'.lower())

ex_3 = 'PLANET' # lets make this lower case?
# print(ex_3.casefold())
# print(ex_3.lower())


# Center Method

word_4 = 'Good Evening'
# print(word_4)
# print(word_4.center(100)) # Takes up 100 characters and centers the string
# print(word_4.center(50))

ex_4 = 'Hello World' # Center me within a space of 65 characters 
# print(ex_4.center(65))

word_5 = 'Pseudopseudohypoparathyroidism'  # How many p's?
# print(word_5.count('p'))

ex_5 = 'Antidisestablishmentarianism' # How many times does the letter 'e' occur?
# print(ex_5.count('e'))

word_6 ='I\tam\ta\ttab' # extendtabs
# print(word_6)
# print(word_6.expandtabs(10))

create_new_line = 'I\n am\n a\n newline'
# print(create_new_line)

ex_6 = "Let's\t do\t some\t coding!" # Lets try to increase the tabs to 10 whitespaces
# print(ex_6.expandtabs(15))

# Find the position of the letter k
word_7 = 'Omphaloskepsis'
# print(word_7.find('k'))

ex_7 = 'Dichlorodifluoromethane' # Find the position of the letter f
# print(ex_7.index('f'))
# print(ex_7.index('x')) # Will only find letter if in word

word_8 = 'Supercalifragilisticexialidocious'
# print(word_8.index('g'))



# isalnum() Are all my characters alphanumeric? Alphanumeric is A-Z, a-z and 0-9

test_1 = 'abcdef'
test_2 = '%$123'

# print(test_1.isalnum())
# print(test_2.isalnum())


ex_8 = '123*'   # Am I alphanumeric?
# print(ex_8.isalnum())



# isalpha() Area all characters in the string in the alphabet?

test_3 = 'abcde'
test_4 = '012345'

# print(test_3.isalpha())
# print(test_4.isalpha())


ex_9 = 'LMN0P' # Are we all in the alphabet
# print(ex_9.isalpha())

# isdecimal() Are all characters decimals?

test_5 = '1234P'
test_6 = '234567'

# print(test_5.isdecimal())
# print(test_6.isdecimal())

ex_11 = '123456' # Check for decimals?
# print(ex_11.isdecimal())


# isdigit() Are all characters digits?

test_7 = 'H1234'
test_8 = '9876'
# print(test_7.isdigit())
# print(test_8.isdigit())

ex_10 = '123Hello' # Check for digits!
# print(ex_10.isdigit())


# strip() Returns a trimmed version of the string
username = '   jessica123    '


ex_21 = '  sportsfan876  ' # sanitize this string

'''
Write some code that will take a string from the user and print if it is a number or not.

Examples:
apple
False

4
True
'''

# Get input from user


# Test input



# Provide output
































