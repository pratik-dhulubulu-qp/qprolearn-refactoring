from Customer import VIP_Customer, Premium_Customer, Regular_Customer
from Order import Order

class OrderManagementSystem:
    @staticmethod
    def main():
        customer = VIP_Customer("John Doe")
        order = Order(customer)

        order.add_item("Laptop", 1000)
        order.add_item("Mouse", 50)
        order.add_item("Keyboard", 80)

        order.print_order()

        OrderManagementSystem.generate_invoice(order)

    @staticmethod
    def generate_invoice(order: Order):
        print("Generating Invoice...")
        print(f"Customer: {order.customer.name}")
        print(f"Total: ${order._total_price:.2f}")
        print(f"Discounted Total: ${order._discounted_price:.2f}")
        print(f"Items: {', '.join(order._items)}")
        print("Thank you for shopping with us!")


# Run the order management system
OrderManagementSystem.main()
