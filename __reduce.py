
from functools import reduce



letters = ["H","E","L","L","O"]

word = reduce(lambda x,y:x+y,letters)
print(word)

# output = HELLO





