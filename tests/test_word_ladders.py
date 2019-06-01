import sys
# test against pypuzz src tree
sys.path.append('../pypuzz')
from pypuzz.word_ladders import WordLadders

def test_finds_spring_from_sprint():
    word_graph = WordLadders()
    ladders = word_graph.get_ladders('sprint', 'spring')
    assert len(ladders) > 0

def test_finds_cake_from_time():
    word_graph = WordLadders()
    ladders = word_graph.get_ladders('time', 'cake')
    assert len(ladders) > 0

def test_finds_charge_from_comedo():
    word_graph = WordLadders()
    ladders = word_graph.get_ladders('comedo', 'charge')
    assert len(ladders) > 0

def test_never_finds_absolute_from_bicycles():
    word_graph = WordLadders()
    ladders = word_graph.get_ladders('bicycles', 'absolute')
    assert len(ladders) == 0