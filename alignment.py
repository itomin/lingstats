from abc import ABC, abstractmethod

class Alignment(ABC):

    def __init__(self, scores):
        self._scores = scores

    @abstractmethod
    def align(self, word1, word2):
        pass


class BeaufilsAlignment(Alignment):
    def align(self, word1, word2):
        return 100