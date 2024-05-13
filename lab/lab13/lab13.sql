.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price
  FROM products
  GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price)
  FROM inventory
  GROUP BY item;


CREATE TABLE shopping_list_helper AS
  SELECT name, store, MIN(MSRP / rating) AS best_deal
  FROM products, lowest_prices
  WHERE products.name = lowest_prices.item
  GROUP BY category;


CREATE TABLE shopping_list AS
  SELECT name, store
  FROM shopping_list_helper;


CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs)
  FROM stores, shopping_list
  WHERE stores.store = shopping_list.store;

