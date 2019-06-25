import abc
#Abstract Base Classes

class Heuristic(abc.ABC):
    @abc.abstractmethod
    def calculate(self):
        pass