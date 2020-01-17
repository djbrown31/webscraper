ALTER TABLE customers
  RENAME COLUMN first TO first_name;

ALTER TABLE customers
  RENAME COLUMN last TO last_name;

ALTER TABLE customers
  ALTER COLUMN first_name TYPE varchar(255),
  ALTER COLUMN last_name TYPE varchar(255);

ALTER TABLE customers
  ALTER COLUMN social TYPE char(9);

ALTER TABLE customers
  ALTER COLUMN account_number TYPE char(14);

ALTER TABLE customers
  ADD line_2 varchar(255);

ALTER TABLE customers
  ALTER COLUMN zip TYPE varchar(5);

ALTER TABLE customers
  DROP COLUMN current_balance_cents;

ALTER TABLE statements
  ALTER COLUMN customer_id SET NOT NULL;

ALTER TABLE statements
  ALTER COLUMN gallons_used TYPE NUMERIC(5, 2);

ALTER TABLE statements
  ALTER COLUMN status SET DEFAULT 'payment_due';



