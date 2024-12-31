from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os

# Delete the existing database file
if os.path.exists('ecommerce.db'):
    os.remove('ecommerce.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email_address = Column(String, unique=True, nullable=False)  # Renamed from 'email'
    password = Column(String, nullable=False)

    # One-to-many relationship with orders
    orders = relationship('Order', back_populates='user')

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    quality = Column(String)  # New attribute added

    # One-to-many relationship with order_items
    order_items = relationship('OrderItem', back_populates='product')

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)  # e.g., 'pending', 'shipped', 'delivered'

    # Many-to-one relationship with users
    user = relationship('User', back_populates='orders')

    # One-to-many relationship with order_items
    order_items = relationship('OrderItem', back_populates='order')

class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)  # Store the price at the time of order

    # Many-to-one relationship with orders
    order = relationship('Order', back_populates='order_items')

    # Many-to-one relationship with products
    product = relationship('Product', back_populates='order_items')

# Create an SQLite database
engine = create_engine('sqlite:///ecommerce.db', echo=True)

# Create tables
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Example users
users = [
    User(username='john_doe', email_address='john@example.com', password='password123'),
    User(username='jane_smith', email_address='jane@example.com', password='securepass'),
    User(username='alice_jones', email_address='alice@example.com', password='mypassword')
]

# Add users to the session
session.add_all(users)
session.commit()

# Example products
products = [
    Product(name='Laptop', description='A high-performance laptop', price=999.99, stock_quantity=10, quality='High'),
    Product(name='Smartphone', description='Latest model smartphone', price=699.99, stock_quantity=25, quality='Medium'),
    Product(name='Headphones', description='Noise-cancelling headphones', price=199.99, stock_quantity=50, quality='High')
]

# Add products to the session
session.add_all(products)
session.commit()

# Example orders
orders = [
    Order(user_id=1, order_date=datetime.now(), status='pending'),
    Order(user_id=2, order_date=datetime.now(), status='shipped')
]

# Add orders to the session
session.add_all(orders)
session.commit()

# Example order items
order_items = [
    OrderItem(order_id=1, product_id=1, quantity=1, price=999.99),
    OrderItem(order_id=1, product_id=3, quantity=2, price=199.99),
    OrderItem(order_id=2, product_id=2, quantity=1, price=699.99)
]

# Add order items to the session
session.add_all(order_items)
session.commit()

# Query all users
all_users = session.query(User).all()
for user in all_users:
    print(f"Username: {user.username}, Email: {user.email_address}")

# Query products with 'High' quality
high_quality_products = session.query(Product).filter(Product.quality == 'High').all()
for product in high_quality_products:
    print(f"Product Name: {product.name}, Price: {product.price}")

# Query orders for user with id 1
user_orders = session.query(Order).filter(Order.user_id == 1).all()
for order in user_orders:
    print(f"Order ID: {order.id}, Status: {order.status}, Date: {order.order_date}")

# Query order details including items for a specific order
order_id = 1  # Example order ID
order = session.query(Order).filter(Order.id == order_id).first()
if order:
    print(f"Order ID: {order.id}, Status: {order.status}, Date: {order.order_date}")
    for item in order.order_items:
        product = item.product
        print(f"  Product: {product.name}, Quantity: {item.quantity}, Price: {item.price}")

# Calculate total amount for a specific order
order_id = 1  # Example order ID
order_items = session.query(OrderItem).filter(OrderItem.order_id == order_id).all()
total_amount = sum(item.quantity * item.price for item in order_items)
print(f"Total Amount for Order ID {order_id}: {total_amount}")

