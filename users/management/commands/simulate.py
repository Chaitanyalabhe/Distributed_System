import threading
from django.core.management.base import BaseCommand
from users.models import User
from products.models import Product
from orders.models import Order

class Command(BaseCommand):
    help = "Simulate simultaneous insertions into multiple databases"

    def insert_users(self):
        users_data = [
            (1, 'Alice', 'alice@example.com'),
            (2, 'Bob', 'bob@example.com'),
            (3, 'Charlie', 'charlie@example.com'),
            (4, 'David', 'david@example.com'),
            (5, 'Eve', 'eve@example.com'),
            (6, 'Frank', 'frank@example.com'),
            (7, 'Grace', 'grace@example.com'),
            (8, 'Alice', 'alice@example.com'),
            (9, 'Henry', 'henry@example.com'),
            (10, 'Jane', 'jane@example.com'),
        ]
        for user in users_data:
            try:
                User.objects.using('users_db').create(id=user[0], name=user[1], email=user[2])
                self.stdout.write(f"Inserted User: {user}")
            except Exception as e:
                self.stderr.write(f"Error inserting User {user}: {e}")

    def insert_products(self):
        products_data = [
            (1, 'Laptop', 1000.00),
            (2, 'Smartphone', 700.00),
            (3, 'Headphones', 150.00),
            (4, 'Monitor', 300.00),
            (5, 'Keyboard', 50.00),
            (6, 'Mouse', 30.00),
            (7, 'Laptop', 1000.00),
            (8, 'Smartwatch', 250.00),
            (9, 'Gaming Chair', 500.00),
            (10, 'Earbuds', -50.00),
        ]
        for product in products_data:
            try:
                if product[2] < 0:
                    raise ValueError("Price cannot be negative.")
                Product.objects.using('products_db').create(id=product[0], name=product[1], price=product[2])
                self.stdout.write(f"Inserted Product: {product}")
            except Exception as e:
                self.stderr.write(f"Error inserting Product {product}: {e}")

    def insert_orders(self):
        orders_data = [
            (1, 1, 1, 2),
            (2, 2, 2, 1),
            (3, 3, 3, 5),
            (4, 4, 4, 1),
            (5, 5, 5, 3),
            (6, 6, 6, 4),
            (7, 7, 7, 2),
            (8, 8, 8, 0),
            (9, 9, 1, -1),
            (10, 10, 11, 2),
        ]
        for order in orders_data:
            try:
                if order[3] <= 0:
                    raise ValueError("Quantity must be positive.")
                Order.objects.using('orders_db').create(id=order[0], user_id=order[1], product_id=order[2], quantity=order[3])
                self.stdout.write(f"Inserted Order: {order}")
            except Exception as e:
                self.stderr.write(f"Error inserting Order {order}: {e}")

    def handle(self, *args, **kwargs):
        threads = []

        # Create threads for simultaneous insertions
        t1 = threading.Thread(target=self.insert_users)
        t2 = threading.Thread(target=self.insert_products)
        t3 = threading.Thread(target=self.insert_orders)

        threads.append(t1)
        threads.append(t2)
        threads.append(t3)

        # Start the threads
        for t in threads:
            t.start()

        # Wait for all threads to complete
        for t in threads:
            t.join()

        self.stdout.write(self.style.SUCCESS("Simultaneous insertions completed!"))