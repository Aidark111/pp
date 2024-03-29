# Create a generator that generates the squares of numbers up to some number N.
def generate_squares(N):
    for i in range(N):
        yield i ** 2

N = 11
for square in generate_squares(N):
    print(square)


#Write a program using generator to print the even numbers 
#between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even_nums = even_numbers(n)
print(",".join(map(str, even_nums)))


#  Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divisible_by_3_and_4(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
start = 0
end = 20
for num in divisible_by_3_and_4(start, end):
    print(num)


# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = 5
b = 10
for square in squares(a, b):
    print(square)


# Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = 5
for num in countdown(n):
    print(num)


