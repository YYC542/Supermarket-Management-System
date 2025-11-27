"""
Integration Tests for Supermarket Management System
Tests the interaction between Product, Sales, and Manager classes
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from product import Product, ProductManager
from sales import Sale, SalesManager


def test_complete_shopping_scenario():
    """
    Integration Test: Complete shopping scenario
    Tests the full workflow from product management to sale completion
    """
    print("\n" + "="*60)
    print("INTEGRATION TEST: Complete Shopping Scenario")
    print("="*60)
    
    # Step 1: Setup inventory
    print("\n[Step 1] Setting up inventory...")
    product_manager = ProductManager()
    
    # Add products to inventory
    product_manager.add_product(Product("P001", "Apple", 1.50, 100, "Fruits"))
    product_manager.add_product(Product("P002", "Milk", 4.50, 50, "Dairy"))
    product_manager.add_product(Product("P003", "Bread", 2.50, 30, "Bakery"))
    product_manager.add_product(Product("P004", "Cheese", 6.00, 20, "Dairy"))
    
    assert len(product_manager.get_all_products()) == 4
    print("✓ Inventory setup complete: 4 products added")
    
    # Step 2: Create sales manager
    print("\n[Step 2] Initializing sales system...")
    sales_manager = SalesManager()
    print("✓ Sales system initialized")
    
    # Step 3: Customer 1 - Complete a sale
    print("\n[Step 3] Processing Customer 1 transaction...")
    sale1 = sales_manager.create_sale()
    
    # Add items to cart
    apple = product_manager.get_product("P001")
    milk = product_manager.get_product("P002")
    
    initial_apple_qty = apple.quantity
    initial_milk_qty = milk.quantity
    
    sale1.add_item(apple, 5)   # 5 apples
    sale1.add_item(milk, 2)    # 2 milk
    
    expected_total = (1.50 * 5) + (4.50 * 2)
    assert sale1.total == expected_total
    print(f"  Cart total: ${sale1.total:.2f}")
    
    # Apply member discount
    sale1.apply_discount(10)  # 10% discount
    assert sale1.total == expected_total * 0.9
    print(f"  After 10% discount: ${sale1.total:.2f}")
    
    # Complete sale
    sale1.complete_sale("Credit Card")
    sales_manager.record_sale(sale1)
    
    # Verify inventory updated
    assert apple.quantity == initial_apple_qty - 5
    assert milk.quantity == initial_milk_qty - 2
    print("✓ Customer 1 transaction complete")
    print(f"  Apple stock: {initial_apple_qty} → {apple.quantity}")
    print(f"  Milk stock: {initial_milk_qty} → {milk.quantity}")
    
    # Step 4: Customer 2 - Another sale
    print("\n[Step 4] Processing Customer 2 transaction...")
    sale2 = sales_manager.create_sale()
    
    bread = product_manager.get_product("P003")
    cheese = product_manager.get_product("P004")
    
    sale2.add_item(bread, 3)    # 3 bread
    sale2.add_item(cheese, 1)   # 1 cheese
    
    sale2.complete_sale("Cash")
    sales_manager.record_sale(sale2)
    
    print("✓ Customer 2 transaction complete")
    
    # Step 5: Verify sales statistics
    print("\n[Step 5] Verifying sales statistics...")
    total_sales = sales_manager.get_sales_count()
    total_revenue = sales_manager.get_total_revenue()
    avg_sale = sales_manager.get_average_sale_value()
    
    assert total_sales == 2
    assert total_revenue > 0
    assert avg_sale == total_revenue / total_sales
    
    print(f"  Total sales: {total_sales}")
    print(f"  Total revenue: ${total_revenue:.2f}")
    print(f"  Average sale: ${avg_sale:.2f}")
    
    # Step 6: Check inventory status
    print("\n[Step 6] Checking inventory status...")
    total_inventory_value = product_manager.get_total_inventory_value()
    dairy_products = product_manager.search_by_category("Dairy")
    low_stock = product_manager.get_low_stock_products(threshold=30)
    
    assert total_inventory_value > 0
    assert len(dairy_products) == 2  # Milk and Cheese
    
    print(f"  Total inventory value: ${total_inventory_value:.2f}")
    print(f"  Dairy products: {len(dairy_products)}")
    print(f"  Low stock items: {len(low_stock)}")
    
    print("\n" + "="*60)
    print("🎉 INTEGRATION TEST PASSED!")
    print("="*60)
    
    return True


def test_error_handling_integration():
    """
    Integration Test: Error handling across modules
    Tests that errors are properly handled in integrated scenarios
    """
    print("\n" + "="*60)
    print("INTEGRATION TEST: Error Handling")
    print("="*60)
    
    product_manager = ProductManager()
    sales_manager = SalesManager()
    
    # Add product with limited stock
    product = Product("P100", "Limited Item", 10.00, 3)
    product_manager.add_product(product)
    
    # Test 1: Try to sell more than available
    print("\n[Test 1] Attempting to oversell...")
    sale = sales_manager.create_sale()
    
    try:
        sale.add_item(product, 5)  # Only 3 available
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Insufficient stock" in str(e)
        print("✓ Overselling prevented correctly")
    
    # Test 2: Try to add duplicate product
    print("\n[Test 2] Attempting to add duplicate product ID...")
    duplicate = Product("P100", "Another Item", 15.00, 10)
    
    try:
        product_manager.add_product(duplicate)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "already exists" in str(e)
        print("✓ Duplicate product prevented correctly")
    
    # Test 3: Try invalid discount
    print("\n[Test 3] Attempting invalid discount...")
    sale2 = sales_manager.create_sale()
    sale2.add_item(product, 1)
    
    try:
        sale2.apply_discount(150)  # Invalid: > 100%
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "between 0 and 100" in str(e)
        print("✓ Invalid discount prevented correctly")
    
    print("\n" + "="*60)
    print("🎉 ERROR HANDLING TEST PASSED!")
    print("="*60)
    
    return True


def test_multi_transaction_inventory_consistency():
    """
    Integration Test: Inventory consistency across multiple transactions
    Ensures inventory remains consistent after multiple sales
    """
    print("\n" + "="*60)
    print("INTEGRATION TEST: Inventory Consistency")
    print("="*60)
    
    product_manager = ProductManager()
    sales_manager = SalesManager()
    
    # Setup: Add product with known quantity
    product = Product("P200", "Test Product", 5.00, 100)
    product_manager.add_product(product)
    
    initial_qty = product.quantity
    total_sold = 0
    
    print(f"\n[Initial] Product quantity: {initial_qty}")
    
    # Perform multiple sales
    print("\n[Processing] 5 sales transactions...")
    for i in range(5):
        sale = sales_manager.create_sale()
        qty_to_sell = 10 + i  # 10, 11, 12, 13, 14
        sale.add_item(product, qty_to_sell)
        sale.complete_sale("Cash")
        sales_manager.record_sale(sale)
        total_sold += qty_to_sell
        print(f"  Sale {i+1}: Sold {qty_to_sell} units")
    
    # Verify consistency
    expected_remaining = initial_qty - total_sold
    actual_remaining = product.quantity
    
    assert actual_remaining == expected_remaining
    assert sales_manager.get_sales_count() == 5
    
    print(f"\n[Final] Product quantity: {actual_remaining}")
    print(f"  Initial: {initial_qty}")
    print(f"  Sold: {total_sold}")
    print(f"  Remaining: {actual_remaining}")
    print(f"  Expected: {expected_remaining}")
    print("✓ Inventory consistency verified")
    
    print("\n" + "="*60)
    print("🎉 INVENTORY CONSISTENCY TEST PASSED!")
    print("="*60)
    
    return True


# Run all integration tests
if __name__ == "__main__":
    print("\n" + "="*70)
    print(" "*15 + "RUNNING INTEGRATION TESTS")
    print("="*70)
    
    test_complete_shopping_scenario()
    test_error_handling_integration()
    test_multi_transaction_inventory_consistency()
    
    print("\n" + "="*70)
    print("🎉🎉🎉 ALL INTEGRATION TESTS PASSED! 🎉🎉🎉")
    print("="*70 + "\n")
