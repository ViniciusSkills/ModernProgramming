from abc import ABC, abstractmethod
from interfaces import IPix, ICreditCard, IDebitCard


class Payment(ABC):
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} makes the payment: {self.make_payment()}"

    @abstractmethod
    def make_payment(self):
        pass


class Pix(Payment, IPix):
    def __init__(self, name):
        super().__init__(name)

    def pay(self):
        return "Pix payment was successful."

    def make_payment(self):
        return self.pay()


class CreditCard(Payment, ICreditCard):
    def __init__(self, name):
        super().__init__(name)

    def pay(self):
        return "Credit card payment was successful."

    def make_payment(self):
        return self.pay()


class DebitCard(Payment, IDebitCard):
    def __init__(self, name):
        super().__init__(name)

    def pay(self):
        return "Debit card payment was successful."

    def make_payment(self):
        return self.pay()