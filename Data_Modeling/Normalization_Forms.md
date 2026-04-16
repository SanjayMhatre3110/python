# Database Normalization Walkthrough

## Unnormalized Form (UNF)
**Description:**  
UNF is the raw form of data where there is no structure or normalization applied. Data may contain repeating groups, multiple values in a single field, and lacks consistency.

**Key Characteristics:**
- Repeating groups allowed
- Multi-valued attributes exist
- Difficult to query and maintain

**Difference from others:**  
This is the starting point — all other normal forms improve upon UNF by reducing redundancy and improving structure.

| OrderID | CustomerName | CustomerAddress | Products                  | TotalAmount |
|---------|--------------|-----------------|---------------------------|-------------|
| 101     | John Smith   | 12 Main St      | Laptop, Mouse             | 1200        |
| 102     | Alice Brown  | 45 Oak Ave      | Phone, Headphones, Charger| 950         |
| 103     | Bob White    | 78 Pine Rd      | Tablet                    | 600         |

---

## First Normal Form (1NF)
**Description:**  
1NF ensures that each column contains atomic (indivisible) values and each record is unique. It removes repeating groups and multi-valued attributes.

**Key Characteristics:**
- No multi-valued attributes
- Each field contains only one value
- Rows are uniquely identifiable

**Difference from UNF:**  
- Eliminates repeating groups  
- Converts multi-valued fields into multiple rows  

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
**Description:**  
2NF removes partial dependencies. This means that non-key attributes must depend on the entire primary key, not just part of it (important when using composite keys).

**Key Characteristics:**
- Must already be in 1NF
- No partial dependency on composite keys
- Data split into related tables

**Difference from 1NF:**  
- Removes redundancy caused by partial dependency  
- Separates data into multiple tables (e.g., Customer and Order)

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
**Description:**  
3NF removes transitive dependencies, meaning non-key attributes should not depend on other non-key attributes.

**Key Characteristics:**
- Must already be in 2NF
- No transitive dependencies
- Better logical data separation

**Difference from 2NF:**  
- Eliminates indirect relationships between non-key attributes  
- Introduces more refined tables (e.g., Product, Order Header, Order Details)

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
**Description:**  
BCNF is a stricter version of 3NF. It ensures that every determinant (attribute that determines another) is a candidate key.

**Key Characteristics:**
- Must already be in 3NF
- Every functional dependency must have a candidate key as determinant
- Handles edge cases not covered by 3NF

**Difference from 3NF:**  
- Stricter rule for functional dependencies  
- Removes anomalies caused by non-candidate key determinants  

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

| Form | Focus | Main Improvement |
|------|------|------------------|
| UNF  | Raw Data | No structure |
| 1NF  | Atomicity | Removes repeating groups |
| 2NF  | Full Dependency | Removes partial dependency |
| 3NF  | Transitive Dependency | Removes indirect relationships |
| BCNF | Strong Dependency Rules | Ensures all determinants are candidate keys |
