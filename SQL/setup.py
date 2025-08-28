import sqlite3
import pandas as pd

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT,
    address TEXT,
    phone TEXT
)
""")

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    user_id TEXT,
    product_id INTEGER,
    purchase_date TEXT,
    amount INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO customers (name, age, email, address, phone) VALUES (?, ?, ?, ?, ?)", 
               ("Alice", 30, "alice@example.com", "123 Main St", "555-1234"))
cursor.execute("INSERT INTO customers (name, age, email, address, phone) VALUES (?, ?, ?, ?, ?)", 
               ("Bob", 25, "bob@example.com", "456 Oak Ave", "555-5678"))
cursor.execute("INSERT INTO customers (name, age, email, address, phone) VALUES (?, ?, ?, ?, ?)", 
               ("Jack", 20, "jack@example.com", "789 Pine Rd", "555-8765"))
cursor.execute("INSERT INTO customers (name, age, email, address, phone) VALUES (?, ?, ?, ?, ?)", 
               ("Phil", 45, "phil@example.com", "321 Maple St", "555-4321"))
cursor.execute("INSERT INTO customers (name, age, email, address, phone) VALUES (?, ?, ?, ?, ?)", 
               ("Jess", 32, "jess@example.com", "654 Elm St", "555-2468"))
cursor.execute("INSERT INTO customers (name, age, email, address, phone) VALUES (?, ?, ?, ?, ?)", 
               ("Bob", 35, "bob2@example.com", "987 Cedar Ave", "555-1357"))

cursor.execute("INSERT INTO transactions (user_id, product_id, purchase_date, amount) VALUES (?, ?, ?, ?)", 
               ("Alice", 101, "2023-01-15", 250))
cursor.execute("INSERT INTO transactions (user_id, product_id, purchase_date, amount) VALUES (?, ?, ?, ?)", 
               ("Bob", 102, "2023-02-20", 150))
cursor.execute("INSERT INTO transactions (user_id, product_id, purchase_date, amount) VALUES (?, ?, ?, ?)", 
               ("Jack", 103, "2023-03-10", 300))
cursor.execute("INSERT INTO transactions (user_id, product_id, purchase_date, amount) VALUES (?, ?, ?, ?)", 
               ("Phil", 104, "2023-04-05", 400))


# Commit & close
conn.commit()
conn.close()