from pprint import pprint
from time import time

message = input("Please tye your sentence: ")

counter = {}
for letter in message:
    counter.setdefault(letter, 0)
    counter[letter] = counter[letter] + 1

pprint(counter)