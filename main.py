import sqlite3
import pandas as pd 

conn = sqlite3.connect("data.sqlite")

# Displaying the product details along with the order details
q = """
SELECT *
FROM orderdetails AS od
      JOIN products AS p
      ON od.productid = p.productid
      LIMIT 10;
"""
print(pd.read_sql(q, conn))


q = """
SELECT *
FROM products AS p
      LEFT JOIN orderdetails AS od
      USING(productcode)
      LIMIT 10;
"""
print(pd.read_sql(q, conn))