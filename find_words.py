"""
Write a function find_words that takes a string input and finds all English-language words between 4 and 10 characters that 
    input letters can form.
For example, find_words('bna') should return 'nana', 'anna', and 'banana'.

Bonuses:
Input strings should not contain spaces, symbols, or diacritics. Write a function that checks that each input string meets 
    these conditions and raises an exception if not.
Make the word-length parameters adjustable through keyword arguments. If you call find_words('bna'), it should default to 
    min and max lengths of 4 and 10, respectively. However, you should also be able to specify new lengths, 
    eg. find_words('bna', min_length=2, max_length=20).
Make find_words a generator function. This means that find_words should return an iterator that can be unpacked when you 
    are ready to use its contents. This may require some googling.
"""

import nltk, re

nltk.download('words')
english_language_words = nltk.corpus.words.words()

def find_words(input, min_length=4, max_length=10):
    
    def check_input(input):
        if not re.match("^[a-z]+$", input):
            raise Exception('Input strings should not contain uppercase letters, numbers, spaces, symbols, or diacritics.')

    check_input(input)

    for word in english_language_words:
        if all(i in input for i in word) and len(word) >= min_length and len(word) <= max_length:
            yield word

words = find_words('bna')
print([w for w in words])