import os
import json
import pypuzz.resources as resources

class WordLadders():
    def __init__(self):
        self.relations = resources.RelatedWordsDictionary(source=resources.US_SCRABBLE)

    def get_ladders(self, word1, word2):
        visited_words = set()
        ladders = [(word1,)]
        next_ladders = []
        solutions = []
        while not solutions and ladders:
            for ladder in ladders:
                last = ladder[-1]
                visited_words.add(last)
                for related in self.relations.get_related(last):
                    if related in visited_words:
                        continue
                    elif (related == word2):
                        solutions.append(ladder + (related,))
                    else:
                        next_ladders.append(ladder + (related,))
            ladders = next_ladders
            next_ladders = []
        return solutions

