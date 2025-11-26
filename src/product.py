"""
Product Management Module
Handles product CRUD operations for supermarket inventory
"""

class Product:
    """Product class representing a supermarket item"""
    
    def __init__(self, product_id, name, price, quantity, category="General"):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    
    def __str__(self):
        return f"Product(ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Qty: {self.quantity})"
    
    def update_quantity(self, amount):
        """Update stock quantity"""
        self.quantity += amount
        return self.quantity
    
    def is_in_stock(self):
        """Check if product is in stock"""
        return self.quantity > 0
    
    def calculate_total_value(self):
        """Calculate total value of product in stock"""
        return self.price * self.quantity


class ProductManager:
    """Manager class for handling multiple products"""
    
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        """Add a new product to inventory"""
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists")
        self.products[product.product_id] = product
        return True
    
    def get_product(self, product_id):
        """Retrieve a product by ID"""
        return self.products.get(product_id)
    
    def remove_product(self, product_id):
        """Remove a product from inventory"""
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False
    
    def update_stock(self, product_id, quantity):
        """Update product stock level"""
        product = self.get_product(product_id)
        if product:
            product.update_quantity(quantity)
            return True
        return False
    
    def get_all_products(self):
        """Get list of all products"""
        return list(self.products.values())
    
    def search_by_category(self, category):
        """Search products by category"""
        return [p for p in self.products.values() if p.category == category]
    
    def get_low_stock_products(self, threshold=10):
        """Get products with stock below threshold"""
        return [p for p in self.products.values() if p.quantity < threshold]
    
    def get_total_inventory_value(self):
        """Calculate total value of all inventory"""
        return sum(p.calculate_total_value() for p in self.products.values())
