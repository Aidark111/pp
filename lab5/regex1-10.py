import re

with open("lab5/row.txt", "r") as file:
    contents = file.read()

# 1. Match a string with 'a' followed by zero or more 'b's:
pattern = re.compile(r'ab*')
print([bool(pattern.match(line)) for line in contents.split('\n')])

# 2. Match a string with 'a' followed by two to three 'b's:
pattern = re.compile(r'ab{2,3}')
print([bool(pattern.match(line)) for line in contents.split('\n')])

# 3. Find sequences of lowercase letters joined with an underscore:
pattern = re.compile(r'[a-z]+_[a-z]+')
print(pattern.findall(contents))

# 4. Find sequences of one uppercase letter followed by lowercase letters:
pattern = re.compile(r'[A-Z][a-z]+')
print(pattern.findall(contents))

# 5. Match a string with 'a' followed by anything, ending in 'b':
pattern = re.compile(r'a.*b$')
print([bool(pattern.match(line)) for line in contents.split('\n')])

# 6. Replace all occurrences of space, comma, or dot with a colon:
print(re.sub(r'[ ,.]', ':', contents))

# 7. Convert snake case string to camel case string:
print(''.join(word.capitalize() for word in "hello_world".split('_')))
print(''.join(word.capitalize() for word in "my_snake_case_string".split('_')))

# 8. Split a string at uppercase letters:
print(re.findall(r'[A-Z][a-z]*', contents))

# 9. Insert spaces between words starting with capital letters:
print(re.sub(r'([a-z])([A-Z])', r'\1 \2', contents))

# 10. Convert a given camel case string to snake case:
print(re.sub(r'(?<!^)(?=[A-Z])', '_', "HelloWorld").lower())
print(re.sub(r'(?<!^)(?=[A-Z])', '_', "MyCamelCaseString").lower())
