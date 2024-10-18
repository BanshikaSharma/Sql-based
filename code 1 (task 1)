class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []  # List to hold user's orders

    def create_order(self, order):
        self.orders.append(order)

    def view_orders(self):
        return self.orders

    def get_order_by_id(self, order_id):
        # Retrieve an order by its ID
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def cancel_order(self, order_id):
        # Cancel an order by its ID
        order = self.get_order_by_id(order_id)
        if order and order.status == 'pending':
            order.status = 'canceled'
            return True
        return False


class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock -= quantity

    def restock(self, quantity):
        # Add stock back to the product
        self.stock += quantity

    def get_details(self):
        # Return product details
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }


class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.products = []  # List to hold products in the order
        self.status = 'pending'

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.products.append((product, quantity))
            product.update_stock(quantity)
        else:
            print("Not enough stock available.")

    def make_payment(self, amount):
        payment = Payment(order=self, amount=amount)
        payment.process_payment()
        self.status = 'completed'

    def get_order_summary(self):
        # Return a summary of the order
        return {
            'order_id': self.order_id,
            'user': self.user.name,
            'products': [(product.name, quantity) for product, quantity in self.products],
            'status': self.status
        }

    def cancel_order(self):
        # Cancel the order if it is still pending
        if self.status == 'pending':
            self.status = 'canceled'
            return True
        return False


class OrderProduct:
    def __init__(self, order, product, quantity):
        self.order = order
        self.product = product
        self.quantity = quantity


class Payment:
    def __init__(self, order, amount):
        self.payment_id = id(self)  # Unique ID for payment
        self.order = order
        self.amount = amount
        self.status = 'pending'

    def process_payment(self):
        # Simulate payment processing
        self.status = 'completed'
        print(f"Payment of {self.amount} for order {self.order.order_id} processed.")

    def refund(self):
        # Simulate refund process
        if self.status == 'completed':
            self.status = 'refunded'
            print(f"Refund for payment {self.payment_id} processed.")
            return True
        return False

    def get_payment_details(self):
        # Return payment details
        return {
            'payment_id': self.payment_id,
            'order_id': self.order.order_id,
            'amount': self.amount,
            'status': self.status
        }
