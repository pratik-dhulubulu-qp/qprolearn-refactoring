class Customer:
    def __init__(self, name: str, customer_type: str):
        self.name = name
        self.customer_type = customer_type  # "Regular", "Premium", "VIP"
        self.discount = 0
        self.set_discount()

    def set_discount(self):
        pass


class VIP_Customer(Customer):
    def __init__(self, name: str):
        super().__init__(name, "VIP")
    def set_discount(self):
        self.discount = 0.2


class Premium_Customer(Customer):
    def __init__(self, name: str):
        super().__init__(name, "Premium")

    def set_discount(self):
        self.discount = 0.1


class Regular_Customer(Customer):
    def __init__(self, name: str):
        super().__init__(name, "Regular")

    def set_discount(self):
        self.discount = 0.05