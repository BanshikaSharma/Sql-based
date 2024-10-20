class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
       
        self.stock -= quantity

    def restock(self, quantity):
       
        self.stock += quantity

    def is_below_threshold(self, threshold):
       
        return self.stock < threshold


def process_orders(products, orders, restock_threshold=10):
   
    restock_alerts = []

    for order in orders:
        product_id, quantity = order
        product = next((p for p in products if p.product_id == product_id), None)

        if product is None:
            print(f"Error: Product ID {product_id} not found.")
            continue

        if product.stock >= quantity:
            product.update_stock(quantity)
            print(f"Processed order for {quantity} of {product.name}. New stock: {product.stock}")
        else:
            print(f"Error: Not enough stock for {product.name}. Current stock: {product.stock}, Requested: {quantity}")

        # Check if the product needs restocking
        if product.is_below_threshold(restock_threshold):
            restock_alerts.append(product)

    return restock_alerts


def restock_items(products, restock_list):
   
    for restock in restock_list:
        product_id, quantity = restock
        product = next((p for p in products if p.product_id == product_id), None)

        if product is None:
            print(f"Error: Product ID {product_id} not found for restocking.")
            continue

        product.restock(quantity)
        print(f"Restocked {quantity} of {product.name}. New stock: {product.stock}")


# Example Usage
if __name__ == "__main__":
   
    product1 = Product(product_id=101, name="Laptop", price=999.99, stock=15)
    product2 = Product(product_id=102, name="Smartphone", price=499.99, stock=5)
    product3 = Product(product_id=103, name="Tablet", price=299.99, stock=20)

    products = [product1, product2, product3]

    # Incoming sales orders
    orders = [
        (101, 3),  # Order for 3 Laptops
        (102, 6),  # Order for 6 Smartphones (should trigger error)
        (103, 5)   # Order for 5 Tablets
    ]

    # Process orders and check for restock alerts
    restock_alerts = process_orders(products, orders)

    # If any products need restocking, restock them
    if restock_alerts:
        print("Restock alerts triggered for the following products:")
        for product in restock_alerts:
            print(f"- {product.name} (Current stock: {product.stock})")

        # Example restock list (you can adjust as needed)
        restock_list = [(102, 10)]  # Restock 10 Smartphones
        restock_items(products, restock_list)
