"""
Sales Management Module
Handles point-of-sale transactions
"""

from datetime import datetime


class SaleItem:
    """Individual item in a sale"""
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.subtotal = product.price * quantity
    
    def __str__(self):
        return f"{self.product.name} x{self.quantity} = ${self.subtotal:.2f}"


class Sale:
    """Sales transaction"""
    
    def __init__(self, sale_id):
        self.sale_id = sale_id
        self.items = []
        self.timestamp = datetime.now()
        self.total = 0
        self.payment_method = None
    
    def add_item(self, product, quantity):
        """Add product to cart"""
        if quantity > product.quantity:
            raise ValueError(f"Insufficient stock for {product.name}")
        
        item = SaleItem(product, quantity)
        self.items.append(item)
        self.total += item.subtotal
        return item
    
    def apply_discount(self, discount_percent):
        """Apply discount to total"""
        if 0 <= discount_percent <= 100:
            discount_amount = self.total * (discount_percent / 100)
            self.total -= discount_amount
            return discount_amount
        raise ValueError("Discount must be between 0 and 100")
    
    def complete_sale(self, payment_method):
        """Complete the sale and update inventory"""
        self.payment_method = payment_method
        for item in self.items:
            item.product.update_quantity(-item.quantity)
        return True
    
    def get_receipt(self):
        """Generate receipt"""
        receipt = f"\n{'='*40}\n"
        receipt += f"  SUPERMARKET RECEIPT\n"
        receipt += f"{'='*40}\n"
        receipt += f"Sale ID: {self.sale_id}\n"
        receipt += f"Date: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
        receipt += f"{'-'*40}\n"
        
        for item in self.items:
            receipt += f"{item}\n"
        
        receipt += f"{'-'*40}\n"
        receipt += f"Total: ${self.total:.2f}\n"
        receipt += f"Payment: {self.payment_method}\n"
        receipt += f"{'='*40}\n"
        receipt += f"Thank you for shopping with us!\n"
        receipt += f"{'='*40}\n"
        
        return receipt


class SalesManager:
    """Sales Manager for tracking transactions"""
    
    def __init__(self):
        self.sales = []
        self.next_sale_id = 1
    
    def create_sale(self):
        """Create a new sale"""
        sale = Sale(f"SALE-{self.next_sale_id:04d}")
        self.next_sale_id += 1
        return sale
    
    def record_sale(self, sale):
        """Record completed sale"""
        self.sales.append(sale)
    
    def get_total_revenue(self):
        """Calculate total revenue"""
        return sum(sale.total for sale in self.sales)
    
    def get_sales_count(self):
        """Get number of completed sales"""
        return len(self.sales)
    
    def get_sales_by_date(self, date):
        """Get sales for a specific date"""
        return [s for s in self.sales if s.timestamp.date() == date]
