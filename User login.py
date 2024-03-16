class User:
    users = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def register(cls, username, password):
        if not any(user.username == username for user in cls.users):
            cls.users.append(User(username, password))
            return True
        return False
class Product:
    products = []
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    @classmethod
    def add_product(cls, name, price, category, stock):
        cls.products.append(Product(name, price, category, stock))

    @classmethod
    def list_products(cls):
        for product in cls.products:
            print(f"Name: {product.name}, Price: {product.price}, Category: {product.category}, Stock: {product.stock}")

    @classmethod
    def update_stock(cls, name, quantity):
        for product in cls.products:
            if product.name == name:
                product.stock -= quantity
                return True
        return False
    @classmethod
    def login(cls, username, password):
        return any(user.username == username and user.password == password for user in cls.users)
from product import Product
class Order:
    @staticmethod
    def place_order(product_name, quantity):
        for product in Product.products:
            if product.name == product_name and product.stock >= quantity:
                Product.update_stock(product_name, quantity)
                print(f"Order placed!! Complete the payment on delivery.")
                print(f"Bill: {product.price * quantity}")
                return
        print("Order cannot be placed. Check product name or stock availability.")
from user import User
from product import Product
from order import Order

# This is a simplified example. Extend it with a loop and more user-friendly interface as needed.

# Initialize some products
Product.add_product("Laptop", 1000, "Electronics", 10)
Product.add_product("Book", 20, "Books", 100)

# User registration and login flow
username = input("Enter username for registration: ")
password = input("Enter password for registration: ")

if User.register(username, password):
    print("Registration successful!")
else:
    print("Username already exists.")

if User.login(input("Enter username for login: "), input("Enter password for login: ")):
    print("Login successful!")
    Product.list_products()
    product_name = input("Enter product name to order: ")
    quantity = int(input("Enter quantity: "))
    Order.place_order(product_name, quantity)
else:
    print("Login failed. Check your username and password.")


