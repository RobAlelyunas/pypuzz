import os
import json
from pypuzz.resources.constants import *
from pypuzz.resources.word_list import WordList

class RelatedWordsDictionary():
    
    related_words_dictionary = {}

    def __init__(self, source=US_SCRABBLE):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        relations_file_name = os.path.join(current_dir,'files', f"{source}_relations.json")
        with open(relations_file_name) as relations_file:
            self.related_words_dictionary = json.load(relations_file)
    
    def get_related(self, word):
        return self.related_words_dictionary[word]
    
    @classmethod
    def generate_relations_file(self, source=US_SCRABBLE, limit_to=None):
        word_list = WordList(source)
        content = word_list.get_word_list()
        words = {word:[] for word in content}
        counter = 0
        for word1 in content:
            print(word1)
            counter = counter + 1
            if limit_to and counter >= limit_to:
                break
            for word2 in word_list.get_words_of_same_length(len(word1)):
                for c in range(0,len(word1)):
                    if word1[c] != word2[c]:
                        if word1[c + 1:] == word2[c + 1:]:
                            words[word1].append(word2)
                        else:
                            break
        current_dir = os.path.dirname(os.path.realpath(__file__))
        relation_dict_name = os.path.join(current_dir,'files', f"generated_{source}_relations.json")
        with open(relation_dict_name, 'w') as relation_dict_file:
            json.dump(words, relation_dict_file, indent=2)
            
if __name__ ==  "__main__":
    RelatedWordsDictionary.generate_relations_file(source=US_SCRABBLE, limit_to=100)