import sys

# test against pypuzz src tree
sys.path.append('../pypuzz')
from pypuzz.resources import WordList
from pypuzz.resources import US_SCRABBLE
from pypuzz.anagrams import Anagrams

def test_can_create_a_random_n_letter_anagram():
    word_list = WordList(US_SCRABBLE)
    word = word_list.get_random_word(7)
    anagrams = Anagrams()
    scrambled = anagrams.scramble(word)
    print(f"{word}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nscrambled word ===== {scrambled}")
    #solutions = anagrams.unscramble(scrambled)
    #assert word in solutions