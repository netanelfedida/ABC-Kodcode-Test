from PaymentProcessor import PaymentProcessor

class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        print(f"{amount} was paid by PayPal")