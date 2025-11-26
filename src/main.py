"""
Main application demo
Demonstrates core features of the supermarket management system
"""

from product import Product, ProductManager
from sales import SalesManager


def demo_product_management():
    """Demo: Product management features"""
    print("\n" + "="*50)
    print("DEMO 1: PRODUCT MANAGEMENT")
    print("="*50)
    
    # Initialize manager
    pm = ProductManager()
    
    # Add products
    print("\n[Adding products...]")
    products = [
        Product("P001", "Milk", 3.99, 50, "Dairy"),
        Product("P002", "Bread", 2.49, 100, "Bakery"),
        Product("P003", "Apple", 0.99, 200, "Fruits"),
        Product("P004", "Chicken", 8.99, 30, "Meat"),
        Product("P005", "Rice", 12.99, 25, "Grains")
    ]
    
    for product in products:
        pm.add_product(product)
        print(f"✓ Added: {product}")
    
    # Display all products
    print(f"\n[Total products in system: {len(pm.get_all_products())}]")
    
    # Search by category
    print("\n[Searching for Dairy products...]")
    dairy_products = pm.search_by_category("Dairy")
    for p in dairy_products:
        print(f"  - {p}")
    
    # Check low stock
    print("\n[Checking low stock (threshold: 30)...]")
    low_stock = pm.get_low_stock_products(30)
    for p in low_stock:
        print(f"  ⚠️ Low stock: {p}")
    
    return pm


def demo_sales_process(product_manager):
    """Demo: Sales process"""
    print("\n" + "="*50)
    print("DEMO 2: SALES PROCESS (POS)")
    print("="*50)
    
    # Initialize sales manager
    sm = SalesManager()
    
    # Create a sale
    print("\n[Creating new sale...]")
    sale = sm.create_sale()
    print(f"✓ Sale created: {sale.sale_id}")
    
    # Add items to cart
    print("\n[Adding items to cart...]")
    milk = product_manager.get_product("P001")
    bread = product_manager.get_product("P002")
    apples = product_manager.get_product("P003")
    
    sale.add_item(milk, 2)
    print(f"  + Added: Milk x2")
    
    sale.add_item(bread, 1)
    print(f"  + Added: Bread x1")
    
    sale.add_item(apples, 5)
    print(f"  + Added: Apple x5")
    
    print(f"\n[Subtotal: ${sale.total:.2f}]")
    
    # Apply discount
    print("\n[Applying 10% member discount...]")
    discount = sale.apply_discount(10)
    print(f"  - Discount: ${discount:.2f}")
    print(f"  Final total: ${sale.total:.2f}")
    
    # Complete sale
    print("\n[Completing sale with Credit Card...]")
    sale.complete_sale("Credit Card")
    sm.record_sale(sale)
    print("✓ Sale completed")
    
    # Print receipt
    print(sale.get_receipt())
    
    # Show updated inventory
    print("[Updated inventory:]")
    print(f"  Milk: {milk.quantity} units remaining")
    print(f"  Bread: {bread.quantity} units remaining")
    print(f"  Apples: {apples.quantity} units remaining")
    
    return sm


def demo_sales_analytics(sales_manager):
    """Demo: Sales analytics"""
    print("\n" + "="*50)
    print("DEMO 3: SALES ANALYTICS")
    print("="*50)
    
    print(f"\nTotal sales completed: {sales_manager.get_sales_count()}")
    print(f"Total revenue: ${sales_manager.get_total_revenue():.2f}")


def main():
    """Main entry point"""
    print("\n" + "🏪"*25)
    print(" "*15 + "SUPERMARKET MANAGEMENT SYSTEM")
    print(" "*20 + "Feature Demonstration")
    print("🏪"*25)
    
    try:
        # Demo 1: Product Management
        pm = demo_product_management()
        
        # Demo 2: Sales Process
        sm = demo_sales_process(pm)
        
        # Demo 3: Analytics
        demo_sales_analytics(sm)
        
        print("\n" + "="*50)
        print("✅ ALL DEMOS COMPLETED SUCCESSFULLY")
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {e}\n")
        raise


if __name__ == "__main__":
    main()
