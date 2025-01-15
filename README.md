# Distributed System Simulation with Concurrent Database Operations

This project showcases a simulation of a distributed system where distinct datasets (`Users`, `Orders`, and `Products`) are stored in independent SQLite databases. The application leverages multi-threading to perform concurrent insertions, demonstrating concurrency and thread-safe database operations in a distributed environment.

This implementation is ideal for understanding the principles of distributed systems, database segregation, and multithreaded programming in Python.

---

## Key Features

### **1. Modular Data Management**
- **Users**: Captures user details with fields such as `id`, `name`, and `email`. Data is stored in `users.db`.
- **Products**: Stores information about products with fields `id`, `name`, and `price`. Data is stored in `products.db`.
- **Orders**: Records customer orders, linking users and products with fields such as `id`, `user_id`, `product_id`, and `quantity`. Data is stored in `orders.db`.

### **2. Concurrency with Multithreading**
- The system simulates simultaneous insertions into the databases using Python's `threading` library, ensuring that each database receives data concurrently.
- By utilizing threads, the system mimics a real-world distributed environment where multiple operations can occur in parallel.

### **3. Application-Level Validation**
- The project ensures data integrity by validating entries before insertion, preventing invalid or inconsistent data from being saved.
- Any data errors (such as negative values in the `quantity` field or products with negative prices) are handled and logged.

### **4. Independent Databases**
- Each model (`Users`, `Orders`, and `Products`) is stored in a separate SQLite database, demonstrating how distributed systems can store different types of data in different databases for better scalability and organization.

### **5. Scalable Architecture**
- The project is designed to be scalable, allowing the integration of more databases and models in the future, as well as expanding the concurrency model to handle larger datasets efficiently.

---

## How It Works

1. **Database Models**: Three models (`User`, `Product`, `Order`) are defined, with each model stored in its respective database (`users.db`, `products.db`, and `orders.db`).
2. **Concurrent Insertions**: Multiple threads are created to insert data into the databases concurrently. Each thread handles the insertion of data for one model.
3. **Thread Safety**: Threads are synchronized to avoid race conditions and ensure data consistency across multiple databases.

---

## Data

### Users Table (users.db)
| id  | name   | email               |
|-----|--------|---------------------|
| 1   | Alice  | alice@example.com    |
| 2   | Bob    | bob@example.com      |
| 3   | Charlie| charlie@example.com  |
| 4   | David  | david@example.com    |
| 5   | Eve    | eve@example.com      |
| 6   | Frank  | frank@example.com    |
| 7   | Grace  | grace@example.com    |
| 8   | Alice  | alice@example.com    |
| 9   | Henry  | henry@example.com    |
| 10  | Jane   | jane@example.com     |

### Products Table (products.db)
| id  | name        | price |
|-----|-------------|-------|
| 1   | Laptop      | 1000  |
| 2   | Smartphone  | 700   |
| 3   | Headphones  | 150   |
| 4   | Monitor     | 300   |
| 5   | Keyboard    | 50    |
| 6   | Mouse       | 30    |
| 7   | Laptop      | 1000  |
| 8   | Smartwatch  | 250   |
| 9   | Gaming Chair| 500   |
| 10  | Earbuds     | -50   |

### Orders Table (orders.db)
| id  | user_id | product_id | quantity |
|-----|---------|------------|----------|
| 1   | 1       | 1          | 2        |
| 2   | 2       | 2          | 1        |
| 3   | 3       | 3          | 5        |
| 4   | 4       | 4          | 1        |
| 5   | 5       | 5          | 3        |
| 6   | 6       | 6          | 4        |
| 7   | 7       | 7          | 2        |
| 8   | 8       | 8          | 0        |
| 9   | 9       | 1          | -1       |
| 10  | 10      | 11         | 2        |

---

## Requirements

- Python 3.x
- Django 3.x or higher
- SQLite
