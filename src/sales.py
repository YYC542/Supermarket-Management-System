"""
Sales Management Module
Handles point-of-sale transactions and sales records
"""

from datetime import datetime


class SaleItem:
    """Individual item in a sale transaction"""
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.subtotal = product.price * quantity
    
    def __str__(self):
        return f"{self.product.name} x{self.quantity} = ${self.subtotal:.2f}"


class Sale:
    """Sale transaction"""
    
    def __init__(self, sale_id):
        self.sale_id = sale_id
        self.items = []
        self.timestamp = datetime.now()
        self.total = 0
        self.payment_method = None
        self.discount_applied = 0
    
    def add_item(self, product, quantity):
        """Add item to shopping cart"""
        if quantity > product.quantity:
            raise ValueError(f"Insufficient stock for {product.name}")
        
        item = SaleItem(product, quantity)
        self.items.append(item)
        self.total += item.subtotal
        return item
    
    def apply_discount(self, discount_percent):
        """Apply percentage discount to total"""
        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount must be between 0 and 100")
        
        discount_amount = self.total * (discount_percent / 100)
        self.total -= discount_amount
        self.discount_applied = discount_amount
        return discount_amount
    
    def complete_sale(self, payment_method):
        """Complete the sale and update inventory"""
        self.payment_method = payment_method
        
        for item in self.items:
            item.product.update_quantity(-item.quantity)
        
        return True
    
    def cancel_sale(self):
        """Cancel the sale"""
        self.items.clear()
        self.total = 0
        self.discount_applied = 0
        return True
    
    def get_receipt(self):
        """Generate a receipt string"""
        receipt = f"\n{'='*50}\n"
        receipt += f"{'SUPERMARKET RECEIPT':^50}\n"
        receipt += f"{'='*50}\n"
        receipt += f"Sale ID: {self.sale_id}\n"
        receipt += f"Date: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
        receipt += f"{'-'*50}\n"
        
        for item in self.items:
            receipt += f"{item}\n"
        
        receipt += f"{'-'*50}\n"
        
        if self.discount_applied > 0:
            receipt += f"Discount: -${self.discount_applied:.2f}\n"
        
        receipt += f"Total: ${self.total:.2f}\n"
        receipt += f"Payment Method: {self.payment_method}\n"
        receipt += f"{'='*50}\n"
        receipt += f"{'Thank you for shopping with us!':^50}\n"
        receipt += f"{'='*50}\n"
        
        return receipt


class SalesManager:
    """Sales Manager for handling multiple transactions"""
    
    def __init__(self):
        self.sales = []
        self.next_sale_id = 1
    
    def create_sale(self):
        """Create a new sale transaction"""
        sale = Sale(f"SALE-{self.next_sale_id:04d}")
        self.next_sale_id += 1
        return sale
    
    def record_sale(self, sale):
        """Record a completed sale"""
        self.sales.append(sale)
        return True
    
    def get_total_revenue(self):
        """Calculate total revenue from all sales"""
        return sum(sale.total for sale in self.sales)
    
    def get_sales_count(self):
        """Get total number of sales"""
        return len(self.sales)
    
    def get_sales_by_date(self, date):
        """Get all sales for a specific date"""
        return [s for s in self.sales if s.timestamp.date() == date]
    
    def get_average_sale_value(self):
        """Calculate average sale value"""
        if not self.sales:
            return 0
        return self.get_total_revenue() / len(self.sales)
