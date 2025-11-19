# Assignment 11-12: Sprint Planning
## Supermarket Management System

## 1. Sprint Goal

**Sprint Goal:** Implement inventory management functionality to track product stock levels and enable CRUD operations for product catalog.

---

## 2. Mini-ADR (Architecture Decision Record)

- **Decision:** Use PostgreSQL with REST API architecture
- **Reason:** Strong ACID compliance ensures accurate inventory tracking and prevents stock inconsistencies
- **Consequence:** Requires database schema design and migration management for inventory tables

---

## 3. Mini-API Description

**Endpoint:** `POST /api/products`

**Request:** `{ "name": "string", "price": "number", "stock": "integer", "category": "string" }`

**Success:** `201 Created` with product object including generated ID

**Fail:** `400 Bad Request` (invalid data) or `409 Conflict` (product already exists)

**Description:** Adds a new product to the supermarket inventory system

---

## Additional API Endpoint

**Endpoint:** `GET /api/products/{id}`

**Request:** Product ID as path parameter

**Success:** `200 OK` with `{ "id", "name", "price", "stock", "category", "lastUpdated" }`

**Fail:** `404 Not Found` (product doesn't exist)

**Description:** Retrieves detailed information about a specific product from inventory

---

**Project:** Supermarket Management System  
**Submitted by:** [Your Name]  
**Date:** November 2025
