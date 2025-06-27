# 📚 ALX Book Store Database Project

A comprehensive MySQL database implementation for an online bookstore management system. This project demonstrates professional database design principles, SQL best practices, and Python database integration.

[![MySQL](https://img.shields.io/badge/MySQL-8.0+-blue.svg)](https://www.mysql.com/)
[![Python](https://img.shields.io/badge/Python-3.6+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Features

- **Complete database schema** for online bookstore management
- **Normalized database design** with proper relationships
- **Python integration** for database creation and management
- **Error handling** and validation
- **Idempotent scripts** for safe re-execution
- **Sample data** and bulk insertion examples

## 📁 Project Structure

```
Intro_to_DB/
├── alx_book_store.sql        # 🗄️  Complete database schema creation
├── MySQLServer.py           # 🐍 Python script to create the database
├── task_2.sql               # 📋 Creates all tables in the database
├── task_3.sql               # 📑 Lists all tables in the database
├── task_4.sql               # 🔍 Shows the structure of the books table
├── task_5.sql               # ➕ Inserts a single customer record
├── task_6.sql               # 📊 Inserts multiple customer records
└── README.md                # 📖 This documentation
```
## 📋 Tasks Overview

| Task | File | Description |
|------|------|-------------|
| **0** | Design Phase | Database schema design for online bookstore |
| **1** | `alx_book_store.sql` | Complete database schema with all tables |
| **2** | `MySQLServer.py` | Python script for database creation |
| **3** | `task_2.sql` | Create all tables with proper constraints |
| **4** | `task_3.sql` | List all tables in the database |
| **5** | `task_4.sql` | Display books table structure |
| **6** | `task_5.sql` | Insert single customer record |
| **7** | `task_6.sql` | Bulk insert multiple customer records |

### Task Details

#### Task 0: Database Design
- 🎯 Designed a relational database schema for an online bookstore
- 📊 Identified core tables: Books, Authors, Customers, Orders, Order_Details
- 🔗 Established proper relationships between tables

#### Task 1: Database Creation (`alx_book_store.sql`)
- 🏗️ Created the complete database schema with all tables
- 🔑 Implemented primary and foreign key relationships
- 📝 Used appropriate data types for each column

#### Task 2: Python Database Creation (`MySQLServer.py`)
- 🐍 Python script that creates the database programmatically
- ⚠️ Handles connection errors gracefully
- ✅ Provides clear success/error messages

#### Task 3: Table Creation (`task_2.sql`)
- 📋 Created all five tables with proper constraints
- 🔗 Established all foreign key relationships
- 🔄 Used `IF NOT EXISTS` to make script idempotent

#### Task 4: List Tables (`task_3.sql`)
- 📑 Simple script to display all tables in the database
- 💻 Uses `SHOW TABLES` command

#### Task 5: Table Structure Inspection (`task_4.sql`)
- 🔍 Displays the complete structure of the books table
- 📊 Uses `INFORMATION_SCHEMA` instead of `DESCRIBE/EXPLAIN`

#### Task 6: Data Insertion (`task_5.sql`)
- ➕ Inserts a single customer record
- 🎯 Explicitly sets all field values

#### Task 7: Bulk Data Insertion (`task_6.sql`)
- 📊 Inserts multiple customer records in one statement
- ⚡ Uses efficient multi-row `INSERT` syntax

## 🚀 Quick Start

### Prerequisites
- MySQL 8.0 or higher
- Python 3.6 or higher
- MySQL Python connector (`mysql-connector-python`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Intro_to_DB
   ```

2. **Install Python dependencies:**
   ```bash
   pip install mysql-connector-python
   ```

3. **Set up MySQL credentials:**
   - Update `MySQLServer.py` with your MySQL credentials
   - Ensure MySQL server is running

## 🛠️ Usage

### Method 1: Using Python Script (Recommended)
```bash
# Create the database
python3 MySQLServer.py

# Create all tables
mysql -u username -p alx_book_store < task_2.sql

# Insert sample data
mysql -u username -p alx_book_store < task_5.sql
mysql -u username -p alx_book_store < task_6.sql
```

### Method 2: Using MySQL CLI
```bash
# Create database and tables
mysql -u username -p < alx_book_store.sql

# Run individual tasks
mysql -u username -p alx_book_store < task_3.sql  # List tables
mysql -u username -p alx_book_store < task_4.sql  # Show books structure
```

### Method 3: Step-by-step Execution
```bash
# 1. Create database
python3 MySQLServer.py

# 2. Create tables
mysql -u username -p alx_book_store < task_2.sql

# 3. Verify tables were created
mysql -u username -p alx_book_store < task_3.sql

# 4. Check books table structure
mysql -u username -p alx_book_store < task_4.sql

# 5. Insert sample data
mysql -u username -p alx_book_store < task_5.sql
mysql -u username -p alx_book_store < task_6.sql
```
## 🗄️ Database Schema

The database consists of five interconnected tables designed for optimal performance and data integrity:

### Tables Overview

| Table | Description | Key Features |
|-------|-------------|--------------|
| `Authors` | Stores author information | Primary key: `author_id` |
| `Books` | Contains book details | Foreign key to `Authors` |
| `Customers` | Customer information | Primary key: `customer_id` |
| `Orders` | Customer order records | Foreign key to `Customers` |
| `Order_Details` | Order line items | Links `Orders` and `Books` |

### Entity Relationship Diagram
```
Authors (1) ←→ (M) Books
                   ↓
Customers (1) ←→ (M) Orders (1) ←→ (M) Order_Details ←→ (M) Books
```

### Table Structures

#### Authors Table
- `author_id` (Primary Key)
- `author_name`

#### Books Table
- `book_id` (Primary Key)
- `title`
- `author_id` (Foreign Key → Authors)
- `price`
- `publication_date`

#### Customers Table
- `customer_id` (Primary Key)
- `customer_name`
- `email`
- `address`

#### Orders Table
- `order_id` (Primary Key)
- `customer_id` (Foreign Key → Customers)
- `order_date`

#### Order_Details Table
- `orderdetailid` (Primary Key)
- `order_id` (Foreign Key → Orders)
- `book_id` (Foreign Key → Books)
- `quantity`

## 🛡️ Best Practices Demonstrated

- ✅ **Proper database normalization** - Eliminates data redundancy
- ✅ **Primary and foreign key constraints** - Ensures data integrity
- ✅ **Appropriate data types** - Optimizes storage and performance
- ✅ **SQL keyword capitalization** - Enhances code readability
- ✅ **Error handling in Python** - Graceful failure management
- ✅ **Idempotent table creation** - Safe script re-execution
- ✅ **Efficient data insertion** - Bulk operations for better performance

## 🚀 Advanced Usage

### Database Querying Examples

```sql
-- Find all books by a specific author
SELECT b.title, b.price 
FROM Books b 
JOIN Authors a ON b.author_id = a.author_id 
WHERE a.author_name = 'Author Name';

-- Get customer order history
SELECT c.customer_name, o.order_date, b.title, od.quantity
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Order_Details od ON o.order_id = od.order_id
JOIN Books b ON od.book_id = b.book_id
WHERE c.customer_id = 1;
```

### Performance Optimization

```sql
-- Create indexes for better query performance
CREATE INDEX idx_books_author ON Books(author_id);
CREATE INDEX idx_orders_customer ON Orders(customer_id);
CREATE INDEX idx_orderdetails_order ON Order_Details(order_id);
```

## 🔧 Troubleshooting

### Common Issues

1. **Connection Error**: Ensure MySQL server is running and credentials are correct
2. **Permission Denied**: Check MySQL user privileges
3. **Table Already Exists**: Scripts are idempotent, safe to re-run
4. **Foreign Key Constraint**: Ensure parent tables exist before creating child tables

### Error Solutions

```bash
# Check MySQL service status
sudo systemctl status mysql

# Restart MySQL service
sudo systemctl restart mysql

# Check MySQL user privileges
mysql -u root -p -e "SHOW GRANTS FOR 'username'@'localhost';"
```

## 📈 Future Enhancements

- [ ] Add inventory management system
- [ ] Implement user authentication
- [ ] Create web interface using Flask/Django
- [ ] Add payment processing tables
- [ ] Implement product categories and reviews
- [ ] Add data analytics views

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

If you have any questions or need help with the project:

- Create an issue in the repository
- Email: support@example.com
- Documentation: [Project Wiki](https://github.com/your-repo/wiki)

---

**⭐ If you find this project helpful, please give it a star!**