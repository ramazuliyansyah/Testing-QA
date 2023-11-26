from typing import List
from sqlalchemy import Column, ForeignKey, String, Float, Integer, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class WelcomeModel:
    def __init__(self):
        self.message = "Hello World!"

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    sku = Column(String(30), unique=True)
    brand = Column(String(30))
    name = Column(String(30))
    description = Column(String(30))
    price = Column(Float)
    non_discountable = Column(Boolean, default=False)

    cart_items = relationship(
        "CartItem", back_populates="product", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Product(sku={self.sku!r}, brand={self.brand!r}, name={self.name!r})"

class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True)
    subtotal = Column(Float)
    shipping_fee = Column(Float)
    grand_total = Column(Float)
    coupon_code = Column(String(30), nullable=True)

    cart_items = relationship(
        "CartItem", back_populates="cart", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Cart(id={self.id!r})"

class CartItem(Base):
    __tablename__ = "cart_item"
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey("cart.id"))
    cart = relationship("Cart", back_populates="cart_items")

    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="cart_items")

    qty = Column(Integer)
    item_price = Column(Float)

class Promotion(Base):
    __tablename__ = "promotion"
    id = Column(Integer, primary_key=True)
    coupon_code = Column(String(30), unique=True)
    subtotal_discount = Column(Float, default=0)
    max_subtotal_discount = Column(Float, nullable=True)
    shipping_discount = Column(Float, default=0)
    max_shipping_discount = Column(Float, nullable=True)
    cashback = Column(Float, default=0)
    max_cashback = Column(Float, nullable=True)
