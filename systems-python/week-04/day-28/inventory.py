import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Product, Stock, Transaction

load_dotenv()

DATABASE_URL = "postgresql://mackook@localhost/inventory_db"
engine = create_engine(DATABASE_URL, echo=False)


def add_product(name: str, sku: str, price: float, description: str = None, low_stock_threshold: int = 10):
    with Session(engine) as session:
        # Check if SKU already exists
        existing = session.query(Product).filter(Product.sku == sku).first()
        if existing:
            print(f"ERROR: Product with SKU '{sku}' already exists")
            return

        product = Product(name=name, sku=sku, price=price, description=description)
        session.add(product)
        session.flush()  # get the product id

        stock = Stock(product_id=product.id, quantity=0, low_stock_threshold=low_stock_threshold)
        session.add(stock)
        session.commit()

        print(f"✓ Product '{name}' added with SKU '{sku}'")


def restock(sku: str, quantity: int, notes: str = None):
    if quantity <= 0:
        print("ERROR: Restock quantity must be positive")
        return

    with Session(engine) as session:
        product = session.query(Product).filter(Product.sku == sku).first()
        if not product:
            print(f"ERROR: Product with SKU '{sku}' not found")
            return

        transaction = Transaction(
            product_id=product.id,
            quantity_change=quantity,
            transaction_type="restock",
            notes=notes
        )
        session.add(transaction)

        product.stock.quantity += quantity
        session.commit()

        print(f"✓ Restocked '{product.name}' by {quantity} units. New quantity: {product.stock.quantity}")


def record_sale(sku: str, quantity: int, notes: str = None):
    if quantity <= 0:
        print("ERROR: Sale quantity must be positive")
        return

    with Session(engine) as session:
        product = session.query(Product).filter(Product.sku == sku).first()
        if not product:
            print(f"ERROR: Product with SKU '{sku}' not found")
            return

        if product.stock.quantity < quantity:
            print(f"ERROR: Insufficient stock. Available: {product.stock.quantity}, Requested: {quantity}")
            return

        transaction = Transaction(
            product_id=product.id,
            quantity_change=-quantity,
            transaction_type="sale",
            notes=notes
        )
        session.add(transaction)

        product.stock.quantity -= quantity
        session.commit()

        if product.stock.quantity <= product.stock.low_stock_threshold:
            print(f"⚠ WARNING: '{product.name}' is low on stock. Current: {product.stock.quantity}")

        print(f"✓ Sale recorded for '{product.name}'. Remaining: {product.stock.quantity}")


def view_stock():
    with Session(engine) as session:
        products = session.query(Product).all()
        if not products:
            print("No products found")
            return

        print("\n--- Current Stock Levels ---")
        for product in products:
            status = "⚠ LOW" if product.stock.quantity <= product.stock.low_stock_threshold else "✓ OK"
            print(f"{product.name} (SKU: {product.sku}) | Stock: {product.stock.quantity} | {status}")


if __name__ == "__main__":
    # Test the system
    print("=== Inventory Management System ===\n")

    add_product("Bluetooth Speaker", "SPK-001", 150.00, "Portable speaker", low_stock_threshold=5)
    add_product("Phone Case", "CASE-001", 25.00, "Protective case", low_stock_threshold=10)

    restock("SPK-001", 20, "Initial stock")
    restock("CASE-001", 50, "Initial stock")

    view_stock()

    record_sale("SPK-001", 3, "Customer purchase")
    record_sale("CASE-001", 45, "Bulk order")

    view_stock()

    record_sale("SPK-001", 20, "Should fail - insufficient stock")