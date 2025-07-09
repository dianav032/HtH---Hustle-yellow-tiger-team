# Debugging Activity Diana Veliz

# 1 Corrected: Division by zero
x = 10
y = 2
result = x / y
print("Result:", result)

# 2 Corrected: Index Error out of range
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i+0])

   # 3 Corrected: Missing colon
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

# 4 Corrected: Missing colon
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

# 5 Corrected: Missing colon
for i in range(5):
   print(i)

   # 6 Corrected: Missing +
def greet(name):
   return "Hello, " + name

print(greet("Alice"))

# 7 Corrected: Missing indentation
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)

# 8 Corrected: Counted up instead of down
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))

# 9 Corrected: Logical error in the condition
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
   print("Hello, " + name)
else:
   print("Hello, stranger!")

# 10 Corrected:
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2
print(divide_numbers(num1, num2))








