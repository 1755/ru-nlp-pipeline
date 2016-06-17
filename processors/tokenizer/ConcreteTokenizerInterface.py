class ConcreteTokenizerInterface:
    """
    Interface for all concrete tokenizers
    """

    def run(self, sentence):
        raise NotImplementedError
