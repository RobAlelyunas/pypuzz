import sys
from word_ladders.WordGraph import WordGraph

def test_sprint_and_spring_are_1_distance_apart():
    print('aaaava')
    word_graph = WordGraph()
    related = word_graph.get_related('sprint')
    assert 'spring' in related

def test_sprint_and_string_are_not_1_distance_apart():
    word_graph = WordGraph()
    related = word_graph.get_related('sprint')
    assert 'string' not in related

def test_finds_spring_from_sprint():
    word_graph = WordGraph()
    ladders = word_graph.get_ladders('sprint', 'spring')
    print(ladders)
    assert len(ladders) > 0

def test_finds_cake_from_time():
    word_graph = WordGraph()
    ladders = word_graph.get_ladders('time', 'cake')
    print(ladders)
    assert len(ladders) > 0

def test_finds_charge_from_comedo():
    word_graph = WordGraph()
    ladders = word_graph.get_ladders('comedo', 'charge')
    print(ladders)
    assert len(ladders) > 0

def test_never_finds_absolute_from_bicycles():
    word_graph = WordGraph()
    ladders = word_graph.get_ladders('bicycles', 'absolute')
    print(ladders)
    assert len(ladders) == 0