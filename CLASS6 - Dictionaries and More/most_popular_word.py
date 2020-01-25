
def most_popular_word(words):
    word_dictionary = {}
    for item in words:
        if item in word_dictionary: #this only checks the keys, not the values
            word_dictionary[item] += 1
        else:
            word_dictionary[item] = 1
    return word_dictionary

# {} refers to a dictionary
# [] refers to a list!
# () refers to a function or a tuple

words = ['hello', 'water', 'hello', 'mike', 'ga']
print(most_popular_word(words))