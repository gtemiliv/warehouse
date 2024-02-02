CREATE TABLE products
(
    "id"    SERIAL PRIMARY KEY,
    "name"  TEXT NOT NULL,
    "quantity"  DECIMAL,
    "unit"  TEXT CHECK ("unit" IN ('pcs', 'set')),
    "price"     DECIMAL,
    "currency"  TEXT CHECK ("currency" IN ('PLN', 'EUR')),
    "receipt_date"  TIMESTAMP,
    "product_condition" TEXT CHECK ("product_condition" IN ('new', 'used', 'damaged'))
);