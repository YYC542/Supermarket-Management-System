"""
Unit Tests for Sales Management System
Tests for Sale, SaleItem, and SalesManager classes
"""

import sys
import os
from datetime import datetime

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from product import Product
from sales import SaleItem, Sale, SalesManager


# ========== SaleItem Class Tests ==========

def test_sale_item_creation():
    """Test creating a sale item"""
    product = Product("P001", "Apple", 1.50, 100)
    item = SaleItem(product, 5)
    
    assert item.product == product
    assert item.quantity == 5
    assert item.subtotal == 7.50  # 1.50 * 5
    
    print("✓ SaleItem creation test passed")


def test_sale_item_str():
    """Test SaleItem string representation"""
    product = Product("P002", "Banana", 0.80, 50)
    item = SaleItem(product, 10)
    
    item_str = str(item)
    assert "Banana" in item_str
    assert "10" in item_str
    assert "8.00" in item_str
    
    print("✓ SaleItem string representation test passed")


# ========== Sale Class Tests ==========

def test_sale_creation():
    """Test creating a sale transaction"""
    sale = Sale("SALE-0001")
    
    assert sale.sale_id == "SALE-0001"
    assert len(sale.items) == 0
    assert sale.total == 0
    assert sale.payment_method is None
    assert isinstance(sale.timestamp, datetime)
    
    print("✓ Sale creation test passed")


def test_sale_add_item():
    """Test adding items to sale"""
    sale = Sale("SALE-0002")
    product = Product("P003", "Orange", 2.00, 20)
    
    item = sale.add_item(product, 3)
    
    assert len(sale.items) == 1
    assert sale.total == 6.00
    assert item.quantity == 3
    
    print("✓ Sale add item test passed")


def test_sale_add_multiple_items():
    """Test adding multiple items to sale"""
    sale = Sale("SALE-0003")
    product1 = Product("P004", "Milk", 4.50, 30)
    product2 = Product("P005", "Bread", 2.50, 40)
    
    sale.add_item(product1, 2)   # 9.00
    sale.add_item(product2, 3)   # 7.50
    
    assert len(sale.items) == 2
    assert sale.total == 16.50
    
    print("✓ Sale add multiple items test passed")


def test_sale_insufficient_stock():
    """Test that sale rejects insufficient stock"""
    sale = Sale("SALE-0004")
    product = Product("P006", "Eggs", 3.00, 5)
    
    try:
        sale.add_item(product, 10)  # More than available
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Insufficient stock" in str(e)
        print("✓ Sale insufficient stock prevention test passed")


def test_sale_apply_discount():
    """Test applying discount to sale"""
    sale = Sale("SALE-0005")
    product = Product("P007", "Cheese", 10.00, 20)
    sale.add_item(product, 2)  # Total: 20.00
    
    discount = sale.apply_discount(10)  # 10% discount
    
    assert discount == 2.00
    assert sale.total == 18.00
    assert sale.discount_applied == 2.00
    
    print("✓ Sale apply discount test passed")


def test_sale_invalid_discount():
    """Test that invalid discount is rejected"""
    sale = Sale("SALE-0006")
    product = Product("P008", "Butter", 5.00, 15)
    sale.add_item(product, 1)
    
    try:
        sale.apply_discount(150)  # Invalid: > 100%
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "between 0 and 100" in str(e)
        print("✓ Sale invalid discount rejection test passed")


def test_sale_complete():
    """Test completing a sale transaction"""
    sale = Sale("SALE-0007")
    product = Product("P009", "Rice", 8.00, 50)
    sale.add_item(product, 5)
    
    initial_qty = product.quantity
    result = sale.complete_sale("Credit Card")
    
    assert result == True
    assert sale.payment_method == "Credit Card"
    assert product.quantity == initial_qty - 5  # Stock reduced
    
    print("✓ Sale complete test passed")


def test_sale_cancel():
    """Test canceling a sale"""
    sale = Sale("SALE-0008")
    product = Product("P010", "Oil", 6.00, 25)
    sale.add_item(product, 2)
    
    result = sale.cancel_sale()
    
    assert result == True
    assert len(sale.items) == 0
    assert sale.total == 0
    assert sale.discount_applied == 0
    
    print("✓ Sale cancel test passed")


def test_sale_get_receipt():
    """Test generating a receipt"""
    sale = Sale("SALE-0009")
    product = Product("P011", "Sugar", 3.00, 40)
    sale.add_item(product, 3)
    sale.complete_sale("Cash")
    
    receipt = sale.get_receipt()
    
    assert "SALE-0009" in receipt
    assert "Sugar" in receipt
    assert "9.00" in receipt
    assert "Cash" in receipt
    assert "Thank you" in receipt
    
    print("✓ Sale receipt generation test passed")


# ========== SalesManager Class Tests ==========

def test_sales_manager_creation():
    """Test creating a sales manager"""
    manager = SalesManager()
    
    assert len(manager.sales) == 0
    assert manager.next_sale_id == 1
    
    print("✓ SalesManager creation test passed")


def test_sales_manager_create_sale():
    """Test creating a new sale through manager"""
    manager = SalesManager()
    
    sale1 = manager.create_sale()
    assert sale1.sale_id == "SALE-0001"
    
    sale2 = manager.create_sale()
    assert sale2.sale_id == "SALE-0002"
    
    print("✓ SalesManager create sale test passed")


def test_sales_manager_record_sale():
    """Test recording a completed sale"""
    manager = SalesManager()
    sale = manager.create_sale()
    product = Product("P012", "Tea", 4.00, 30)
    sale.add_item(product, 2)
    sale.complete_sale("Debit Card")
    
    result = manager.record_sale(sale)
    
    assert result == True
    assert len(manager.sales) == 1
    
    print("✓ SalesManager record sale test passed")


def test_sales_manager_total_revenue():
    """Test calculating total revenue"""
    manager = SalesManager()
    
    # Sale 1
    sale1 = manager.create_sale()
    product1 = Product("P013", "Coffee", 5.00, 20)
    sale1.add_item(product1, 2)  # 10.00
    sale1.complete_sale("Cash")
    manager.record_sale(sale1)
    
    # Sale 2
    sale2 = manager.create_sale()
    product2 = Product("P014", "Juice", 3.00, 25)
    sale2.add_item(product2, 3)  # 9.00
    sale2.complete_sale("Card")
    manager.record_sale(sale2)
    
    total = manager.get_total_revenue()
    assert total == 19.00
    
    print("✓ SalesManager total revenue test passed")


def test_sales_manager_sales_count():
    """Test getting total number of sales"""
    manager = SalesManager()
    
    for i in range(5):
        sale = manager.create_sale()
        product = Product(f"P{i}", f"Item{i}", 1.00, 10)
        sale.add_item(product, 1)
        sale.complete_sale("Cash")
        manager.record_sale(sale)
    
    count = manager.get_sales_count()
    assert count == 5
    
    print("✓ SalesManager sales count test passed")


def test_sales_manager_average_sale_value():
    """Test calculating average sale value"""
    manager = SalesManager()
    
    # Sale 1: $10
    sale1 = manager.create_sale()
    product1 = Product("P015", "Item1", 10.00, 10)
    sale1.add_item(product1, 1)
    sale1.complete_sale("Cash")
    manager.record_sale(sale1)
    
    # Sale 2: $20
    sale2 = manager.create_sale()
    product2 = Product("P016", "Item2", 20.00, 10)
    sale2.add_item(product2, 1)
    sale2.complete_sale("Cash")
    manager.record_sale(sale2)
    
    average = manager.get_average_sale_value()
    assert average == 15.00  # (10 + 20) / 2
    
    print("✓ SalesManager average sale value test passed")


# Run all tests if executed directly
if __name__ == "__main__":
    print("\n" + "="*60)
    print("RUNNING UNIT TESTS - SALES MODULE")
    print("="*60 + "\n")
    
    test_sale_item_creation()
    test_sale_item_str()
    test_sale_creation()
    test_sale_add_item()
    test_sale_add_multiple_items()
    test_sale_insufficient_stock()
    test_sale_apply_discount()
    test_sale_invalid_discount()
    test_sale_complete()
    test_sale_cancel()
    test_sale_get_receipt()
    test_sales_manager_creation()
    test_sales_manager_create_sale()
    test_sales_manager_record_sale()
    test_sales_manager_total_revenue()
    test_sales_manager_sales_count()
    test_sales_manager_average_sale_value()
    
    print("\n" + "="*60)
    print("🎉 ALL UNIT TESTS PASSED!")
    print("="*60 + "\n")
