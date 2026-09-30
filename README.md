# Supply Chain & Inventory Management System

A Python-based console application designed to manage products, suppliers, inventory, and stock transactions.

## Features

### Product Management

* Add products
* View all products
* Search products
* Update product details
* Delete products

### Supplier Management

* Add suppliers
* View suppliers
* Search suppliers

### Inventory Management

* Add stock
* Remove stock
* Check current stock
* Low-stock alerts
* Calculate total inventory value

### Transaction Management

* Purchase stock
* Sell products
* Maintain transaction history
* Automatic transaction ID generation

## Technologies Used

* Python
* CSV File Handling
* Object-Oriented Programming (OOP)
* File Handling
* Exception Handling
* Modular Programming

## Project Structure

```text
supply-chain-inventory-management/
│
├── data/
│   ├── productlist.csv
│   ├── supplierlist.csv
│   └── transactionlist.csv
│
├── src/
│   ├── main.py
│   ├── Products.py
│   ├── Suppliers.py
│   ├── Inventory.py
│   └── Transactions.py
│
└── README.md
```

## How to Run

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd supply-chain-inventory-management
```

Run the application:

```bash
python src/main.py
```

## Application Menu

```text
==================================================
       SUPPLY CHAIN & INVENTORY SYSTEM
==================================================

1. PRODUCT MANAGEMENT
2. SUPPLIER MANAGEMENT
3. INVENTORY MANAGEMENT
4. TRANSACTION MANAGEMENT
5. EXIT
```

## Learning Objectives

This project was developed to practice:

* Python Object-Oriented Programming
* Classes and objects
* Functions and methods
* CSV file handling
* CRUD operations
* Menu-driven applications
* Inventory management concepts
* Basic transaction processing
* Modular project organization

## Future Improvements

* Add a graphical user interface
* Add database integration using MySQL or SQLite
* Generate inventory reports
* Add advanced search and filtering
* Add sales and purchase reports


