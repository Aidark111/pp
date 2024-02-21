def grams_to_ounces(grams):
    ounces = grams * 28.3495231
    return ounces
a = int(input("Enter the weight in grams: "))
print(grams_to_ounces(a))