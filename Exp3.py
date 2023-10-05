# create string type variables

name = "Python"
print(name)

message = "I love Python."
print(message)
greet = 'hello'
print(greet[1])
greet = 'hello'
print(greet[-4])
greet = 'Hello'
print(greet[1:4])
message = 'Hola Amigos'
print(message)
message = 'Hola Amigos'
# assign new string to message variable
message = 'Hello Friends'
print(message); # prints "Hello Friends"
# multiline string
message = """
Never gonna give you up
Never gonna let you down
"""
print(message)
str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)
greet = "Hello, "
name = "Jack"
# using + operator
result = greet + name
print(result)
greet = 'Hello'
# count length of greet string
print(len(greet))
# escape double quotes
example = "He said, \"What's there?\""
# escape single quotes
example = 'He said, "What\'s there?"'
print(example)
name = 'Cathy'
country = 'UK'
print(f'{name} is from {country}')