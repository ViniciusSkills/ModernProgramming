from abc import ABC, abstractmethod


class IFly(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass


class IJump(ABC):
    @abstractmethod
    def jump(self):
        pass


class IClimb(ABC):
    @abstractmethod
    def climb(self):
        pass

class IRun(ABC):
    @abstractmethod
    def run(self):
        pass

class IForce(ABC):
    @abstractmethod
    def force(self):
        pass

class IPix(ABC):
    @abstractmethod
    def pay(self):
        pass

class ICreditCard(ABC):
    @abstractmethod
    def pay(self):
        pass

class IDebitCard(ABC):
    @abstractmethod
    def pay(self):
        pass
