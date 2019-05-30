import os
import json

class WordGraph():
    def __init__(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        relations_file_name = os.path.join(current_dir,'resources','relations.json')
        with open(relations_file_name) as relations_file:
            self.words = json.load(relations_file)

    def get_related(self, word):
        return self.words[word]

'''
This generates a json structure that shows for each word all the words that are one character away.  It takes about an hour
to run currently so only needs to be done when a new word list is used
'''
def generate_relations_file():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    word_list_file_name = os.path.join(current_dir,'resources','word_list_twl06.txt')
    with open(word_list_file_name) as word_list_file:
        content = word_list_file.readlines()
    content = [x.strip() for x in content]
    words = {word:[] for word in content}
    words_by_len = {}
    for word in content:
        try:
            elem = words_by_len[len(word)]
        except KeyError:
            elem = []
            words_by_len[len(word)] = elem
        elem.append(word)
    counter = 0
    for word1 in content:
        print(word1)
        counter = counter + 1
        if (counter > 200):
            break
        for word2 in words_by_len[len(word1)]:
            for c in range(0,len(word1)):
                if word1[c] != word2[c]:
                    if word1[c + 1:] == word2[c + 1:]:
                        words[word1].append(word2)
                    else:
                        break
    relation_dict_name = os.path.join(current_dir,'resources','generated_relations.json')
    with open(relation_dict_name, 'w') as relation_dict_file:
        json.dump(words, relation_dict_file, indent=2)
        
if __name__ ==  "__main__":
    generate_relations_file()
