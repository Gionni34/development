'''
# You are given a triangle with a side #1 of 4, base of 6, and side #2 of 3. Create
a brief python script that will determine the perimeter of the triangle. Comment your code

1. Print the perimeter
2. Using boolean operators is side #1 greater than the base?
3. Using boolean operators is side #2 less than the base?
4. Using boolean operators is base larger than or equal to side #1?

'''


# Variables

side_one = 6
base = 4
side_two = 7

# Formula
perimeter = side_one + base + side_two
print(perimeter)
print('Using boolean operators is side #1 greater than the base?',side_one > base)
print('Using boolean operators is side #2 less than the base?', side_two < base)
print('Using boolean operators is base larger than or equal to side #1?',base >= side_one)
