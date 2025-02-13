from PaymentProcessor import PaymentProcessor

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        print(f"{amount} was paid by credit card")