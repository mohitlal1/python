def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_A, fruit)

print(list(filter_object))

dromes = ("demigod", "rewire", "madam", "freer", "tivit", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)