import os
import treetaggerwrapper
from nltk import RegexpTokenizer
from .ConcreteTokenizerInterface import ConcreteTokenizerInterface


class BaseLineTokenizer(ConcreteTokenizerInterface):
    """
    Baseline realization of tokenizer
    @todo: add documentaion for tagging
    """
    _this_file_name = os.path.splitext(os.path.basename(__file__))[0]
    _current_directory = os.path.dirname(os.path.realpath(__file__))

    _word_expression = r'''[а-яА-яa-zA-z0-9ЎўҚқҒғҲҳ\'‘’\-–—/.]+'''
    _symbol_expression = r'''[,-–—*:;«»№\)\(]{1}'''
    _tokenizer = RegexpTokenizer(r'%s|%s' % (
        _word_expression,
        _symbol_expression
    ))

    _treetagger_diretctory = _current_directory + '/' + _this_file_name
    _treetagger_par_file = _treetagger_diretctory + '/lib/russian-utf8.par'
    _tagger = treetaggerwrapper.TreeTagger(TAGLANG='ru',
                                           TAGDIR=_treetagger_diretctory,
                                           TAGPARFILE=_treetagger_par_file)

    def run(self, sentence):
        words = self._tokenizer.tokenize(sentence)

        # hack for trailing dot
        if words[-1][-1] == '.':
            words[-1] = words[-1][:-1]
            words.append('.')

        tags = self._tagger.tag_text("\n".join(words), tagonly=True)
        return [self._str2triplet(tagged_string) for tagged_string in tags]

    def _str2triplet(self, string):
        triplet = tuple(string.split('\t'))
        if len(triplet) < 3:
            raise AttributeError
        return triplet
