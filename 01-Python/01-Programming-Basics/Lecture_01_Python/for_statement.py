### FOR STATEMENT WITH LISTS ###
words = ['cat', 'wolf', 'beetle']

# Loop through the words in the list "words":
for word in words:
    # word is a placeholder which stores a new value (word) for each iteration
    # prints out uppercased word
    print(word.upper())

# LIST COMPREHENSION
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

# LIST COMPREHENSION WITH IF-STATEMEN
uppercase_words = [word.upper() for word in words if word[0] == "C"]
print(uppercase_words)

# LOOP OVER INDEX AND VALUE
for index, word in enumerate(words):
    print(index, word)

### FOR STATEMENT WITH DICTIONARIES ###
instruments = {'paul': 'bass', 'ringo': 'drums'}

for beatle, instrument in instruments.items():
    # instruments.items() returns the key-value pairs in tuples -> we need two placeholders
    print(f'{beatle.capitalize()} plays the {instrument}')

# instruments.values() and instruments.keys() can also be used!
