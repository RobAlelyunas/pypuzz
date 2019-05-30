import sys
from word_ladders.WordGraph import WordGraph

def test_sprint_and_spring_are_1_distance_apart():
    word_graph = WordGraph()
    related = word_graph.get_related('sprint')
    assert 'spring' in related

def test_sprint_and_string_are_not_1_distance_apart():
    word_graph = WordGraph()
    related = word_graph.get_related('sprint')
    assert 'string' not in related