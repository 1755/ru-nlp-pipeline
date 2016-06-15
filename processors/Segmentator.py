import inspect
from .segmentator.BaseLineSegmentator import BaseLineSegmentator
from .segmentator.ConcreteSegmentatorInterface import ConcreteSegmentatorInterface


class InvalidConfigurationError(ValueError):
    """
    Exception wich raised on wrong segmentator configuration
    """
    pass


class Segmentator(object):
    """
    Bridge class for segmentation language processor -- segmentator.
    It's propper way to use it instead concreate segmentator.

    >>> segmentator = Segmentator()
    >>> segmentator.run('Привет. Это два предложения.')
    ['Привет.', 'Это два предложения']

    """

    def __init__(self, concrete_segmentator_class=BaseLineSegmentator):
        """
        Initialize segmentator

        Args:
            concrete_segmentator_class: Class of concrete segmentator 
                        wich would be used for segmentation
        Raises:
            InvalidConfigurationError: When concrete_segmentator_class is not
                    derivavite from ConcreteSegmentatorInterface
        """
        if (not inspect.isclass(concrete_segmentator_class) or
                not issubclass(concrete_segmentator_class, ConcreteSegmentatorInterface)):
            raise InvalidConfigurationError()

        self._concrete_segmentator = concrete_segmentator_class()

    def run(self, plaintext):
        """
        Returns list of sentences coresponded to origin text

        Args:
            plaintext: Text which would be segmetated
        Return:
            List of sentences corresponded to plaintext
        """
        return self._concrete_segmentator.run(plaintext)
