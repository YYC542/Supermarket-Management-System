"""
Unit Tests for Supermarket Management System
Tests for Product and ProductManager classes
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from product import Product, ProductManager


# ========== Product Class Tests ==========

def test_product_creation():
    """Test creating a product instance"""
    product = Product("P001", "Apple", 1.50, 100, "Fruits")
    
    assert product.product_id == "P001"
    assert product.name == "Apple"
    assert product.price == 1.50
    assert product.quantity == 100
    assert product.category == "Fruits"
    print("✓ Product creation test passed")


def test_product_update_quantity():
    """Test updating product quantity"""
    product = Product("P002", "Banana", 0.80, 50)
    
    # Add stock
    new_qty = product.update_quantity(30)
    assert new_qty == 80
    assert product.quantity == 80
    
    # Remove stock
    new_qty = product.update_quantity(-20)
    assert new_qty == 60
    assert product.quantity == 60
    
    print("✓ Product quantity update test passed")


def test_product_is_in_stock():
    """Test checking if product is in stock"""
    product1 = Product("P003", "Orange", 2.00, 10)
    product2 = Product("P004", "Mango", 3.00, 0)
    
    assert product1.is_in_stock() == True
    assert product2.is_in_stock() == False
    
    print("✓ Product stock check test passed")


def test_product_calculate_total_value():
    """Test calculating total value of product"""
    product = Product("P005", "Milk", 4.50, 20)
    
    total_value = product.calculate_total_value()
    assert total_value == 90.0  # 4.50 * 20
    
    print("✓ Product total value calculation test passed")


# ========== ProductManager Class Tests ==========

def test_product_manager_add_product():
    """Test adding products to manager"""
    manager = ProductManager()
    product = Product("P006", "Bread", 2.50, 30)
    
    result = manager.add_product(product)
    assert result == True
    assert len(manager.products) == 1
    
    print("✓ ProductManager add product test passed")


def test_product_manager_duplicate_product():
    """Test that duplicate product IDs are rejected"""
    manager = ProductManager()
    product1 = Product("P007", "Cheese", 5.00, 15)
    product2 = Product("P007", "Different Cheese", 6.00, 20)
    
    manager.add_product(product1)
    
    try:
        manager.add_product(product2)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "already exists" in str(e)
        print("✓ ProductManager duplicate prevention test passed")


def test_product_manager_get_product():
    """Test retrieving a product by ID"""
    manager = ProductManager()
    product = Product("P008", "Eggs", 3.00, 50)
    manager.add_product(product)
    
    retrieved = manager.get_product("P008")
    assert retrieved is not None
    assert retrieved.name == "Eggs"
    
    # Test non-existent product
    non_existent = manager.get_product("P999")
    assert non_existent is None
    
    print("✓ ProductManager get product test passed")


def test_product_manager_remove_product():
    """Test removing a product"""
    manager = ProductManager()
    product = Product("P009", "Butter", 4.00, 25)
    manager.add_product(product)
    
    result = manager.remove_product("P009")
    assert result == True
    assert len(manager.products) == 0
    
    # Try removing non-existent product
    result = manager.remove_product("P009")
    assert result == False
    
    print("✓ ProductManager remove product test passed")


def test_product_manager_update_stock():
    """Test updating stock through manager"""
    manager = ProductManager()
    product = Product("P010", "Rice", 10.00, 100)
    manager.add_product(product)
    
    result = manager.update_stock("P010", 50)
    assert result == True
    assert product.quantity == 150
    
    # Test non-existent product
    result = manager.update_stock("P999", 10)
    assert result == False
    
    print("✓ ProductManager update stock test passed")


def test_product_manager_search_by_category():
    """Test searching products by category"""
    manager = ProductManager()
    manager.add_product(Product("P011", "Apple", 1.50, 100, "Fruits"))
    manager.add_product(Product("P012", "Banana", 0.80, 50, "Fruits"))
    manager.add_product(Product("P013", "Milk", 4.50, 20, "Dairy"))
    
    fruits = manager.search_by_category("Fruits")
    assert len(fruits) == 2
    
    dairy = manager.search_by_category("Dairy")
    assert len(dairy) == 1
    
    print("✓ ProductManager search by category test passed")


def test_product_manager_low_stock_products():
    """Test finding low stock products"""
    manager = ProductManager()
    manager.add_product(Product("P014", "Item1", 1.00, 5))   # Low stock
    manager.add_product(Product("P015", "Item2", 2.00, 15))  # Normal stock
    manager.add_product(Product("P016", "Item3", 3.00, 8))   # Low stock
    
    low_stock = manager.get_low_stock_products(threshold=10)
    assert len(low_stock) == 2
    
    print("✓ ProductManager low stock detection test passed")


def test_product_manager_total_inventory_value():
    """Test calculating total inventory value"""
    manager = ProductManager()
    manager.add_product(Product("P017", "Item1", 10.00, 5))   # Value: 50
    manager.add_product(Product("P018", "Item2", 20.00, 3))   # Value: 60
    manager.add_product(Product("P019", "Item3", 5.00, 10))   # Value: 50
    
    total_value = manager.get_total_inventory_value()
    assert total_value == 160.0
    
    print("✓ ProductManager total inventory value test passed")


# Run all tests if executed directly
if __name__ == "__main__":
    print("\n" + "="*60)
    print("RUNNING UNIT TESTS - PRODUCT MODULE")
    print("="*60 + "\n")
    
    test_product_creation()
    test_product_update_quantity()
    test_product_is_in_stock()
    test_product_calculate_total_value()
    test_product_manager_add_product()
    test_product_manager_duplicate_product()
    test_product_manager_get_product()
    test_product_manager_remove_product()
    test_product_manager_update_stock()
    test_product_manager_search_by_category()
    test_product_manager_low_stock_products()
    test_product_manager_total_inventory_value()
    
    print("\n" + "="*60)
    print("🎉 ALL UNIT TESTS PASSED!")
    print("="*60 + "\n")
