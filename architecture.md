# System Architecture

## Overview
The Supermarket Management System follows a three-tier MVC architecture with separate presentation, business logic, and data access layers.

## Architecture Diagram<img width="843" height="1026" alt="image" src="https://github.com/user-attachments/assets/11dab459-c44b-4627-ba82-216a897ba99b" />
## Main Components

### 1. Frontend (React.js)
- **Dashboard Module**: Overview of sales, inventory alerts, and key metrics
- **Inventory Module**: Product catalog, stock levels, reorder management
- **POS Module**: Barcode scanning, billing, payment processing
- **Employee Module**: Staff records, attendance, shift scheduling
- **Reports Module**: Sales reports, inventory reports, profit analysis
- **Admin Module**: User management, system configuration

### 2. Backend (Spring Boot)
- **REST API Controllers**: Handle HTTP requests from frontend
- **Service Layer**: Business logic implementation
- **Repository Layer**: Database operations using JPA
- **Security**: JWT-based authentication and role-based access control
- **Exception Handling**: Centralized error management

### 3. Database (MySQL)
- **Products Table**: Item details, prices, categories, stock levels
- **Sales Table**: Transaction records, items sold, payment methods
- **Employees Table**: Staff information, roles, credentials
- **Suppliers Table**: Vendor details, contact info, supply history
- **Customers Table**: Customer profiles, loyalty points, purchase history
- **Inventory_Logs Table**: Stock movement tracking, audit trail

## Key Features Architecture

### Inventory Management
- Real-time stock tracking with automatic alerts for low stock
- Barcode/SKU-based product identification
- Batch and expiry date management
- Automated reorder suggestions based on sales trends

### Point of Sale (POS)
- Fast barcode scanning interface
- Multiple payment methods (cash, card, digital wallets)
- Receipt generation and printing
- Return and refund processing

### Analytics & Reporting
- Daily, weekly, monthly sales reports
- Profit margin analysis by product/category
- Inventory turnover reports
- Employee performance metrics

## Security Considerations
- Password encryption using BCrypt
- Role-based access (Admin, Manager, Cashier, Inventory Staff)
- JWT tokens for session management
- SQL injection prevention through parameterized queries
- Input validation on all forms
- Audit logging for critical operations
