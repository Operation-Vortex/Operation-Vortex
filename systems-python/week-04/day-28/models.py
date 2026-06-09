from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime, timezone

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    sku = Column(String, unique=True, nullable=False)

    stock = relationship("Stock", back_populates="product", uselist=False)
    transactions = relationship("Transaction", back_populates="product")

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, sku={self.sku})"


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    quantity = Column(Integer, nullable=False, default=0)
    low_stock_threshold = Column(Integer, nullable=False, default=10)

    product = relationship("Product", back_populates="stock")

    def __repr__(self):
        return f"Stock(product_id={self.product_id}, quantity={self.quantity})"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    quantity_change = Column(Integer, nullable=False)
    transaction_type = Column(String, nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    product = relationship("Product", back_populates="transactions")

    def __repr__(self):
        return f"Transaction(product_id={self.product_id}, change={self.quantity_change}, type={self.transaction_type})"