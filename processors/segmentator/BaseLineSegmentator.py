import os
import nltk
from .ConcreteSegmentatorInterface import ConcreteSegmentatorInterface


class BaseLineSegmentator(ConcreteSegmentatorInterface):
    """
    Baseline realization of text segmentator
    """
    _punkt_sentence_tokenizator = None

    _data_directory = os.path.dirname(os.path.realpath(
        __file__)) + '/' + os.path.splitext(os.path.basename(__file__))[0]

    _pickle_name = 'lex.russian.pickle'

    def __init__(self):
        if self._punkt_sentence_tokenizator is None:
            self._punkt_sentence_tokenizator = nltk.data.load(
                self._data_directory + '/' + self._pickle_name)

    def run(self, text):
        return [segment.strip() for segment in self._punkt_sentence_tokenizator.tokenize(text.strip())]
