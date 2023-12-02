from api.utils import get_price, get_subtotal
from api.models import Product
from .settings import DEFAULT_PRICE

def test_get_price(client):
    product_ids = [Product(id=index + 1).id for index in range(2)]
    prices = {id: id * DEFAULT_PRICE for id in product_ids}
    assert prices == get_price(product_ids)

def test_get_subtotal(client):
    cart_items = [
        {'product_id': 1, 'qty': 3},
        {'product_id': 2, 'qty': 2},
    ]
    cart = {'cart_items': cart_items}

    expected_subtotal = sum(DEFAULT_PRICE * item['product_id'] * item['qty'] for item in cart_items)
    assert expected_subtotal == get_subtotal(cart)['subtotal']