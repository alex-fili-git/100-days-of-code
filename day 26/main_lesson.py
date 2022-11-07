# list and dictionary comprehensions cuts down on amount of code
# you create a new list from an existing list
numbers = [1, 2, 3]
# instead of for loop
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
#now
# new_list = [new_item for items in list]
new_list = [n+1 for n in numbers]
# can also use it for strings
name = "Angela"
new_list = [letter for letter in name]
# for all sequences such as range, because it has order
new_list = [n*2 for n in range(1,5)]
# can implement conditions
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_list = [name.upper() for name in names if len(name) > 5]


# dictionary comprehensions
# from list
# new_dict = {new_key:new_value for item in list}
# from dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items()}
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
scores = {name: random.randint(1, 100) for name in names}
passed = {name: score for (name, score) in scores.items() if score > 59}

# iterate over pandas dataframe is like iterating over dictionary
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# loop through dict
for (key, value) in student_dict.items():
    print(value)

import pandas
student_dataframe = pandas.DataFrame(student_dict)
for (key,value) in student_dataframe.items():
    # key gives title of column
    # value gives all values in column
    pass

#looping through dataframe uses specific iter method for all rows
for (index, row) in student_dataframe.iterrows():
    # index gives the index of the row
    # row gives all values for each row which gives a pandas series object
    print(row.student)
