# Lab 3

# Task 1: Working with Strings
food = 'chicken tacos'
print(food[0:3])
print(food[-3:-1])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

# task 2: Working with Lists
number_list = [1, 2, 43, -9, 4, 23]
number_list.append(26)
print(number_list)
number_list.insert(3, 897)
print(number_list)
number_list.pop()
print(number_list)
remove_element = number_list.pop(2)
print(remove_element)
print(number_list)
number_list.sort()

# †ask 3: Working with Dictionaries
books = {"Gillian Flynn" : "Gone Girl",
         "Stephen King" : "Billy Summers",
         "Clyde Phillips" : "Dexter: New Blood", 
         "S. E. Hinton" : "The Outsiders"}
print(books.keys())
print(books.values())
books["Clyde Phillips"] = "Dexter: New Blood"
print(books)
books["Stephen King"] = "Billy Summers"
print(books)
books["Gillian Flynn"] = "Gone Girl"
print(books)
del books["Clyde Phillips"]
print(books)
print(books["S. E. Hinton"])
print(len(books))








