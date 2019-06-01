import random

class Anagrams():

    def scramble(self, word):
        word_list = list(word)
        random.shuffle(word_list)
        return "".join(word_list)
