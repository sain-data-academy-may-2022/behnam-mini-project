# from unittest import TestCase
# import mysql.connector
# from mysql.connector import errorcode
# from mock import patch


# MYSQL_USER = "root"
# MYSQL_PASSWORD = "password"
# MYSQL_DB = "testdb"
# MYSQL_HOST = "localhost"
# MYSQL_PORT = "3306"

# config = {
#     'host': MYSQL_HOST,
#     'user': MYSQL_USER,
#     'password': MYSQL_PASSWORD,
#     'database': MYSQL_DB
# }

# class MockDB(TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cnx = mysql.connector.connect(
#             host=MYSQL_HOST,
#             user=MYSQL_USER,
#             password=MYSQL_PASSWORD,
#             port = MYSQL_PORT
#         )
#         cursor = cnx.cursor(dictionary=True)

#         # drop database if it already exists
#         try:
#             cursor.execute("DROP DATABASE {}".format(MYSQL_DB))
#             cursor.close()
#             print("DB dropped")
#         except mysql.connector.Error as err:
#             print("{}{}".format(MYSQL_DB, err))

#         cursor = cnx.cursor(dictionary=True)
#         try:
#             cursor.execute(
#                 "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(MYSQL_DB))
#         except mysql.connector.Error as err:
#             print("Failed creating database: {}".format(err))
#             exit(1)
#         cnx.database = MYSQL_DB

#         query = """
#             CREATE TABLE `products` (
#                     `product_id` INT AUTO_INCREMENT PRIMARY KEY ,
#                     `name` VARCHAR(255) NOT NULL
#                     );
#                 """
#         cursor.execute(query)
#         cnx.commit()

#         query = """
#             CREATE TABLE IF NOT EXISTS couriers(
#                 courier_id INT AUTO_INCREMENT PRIMARY KEY,
#                 name VARCHAR(255) NOT NULL
#             );
#                 """

#         cursor.execute(query)
#         cnx.commit()

#         query = """
#             CREATE TABLE IF NOT EXISTS orders(
#                 order_id INT AUTO_INCREMENT,
#                 product_id INT,
#                 courier_id INT,
#                 current_status VARCHAR(255) NOT NULL,
#                 customer_name VARCHAR(255) NOT NULL,
#                 customer_address VARCHAR(255) NOT NULL,
#                 customer_phone INT NOT NULL,
#                 is_completed BOOLEAN NOT NULL DEFAULT FALSE,
#                 PRIMARY KEY (order_id ),
#                 FOREIGN KEY (product_id )
#                     REFERENCES products(product_id )
#                     ON UPDATE RESTRICT ON DELETE CASCADE,
#                 FOREIGN KEY (courier_id )
#                     REFERENCES couriers(courier_id )
#                     ON UPDATE RESTRICT ON DELETE CASCADE
#             );
#                 """
#         cursor.execute(query)
#         cnx.commit()

#         insert_data_query = """INSERT INTO `products` (`name`) VALUES
#                             ('test_product_1'),
#                             ('test_product_2')"""
#         try:
#             cursor.execute(insert_data_query)
#             cnx.commit()
#         except mysql.connector.Error as err:
#             print("Data insertion to products failed \n" + err)

#         insert_data_query = """INSERT INTO `couriers` (`name`) VALUES
#                             ('test_courier_1'),
#                             ('test_courier_2')"""
#         try:
#             cursor.execute(insert_data_query)
#             cnx.commit()
#         except mysql.connector.Error as err:
#             print("Data insertion to couriers failed \n" + err)


#         insert_data_query = """INSERT INTO `orders`
#         (`product_id`,
#          `courier_id`,
#          `current_status`,
#          `customer_name`,
#          `customer_address`,
#          `customer_phone`)
#         VALUES
#         (1, 1, 'Out for delivery', 'Jack', 'test_address_1', 77777777),
#         (2, 2, 'Preparing', 'Leo', 'test_address_2', 88888888),
#         (2, 1, 'Preparing', 'Fabio', 'test_address_3', 99999999),
#         (1, 2, 'Preparing', 'Jessica', 'test_address_4', 99999999)
#         """
#         try:
#             cursor.execute(insert_data_query)
#             cnx.commit()
#         except mysql.connector.Error as err:
#             print("Data insertion to couriers failed \n" + err)

#         cursor.close()
#         cnx.close()

#         testconfig ={
#             'host': MYSQL_HOST,
#             'user': MYSQL_USER,
#             'password': MYSQL_PASSWORD,
#             'database': MYSQL_DB
#         }
#         cls.mock_db_config = patch.dict(config, testconfig)

#     @classmethod
#     def tearDownClass(cls):
#         cnx = mysql.connector.connect(
#             host=MYSQL_HOST,
#             user=MYSQL_USER,
#             password=MYSQL_PASSWORD
#         )
#         cursor = cnx.cursor(dictionary=True)

#         # drop test database
#         try:
#             cursor.execute("DROP DATABASE {}".format(MYSQL_DB))
#             cnx.commit()
#             cursor.close()
#         except mysql.connector.Error as err:
#             print("Database {} does not exists. Dropping db failed".format(MYSQL_DB))
#         cnx.close()
