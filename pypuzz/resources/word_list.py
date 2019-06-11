import os
import random
from pypuzz.resources.constants import US_SCRABBLE

class WordList():
    
    word_list = {}

    def __init__(self, source=US_SCRABBLE):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        word_list_file_name = os.path.join(current_dir,'files',f"{source}.txt")
        with open(word_list_file_name, encoding='utf-8') as word_list_file:
            self.content = word_list_file.readlines()
        self.content = [x.strip() for x in self.content]
        self.words_by_len = {}
        for word in self.content:
            try:
                elem = self.words_by_len[len(word)]
            except KeyError:
                elem = []
                self.words_by_len[len(word)] = elem
            elem.append(word)

    def get_word_list(self):
        return self.content

    def get_words_of_same_length(self, length):
        return self.words_by_len[length]

    def get_random_word(self, length):
        words = self.get_words_of_same_length(length)
        index = random.randint(0, len(words))
        return words[index]
