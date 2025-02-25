from Customer import Customer


class Order:
    def __init__(self, customer: Customer):
        self.customer = customer
        self._items = []
        self._prices = []
        self._total_price = 0
        self._discounted_price = 0

    def add_item(self, item: str, price: float):
        self._items.append(item)
        self._prices.append(price)
        self.calculate_total()

    def calculate_total(self):
        self._total_price = sum(self._prices)
        self.apply_discount()

    def apply_discount(self):
        self._discounted_price = self._total_price - (self._total_price * self.customer.discount)

    def print_order(self):
        print(f"Customer: {self.customer.name}")
        print(f"Items: {', '.join(self._items)}")
        print(f"Total Price: ${self._total_price:.2f}")
        print(f"Discounted Price: ${self._discounted_price:.2f}")