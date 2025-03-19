class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        self.strategy.pay(amount)
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Bitcoin.")
        
if __name__ == "__main__":
    # Create strategies
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    bitcoin = BitcoinPayment()

    # Context using Credit Card
    context = PaymentContext(credit_card)
    context.execute_payment(100)

    # Switch to PayPal
    context.set_strategy(paypal)
    context.execute_payment(200)

    # Switch to Bitcoin
    context.set_strategy(bitcoin)
    context.execute_payment(300)
