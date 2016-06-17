import unittest
from processors.Tokenizer import Tokenizer


class TokenizerCorectness(unittest.TestCase):
    simple_cases = (
        ('Мама мыла раму.', [
            ('Мама', 'Ncfsny', 'мама'),
            ('мыла', 'Vmis-sfa-e', 'мыть'),
            ('раму', 'Ncfsan', 'рама'),
            ('.', 'SENT', '.'),
        ]),
        ('Он видел их семью своими глазами.', [
            ('Он', 'P-3msnn', 'он'),
            ('видел', 'Vmis-sma-e', 'видеть'),
            ('их', 'P-----a', 'их'),
            ('семью', 'Ncfsan', 'семья'),
            ('своими', 'P---pia', 'свой'),
            ('глазами', 'Ncmpin', 'глаз'),
            ('.', 'SENT', '.'),

        ])
    )

    def test_simple_cases(self):
        """
        Run simple test cases of tokenizer
        """
        tokenizer = Tokenizer()
        for sentence, list_of_morphset in self.simple_cases:
            given_list = tokenizer.run(sentence)
            self.assertEqual(list_of_morphset, given_list)
