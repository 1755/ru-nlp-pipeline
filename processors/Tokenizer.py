import inspect
from .tokenizer.BaseLineTokenizer import BaseLineTokenizer
from .tokenizer.ConcreteTokenizerInterface import ConcreteTokenizerInterface
from .Exceptions import InvalidConfigurationError


class Tokenizer(object):
    """
    Bridge class for tokenization language processor -- tokenizer.
    It's propper way to use it instead concreate tokenizator.
    """

    def __init__(self, concrete_tokenizator_class=BaseLineTokenizer):
        """
        Initialize tokenizator

        Args:
            concrete_tokenizator_class: Class of concrete tokenizer 
                        wich would be used for tokenization
        Raises:
            InvalidConfigurationError: When concrete_segmentator_class is not
                    derivavite from ConcreteSegmentatorInterface
        """
        if (not inspect.isclass(concrete_tokenizator_class) or
                not issubclass(concrete_tokenizator_class, ConcreteTokenizerInterface)):
            raise InvalidConfigurationError()

        self._concrete_tokenizer = concrete_tokenizator_class()

    def run(self, sentence):
        """
        Returns list of morphsets coresponded to origin sentence

        Args:
            sentence: Sentence which would be tokenized
        Return:
            List of morpghset corresponded to sentence
        """
        return self._concrete_tokenizer.run(sentence)
