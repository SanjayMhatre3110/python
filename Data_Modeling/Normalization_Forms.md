# Database Normalization Walkthrough

## Unnormalized Form (UNF)
Data is stored with repeating groups and multi-valued fields.

| OrderID | CustomerName | CustomerAddress | Products                  | TotalAmount |
|---------|--------------|-----------------|---------------------------|-------------|
| 101     | John Smith   | 12 Main St      | Laptop, Mouse             | 1200        |
| 102     | Alice Brown  | 45 Oak Ave      | Phone, Headphones, Charger| 950         |
| 103     | Bob White    | 78 Pine Rd      | Tablet                    | 600         |

---

## First Normal Form (1NF)
Eliminate multi-valued attributes. Each row contains atomic values.

| OrderID | CustomerName | CustomerAddress | Product    | TotalAmount |
|---------|--------------|-----------------|------------|-------------|
| 101     | John Smith   | 12 Main St      | Laptop     | 1200        |
| 101     | John Smith   | 12 Main St      | Mouse      | 1200        |
| 102     | Alice Brown  | 45 Oak Ave      | Phone      | 950         |
| 102     | Alice Brown  | 45 Oak Ave      | Headphones | 950         |
| 102     | Alice Brown  | 45 Oak Ave      | Charger    | 950         |
| 103     | Bob White    | 78 Pine Rd      | Tablet     | 600         |

---

## Second Normal Form (2NF)
Remove partial dependency. Split customer info into a separate table.

**Customer Table**
| Customer_ID | CustomerName | CustomerAddress |
|-------------|--------------|-----------------|
| 1           | John Smith   | 12 Main St      |
| 2           | Alice Brown  | 45 Oak Ave      |
| 3           | Bob White    | 78 Pine Rd      |

**Order Table**
| OrderID | Customer_ID | Product | TotalAmount |
|---------|-------------|---------|-------------|
| 101     | 1           | Laptop  | 1200        |
| 101     | 1           | Mouse   | 1200        |
| 102     | 2           | Phone   | 950         |
| 102     | 2           | Headphones | 950      |
| 102     | 2           | Charger | 950         |
| 103     | 3           | Tablet  | 600         |

---

## Third Normal Form (3NF)
Remove transitive dependency. Create a separate Product table and split Order Header vs Order Details.

**Customer Table**
| Customer_ID | CustomerName | CustomerAddress |
|-------------|--------------|-----------------|
| 1           | John Smith   | 12 Main St      |
| 2           | Alice Brown  | 45 Oak Ave      |
| 3           | Bob White    | 78 Pine Rd      |

**Product Table**
| Product_ID | ProductName  | UnitPrice |
|------------|--------------|-----------|
| 1          | Laptop       | 1200      |
| 2          | Mouse        | 25        |
| 3          | Phone        | 950       |
| 4          | Headphones   | 150       |
| 5          | Charger      | 30        |
| 6          | Tablet       | 600       |

**Order Header Table**
| OrderID | Customer_ID | OrderDate   | TotalAmount |
|---------|-------------|-------------|-------------|
| 101     | 1           | 2026-04-01  | 1225        |
| 102     | 2           | 2026-04-02  | 1130        |
| 103     | 3           | 2026-04-03  | 600         |

**Order Details Table**
| OrderID | Product_ID | Quantity | LineAmount |
|---------|------------|----------|------------|
| 101     | 1          | 1        | 1200       |
| 101     | 2          | 1        | 25         |
| 102     | 3          | 1        | 950        |
| 102     | 4          | 1        | 150        |
| 102     | 5          | 1        | 30         |
| 103     | 6          | 1        | 600        |

---

## Boyce-Codd Normal Form (BCNF)
Ensure every determinant is a candidate key.  
Example refinement: if one product is always supplied by one vendor, then `Product → Vendor` is a dependency. We split vendors into their own table.

**Vendor Table**
| Vendor_ID | VendorName | ContactInfo |
|-----------|------------|-------------|
| V1        | TechWorld  | info@techworld.com |
| V2        | GadgetHub  | support@gadgethub.com |

**Product Table (refined)**
| Product_ID | ProductName | UnitPrice | Vendor_ID |
|------------|-------------|-----------|-----------|
| 1          | Laptop      | 1200      | V1        |
| 2          | Mouse       | 25        | V1        |
| 3          | Phone       | 950       | V2        |
| 4          | Headphones  | 150       | V2        |
| 5          | Charger     | 30        | V2        |
| 6          | Tablet      | 600       | V1        |

---

# Summary
- **UNF:** Raw data with repeating groups.  
- **1NF:** Atomic values, no multi-valued fields.  
- **2NF:** Remove partial dependencies (split customers).  
- **3NF:** Remove transitive dependencies (split products, order header/details).  
- **BCNF:** Ensure every determinant is a candidate key (split vendors).  
