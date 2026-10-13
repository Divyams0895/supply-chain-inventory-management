# Supply Chain & Inventory Management System

An end-to-end inventory management and analytics project built using Python, MySQL, SQL, and Power BI.

## Overview

This project demonstrates how a supply chain inventory system can evolve from a simple CSV-based application into a relational database solution with interactive business intelligence dashboards.

It focuses on product and supplier management, stock monitoring, transaction tracking, and inventory analysis.

## Project Versions

### Version 1 — Python & CSV
- Menu-driven console application
- Product and supplier management
- Inventory stock updates and tracking
- Low-stock alerts and inventory valuation
- Sales, purchases, and transaction history
- CSV-based data storage

### Version 2 — Python & MySQL
- Relational database integration
- Product, supplier, inventory, and transaction tables
- SQL queries and CRUD operations
- Primary keys, foreign keys, and table relationships
- Structured storage for inventory and transaction records

### Version 3 — Power BI Analytics
- Executive Overview dashboard
- Inventory Analysis dashboard
- Sales & Transactions dashboard
- Supplier Analysis dashboard
- DAX measures and data model relationships
- Interactive reports for inventory and purchasing insights

## Technology Stack

- **Programming:** Python
- **Database:** MySQL
- **Query Language:** SQL
- **Business Intelligence:** Microsoft Power BI
- **Analytics:** DAX
- **Data Storage (Version 1):** CSV

## Key Business Questions

- Which products are running low on stock?
- What is the estimated value of current inventory?
- How do sales and purchase values change over time?
- Which product categories contribute the most sales?
- Which suppliers account for the highest purchasing value?
- How is inventory value distributed across suppliers and categories?

## Database Design

The MySQL database contains four core tables:

- `suppliers` — supplier details and contact information
- `products` — product information, categories, prices, and reorder levels
- `inventory` — current stock quantities
- `transactions` — historical sales and purchase records

Foreign keys connect products with suppliers and inventory and transaction records with products.

## Power BI Dashboards

The report is organized into four pages:

1. **Executive Overview** — key performance indicators and overall business trends.
2. **Inventory Analysis** — current stock, inventory value, and low-stock products.
3. **Sales & Transactions** — sales and purchases over time, category analysis, and transaction details.
4. **Supplier Analysis** — products supplied, purchasing value, and supplier inventory contribution.

> PowerBI Live Link:  `https://app.powerbi.com/groups/me/reports/74797f35-d936-4909-b801-3e51b5e22d07/56c7b6eb70e23ff292aa?experience=power-bi` 

## Getting Started

### Requirements
- Python 3
- MySQL Server and MySQL Workbench
- Microsoft Power BI Desktop for dashboard exploration

### Setup
1. Clone this repository.
2. Follow the instructions for the version you want to run.
3. For Version 2, create the MySQL database and execute the schema script.
4. Configure the database connection using your own local credentials.
5. Install any required Python packages.
6. Run the Python entry point specified for that version.
7. Open the Power BI report in Power BI Desktop after configuring its data connection.

Detailed setup commands will be documented alongside the corresponding version.

## Learning Outcomes

- Python application development and modular programming
- SQL CRUD operations and relational database design
- Data integrity through primary and foreign key relationships
- Inventory and transaction data management
- Data modeling, DAX, and interactive Power BI reporting
- Translating operational data into business insights

## Project Status

Developed iteratively, with a CSV-based Python version, a MySQL-backed version, and a Power BI analytics layer.

