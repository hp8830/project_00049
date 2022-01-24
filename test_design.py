from supermarket import Checkout
import pytest 

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("item_01", 1)
    checkout.addItemPrice("item_02", 2)
    return checkout


def test_canCalculateTotal(checkout): 
    checkout.addItem("item_01")
    assert checkout.calcTotal() == 1


def test_canAddMultipleItemsCorrectTotal(checkout): 
    checkout.addItem("item_01")
    checkout.addItem("item_02")
    assert checkout.calcTotal() == 3


def test_canAddDiscountRules(checkout):
    checkout.addDiscount("item_01", 3, 2)

def test_canApplyDiscountToTotal(checkout): 
    checkout.addDiscount("item_01", 3, 2)
    checkout.addItem("item_01")
    checkout.addItem("item_01")
    checkout.addItem("item_01")
    assert checkout.calcTotal() == 2

def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")