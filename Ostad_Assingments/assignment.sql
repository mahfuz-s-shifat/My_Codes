
-- Multi-Vendor SaaS Application - Complete SQL Script (DDL, DML, DQL)


-- 1. Create SubscriptionPlan table

CREATE TABLE SubscriptionPlan (
    plan_id INT PRIMARY KEY AUTO_INCREMENT,
    plan_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    duration VARCHAR(50) NOT NULL,
    features TEXT
);


-- 2. Create Vendor table with Foreign Key to SubscriptionPlan

CREATE TABLE Vendor (
    vendor_id INT PRIMARY KEY AUTO_INCREMENT,
    business_name VARCHAR(150) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    business_address TEXT NOT NULL,
    subscription_plan_id INT,
    CONSTRAINT fk_vendor_subscription 
        FOREIGN KEY (subscription_plan_id) 
        REFERENCES SubscriptionPlan(plan_id)
        ON DELETE SET NULL
);


-- 3. Create Category table

CREATE TABLE Category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT
);


-- 4. Create Product table with Foreign Key to Vendor

CREATE TABLE Product (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    vendor_id INT NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL,
    status ENUM('active', 'inactive') DEFAULT 'active',
    CONSTRAINT fk_product_vendor 
        FOREIGN KEY (vendor_id) 
        REFERENCES Vendor(vendor_id) 
        ON DELETE CASCADE
);


-- 5. Create ProductCategory junction table for M:N relationship between Product and Category

CREATE TABLE ProductCategory (
    product_id INT,
    category_id INT,
    PRIMARY KEY (product_id, category_id),
    CONSTRAINT fk_pc_product 
        FOREIGN KEY (product_id) 
        REFERENCES Product(product_id) 
        ON DELETE CASCADE,
    CONSTRAINT fk_pc_category 
        FOREIGN KEY (category_id) 
        REFERENCES Category(category_id) 
        ON DELETE CASCADE
);


-- 6. Create Customer table

CREATE TABLE Customer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address TEXT NOT NULL
);


-- 7. Create Order table

CREATE TABLE `Order` (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    order_status VARCHAR(50) NOT NULL,
    CONSTRAINT fk_order_customer FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);


-- 8. Create OrderItem table

CREATE TABLE OrderItem (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_orderitem_order FOREIGN KEY (order_id) REFERENCES `Order`(order_id) ON DELETE CASCADE,
    CONSTRAINT fk_orderitem_product FOREIGN KEY (product_id) REFERENCES Product(product_id)
);


-- 9. Create Payment table

CREATE TABLE Payment (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    method VARCHAR(50) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_status VARCHAR(50) NOT NULL,
    CONSTRAINT fk_payment_order FOREIGN KEY (order_id) REFERENCES `Order`(order_id) ON DELETE CASCADE
);





-- PART C: SQL DML (Insert/Update/Delete Operations)


-- 01. Insert a new vendor named "SmartTech Ltd." under the Basic plan

INSERT INTO Vendor (business_name, contact_person, email, phone_number, business_address, subscription_plan_id)
VALUES (
    'SmartTech Ltd.', 
    'Rahim Khan', 
    'rahim@smarttech.com', 
    '017XXXXXXXX', 
    'Dhaka, Bangladesh', 
    (SELECT plan_id FROM SubscriptionPlan WHERE plan_name = 'Basic')
);


-- 02. Insert a product called "Laptop" under Electronics category belonging to SmartTech Ltd.

INSERT INTO Product (vendor_id, product_name, description, price, stock_quantity, status)
VALUES (
    (SELECT vendor_id FROM Vendor WHERE business_name = 'SmartTech Ltd.'),
    'Laptop',
    'High-performance laptop',
    75000.00,
    10,
    'active'
);


INSERT INTO ProductCategory (product_id, category_id)
VALUES (
    LAST_INSERT_ID(),
    (SELECT category_id FROM Category WHERE name = 'Electronics')
);


-- 03. Update the stock quantity of "Laptop" product to 15
UPDATE Product 
SET stock_quantity = 15 
WHERE product_name = 'Laptop';


-- 04. Delete a customer whose email is "oldcustomer@gmail.com"

DELETE FROM Customer 
WHERE email = 'oldcustomer@gmail.com';





-- PART D: SQL Queries (DQL)


-- 01. Display all vendors along with their subscription plan name and price
SELECT 
    v.business_name, 
    v.contact_person, 
    v.email, 
    sp.plan_name, 
    sp.price
FROM Vendor v
LEFT JOIN SubscriptionPlan sp ON v.subscription_plan_id = sp.plan_id;


-- 02. Find all products under the category "Electronics" with their name, price, and stock quantity

SELECT 
    p.product_name, 
    p.price, 
    p.stock_quantity
FROM Product p
JOIN ProductCategory pc ON p.product_id = pc.product_id
JOIN Category c ON pc.category_id = c.category_id
WHERE c.name = 'Electronics';


-- 03. List all orders placed by customer "Karim Uddin", showing order_id, date, total_amount, and status

SELECT 
    o.order_id, 
    o.order_date, 
    o.total_amount, 
    o.order_status
FROM `Order` o
JOIN Customer c ON o.customer_id = c.customer_id
WHERE c.name = 'Karim Uddin';


-- 04. Show the payment details (method, amount, status) for order_id = 1

SELECT 
    method, 
    amount, 
    payment_status
FROM Payment
WHERE order_id = 1;


-- 05. Find the top 5 best-selling products based on total quantity sold

SELECT 
    p.product_id, 
    p.product_name, 
    SUM(oi.quantity) AS total_quantity_sold
FROM Product p
JOIN OrderItem oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 5;