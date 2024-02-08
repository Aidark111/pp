def print_permutations(string):
    from itertools import permutations
    perms = [''.join(p) for p in permutations(string)]
    for perm in perms:
        print(perm)
string = input("Enter a string: ")
print("Permutations of the string:")
print_permutations(string)