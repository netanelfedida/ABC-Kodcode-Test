from abc import ABC, abstractmethod
class MyAnimal(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def speak(self):
        pass