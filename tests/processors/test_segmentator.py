import unittest
from processors.Segmentator import Segmentator, InvalidConfigurationError


class SegmentatorInitialization(unittest.TestCase):
    def test_initialization(self):
        self.assertRaises(
            InvalidConfigurationError, Segmentator, None
        )

        self.assertRaises(
            InvalidConfigurationError, Segmentator, 123
        )

        self.assertRaises(
            InvalidConfigurationError, Segmentator, Segmentator
        )


class SegmentatorCorectness(unittest.TestCase):
    simple_cases = (
        ('Привет, как дела? Вроде бы хорошо.',
            ['Привет, как дела?', 'Вроде бы хорошо.']),
        ('Это был кот Вася. Он сидел на крыльце возле дома.',
            ['Это был кот Вася.', 'Он сидел на крыльце возле дома.'])
    )

    def test_simple_cases(self):
        """
        Run simple test cases of segmentator
        """
        segmentator = Segmentator()
        for plaintext, list_of_sentences in self.simple_cases:
            given_list = segmentator.run(plaintext)
            self.assertEqual(list_of_sentences, given_list)
