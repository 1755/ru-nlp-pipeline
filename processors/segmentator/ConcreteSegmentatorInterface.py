class ConcreteSegmentatorInterface:
    """
    Interface for all concrete segmentators 
    """

    def run(self, plaintext):
        raise NotImplementedError
