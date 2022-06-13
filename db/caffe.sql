CREATE TABLE IF NOT EXISTS products(
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS couriers(
    courier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders(
    order_id INT AUTO_INCREMENT,
    product_id INT,
    courier_id INT,
    current_status VARCHAR(255) NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    customer_address VARCHAR(255) NOT NULL,
    customer_phone INT NOT NULL,
    is_completed BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (order_id ),
    FOREIGN KEY (product_id )
        REFERENCES products(product_id )
        ON UPDATE RESTRICT ON DELETE CASCADE,
    FOREIGN KEY (courier_id )
        REFERENCES couriers(courier_id )
        ON UPDATE RESTRICT ON DELETE CASCADE
);
