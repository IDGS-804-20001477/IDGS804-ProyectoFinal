/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80032 (8.0.32)
 Source Host           : localhost:3306
 Source Schema         : luminary_lane

 Target Server Type    : MySQL
 Target Server Version : 80032 (8.0.32)
 File Encoding         : 65001

 Date: 03/04/2023 16:46:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for measurement_units
-- ----------------------------
DROP TABLE IF EXISTS `measurement_units`;
CREATE TABLE `measurement_units`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` tinyint NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of measurement_units
-- ----------------------------

-- ----------------------------
-- Table structure for product_details
-- ----------------------------
DROP TABLE IF EXISTS `product_details`;
CREATE TABLE `product_details`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` float NOT NULL,
  `product_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_product_details_products`(`product_id` ASC) USING BTREE,
  CONSTRAINT `fk_product_details_products` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of product_details
-- ----------------------------

-- ----------------------------
-- Table structure for products
-- ----------------------------
DROP TABLE IF EXISTS `products`;
CREATE TABLE `products`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `sku` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `price` float NOT NULL,
  `size` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `min_value` float NOT NULL,
  `max_value` float NOT NULL,
  `status` tinyint NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of products
-- ----------------------------

-- ----------------------------
-- Table structure for providers
-- ----------------------------
DROP TABLE IF EXISTS `providers`;
CREATE TABLE `providers`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `business_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `contact_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `contact_email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `contact_phone` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` tinyint NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `contact_email_unique`(`contact_email` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of providers
-- ----------------------------

-- ----------------------------
-- Table structure for sale_orders
-- ----------------------------
DROP TABLE IF EXISTS `sale_orders`;
CREATE TABLE `sale_orders`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `reference_number` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `total` float NOT NULL,
  `client_id` int NOT NULL,
  `sale_orders_status_id` int NOT NULL,
  `status` tinyint NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_sale_orders_sale_orders_status`(`sale_orders_status_id` ASC) USING BTREE,
  CONSTRAINT `fk_sale_orders_sale_orders_status` FOREIGN KEY (`sale_orders_status_id`) REFERENCES `sale_orders_status` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sale_orders
-- ----------------------------

-- ----------------------------
-- Table structure for sale_orders_details
-- ----------------------------
DROP TABLE IF EXISTS `sale_orders_details`;
CREATE TABLE `sale_orders_details`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `price` float NOT NULL,
  `product_id` int NOT NULL,
  `sale_orders_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_sale_orders_details_sale_orders`(`sale_orders_id` ASC) USING BTREE,
  INDEX `fk_sale_orders_details_product`(`product_id` ASC) USING BTREE,
  CONSTRAINT `fk_sale_orders_details_product` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_sale_orders_details_sale_orders` FOREIGN KEY (`sale_orders_id`) REFERENCES `sale_orders` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sale_orders_details
-- ----------------------------

-- ----------------------------
-- Table structure for sale_orders_status
-- ----------------------------
DROP TABLE IF EXISTS `sale_orders_status`;
CREATE TABLE `sale_orders_status`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` tinyint NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sale_orders_status
-- ----------------------------
INSERT INTO `sale_orders_status` VALUES (1, 'PEDIDO', 1, '2023-04-03 09:20:26');
INSERT INTO `sale_orders_status` VALUES (2, 'ELABORANDO', 1, '2023-04-03 09:20:49');
INSERT INTO `sale_orders_status` VALUES (3, 'EMPACANDO', 1, '2023-04-03 09:21:04');
INSERT INTO `sale_orders_status` VALUES (4, 'ENVIANDO', 1, '2023-04-03 09:21:23');
INSERT INTO `sale_orders_status` VALUES (5, 'ENTREGADO', 1, '2023-04-03 09:21:33');
INSERT INTO `sale_orders_status` VALUES (6, 'CANCELADO', 1, '2023-04-03 09:47:45');

-- ----------------------------
-- Procedure structure for deleteProduct
-- ----------------------------
DROP PROCEDURE IF EXISTS `deleteProduct`;
delimiter ;;
CREATE PROCEDURE `deleteProduct`(IN pId INT)
BEGIN
	START TRANSACTION;
		/*We eliminate logical form the product*/
		UPDATE products
		SET `status` = 0
		WHERE id = pId;
	COMMIT;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for deleteProvider
-- ----------------------------
DROP PROCEDURE IF EXISTS `deleteProvider`;
delimiter ;;
CREATE PROCEDURE `deleteProvider`(IN pId INT)
BEGIN
	/*We eliminate logical form provider*/
	UPDATE providers
	SET `status` = 0
	WHERE id = pId;
END
;;
delimiter ;

-- ----------------------------
-- Function structure for generateProductSku
-- ----------------------------
DROP FUNCTION IF EXISTS `generateProductSku`;
delimiter ;;
CREATE FUNCTION `generateProductSku`(pName VARCHAR(50))
 RETURNS varchar(20) CHARSET utf8mb4
BEGIN
	DECLARE _sku VARCHAR(20);
	SELECT CONCAT(LEFT(UPPER(pName),2), (FLOOR(RAND() * 401) + 100), RIGHT(NOW(),8)) INTO _sku;
	SELECT REPLACE(_sku,':','') INTO _sku;
	RETURN _sku;
END
;;
delimiter ;

-- ----------------------------
-- Function structure for generateSaleOrderReferenceNumber
-- ----------------------------
DROP FUNCTION IF EXISTS `generateSaleOrderReferenceNumber`;
delimiter ;;
CREATE FUNCTION `generateSaleOrderReferenceNumber`()
 RETURNS varchar(100) CHARSET utf8mb4
BEGIN
	DECLARE numberReference VARCHAR(100);
	SELECT CONCAT('SO-',(FLOOR(RAND() * 401) + 100), RIGHT(NOW(),8)) INTO numberReference;
	SELECT REPLACE(numberReference,':','') INTO numberReference;
	RETURN numberReference;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getMeasurementUnits
-- ----------------------------
DROP PROCEDURE IF EXISTS `getMeasurementUnits`;
delimiter ;;
CREATE PROCEDURE `getMeasurementUnits`(IN pStatus INT)
BEGIN
	SELECT id, `name`
	FROM measurement_units
	WHERE `status` = pStatus;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getProduct
-- ----------------------------
DROP PROCEDURE IF EXISTS `getProduct`;
delimiter ;;
CREATE PROCEDURE `getProduct`(IN pProductId INT)
BEGIN
	SELECT products.id, products.sku, products.`name`, products.price, products.size, product_details.quantity, products.min_value, products.max_value, products.description
	FROM products
	INNER JOIN product_details
		ON product_details.product_id = products.id
	WHERE products.id = pProductId;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getProducts
-- ----------------------------
DROP PROCEDURE IF EXISTS `getProducts`;
delimiter ;;
CREATE PROCEDURE `getProducts`(IN pStatus INT)
BEGIN
	SELECT products.id, products.sku, products.`name`, products.price, products.size, product_details.quantity, products.min_value, products.max_value, products.description
	FROM products
	INNER JOIN product_details
		ON product_details.product_id = products.id
	WHERE products.`status` = pStatus;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getProvider
-- ----------------------------
DROP PROCEDURE IF EXISTS `getProvider`;
delimiter ;;
CREATE PROCEDURE `getProvider`(IN pId INT)
BEGIN
	SELECT id, business_name, contact_name, contact_email, contact_phone, address
	FROM providers
	WHERE id = pId;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getProviders
-- ----------------------------
DROP PROCEDURE IF EXISTS `getProviders`;
delimiter ;;
CREATE PROCEDURE `getProviders`(IN pStatus INT)
BEGIN
	SELECT id, business_name, contact_name, contact_email, contact_phone, address
	FROM providers
	WHERE `status` = pStatus;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getSaleOrder
-- ----------------------------
DROP PROCEDURE IF EXISTS `getSaleOrder`;
delimiter ;;
CREATE PROCEDURE `getSaleOrder`(IN pId INT)
BEGIN
	SELECT sale_orders.id, sale_orders.reference_number, sale_orders.total, sale_orders.client_id, sale_orders_details.price, sale_orders_details.quantity, sale_orders_status.`name`, products.`name`
	FROM sale_orders
	INNER JOIN sale_orders_details
		ON sale_orders_details.sale_orders_id = sale_orders.id
	INNER JOIN sale_orders_status
		ON sale_orders_status.id = sale_orders.sale_orders_status_id
	INNER JOIN products
		ON products.id = sale_orders_details.product_id
	WHERE sale_orders.id = pId;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getSaleOrders
-- ----------------------------
DROP PROCEDURE IF EXISTS `getSaleOrders`;
delimiter ;;
CREATE PROCEDURE `getSaleOrders`()
BEGIN
	SELECT sale_orders.id, sale_orders.reference_number, sale_orders.total, sale_orders.client_id, sale_orders_details.price, sale_orders_details.quantity, sale_orders_status.`name`, products.`name`
	FROM sale_orders
	INNER JOIN sale_orders_details
		ON sale_orders_details.sale_orders_id = sale_orders.id
	INNER JOIN sale_orders_status
		ON sale_orders_status.id = sale_orders.sale_orders_status_id
	INNER JOIN products
		ON products.id = sale_orders_details.product_id
	WHERE sale_orders.`status` = 1;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getSaleOrderStatus
-- ----------------------------
DROP PROCEDURE IF EXISTS `getSaleOrderStatus`;
delimiter ;;
CREATE PROCEDURE `getSaleOrderStatus`()
BEGIN
	SELECT id, `name`
	FROM sale_orders_status;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for insertProduct
-- ----------------------------
DROP PROCEDURE IF EXISTS `insertProduct`;
delimiter ;;
CREATE PROCEDURE `insertProduct`(IN pName VARCHAR(50),
IN pDescription VARCHAR(255),
IN pPrice FLOAT,
IN pSize VARCHAR(5),
IN pMinValue FLOAT,
IN pMaxValue FLOAT,

/*Product Details data*/
IN pQuantity FLOAT)
BEGIN
	DECLARE product_id_generate INT;
	
	START TRANSACTION;
		/*We insert a product and get the id*/
		INSERT INTO products(sku, `name`, description, price, size, min_value, max_value, created_at)
		VALUES(generateProductSku(pName), pName, pDescription, pPrice, pSize, pMinValue, pMaxValue, NOW());
		SET product_id_generate = LAST_INSERT_ID();
		
		/*We insert a detail to product*/
		INSERT INTO product_details(quantity, product_id)
		VALUES(pQuantity, product_id_generate);
	COMMIT;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for insertProvider
-- ----------------------------
DROP PROCEDURE IF EXISTS `insertProvider`;
delimiter ;;
CREATE PROCEDURE `insertProvider`(IN pBusiness_name VARCHAR(50),
IN pContact_name VARCHAR(100),
IN pContact_email VARCHAR(50),
IN pContact_phone VARCHAR(10),
IN pAddress VARCHAR(255))
BEGIN
	START TRANSACTION;
		INSERT INTO providers(business_name, contact_name, contact_email, contact_phone, address, created_at)
		VALUES(pBusiness_name, pContact_name, pContact_email, pContact_phone, pAddress, NOW());
	COMMIT;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for insertSaleOrder
-- ----------------------------
DROP PROCEDURE IF EXISTS `insertSaleOrder`;
delimiter ;;
CREATE PROCEDURE `insertSaleOrder`(IN pTotal FLOAT,
IN pClient_id INT,

/*Data sale_order detail*/
IN pJson_Details JSON)
BEGIN
	DECLARE sale_order_header_id, length_array, i, _quantity, _product_id INT;
	DECLARE _price FLOAT;
	DECLARE product_json VARCHAR(4000);
	
	START TRANSACTION;
		/*First, we insert sale_order header for get the ID*/
		INSERT INTO sale_orders(reference_number, total, client_id, sale_orders_status_id, created_at)
		VALUES (generateSaleOrderReferenceNumber(), pTotal, pClient_id, 1, NOW());
		SET sale_order_header_id = LAST_INSERT_ID();
		
		/*And we insert the sale_order detail*/
		SET length_array = JSON_LENGTH(pJson_Details);
		SET i = 0;
		WHILE i < length_array DO
			SELECT JSON_EXTRACT(pJson_Details, CONCAT( '$[', i, ']' )) INTO product_json;
			SELECT JSON_EXTRACT(product_json, '$.quantity') INTO _quantity;
			SELECT JSON_EXTRACT(product_json, '$.price') INTO _price;
			SELECT JSON_EXTRACT(product_json, '$.product_id') INTO _product_id;
			
			INSERT INTO sale_orders_details(quantity, price, product_id, sale_orders_id)
			VALUES(_quantity, _price, _product_id, sale_order_header_id);
			
			SET i = i + 1;
		END WHILE;
	COMMIT;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for updateProduct
-- ----------------------------
DROP PROCEDURE IF EXISTS `updateProduct`;
delimiter ;;
CREATE PROCEDURE `updateProduct`(IN pId INT,
IN pSku VARCHAR(100),
IN pName VARCHAR(50),
IN pDescription VARCHAR(255),
IN pPrice FLOAT,
IN pSize VARCHAR(5),
IN pMinValue FLOAT,
IN pMaxValue FLOAT,

/*Product Details data*/
IN pQuantity FLOAT)
BEGIN
	START TRANSACTION;
		/*We update product header*/
		UPDATE products 
		SET sku = pSku,
				`name` = pName,
				description = pDescription,
				price = pPrice,
				size = pSize,
				min_value = pMinValue,
				max_value = pMaxValue
		WHERE id = pId;
		
		/*We update product detail*/
		UPDATE product_details
		SET quantity = pQuantity
		WHERE product_id = pId;
	COMMIT;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for updateProvider
-- ----------------------------
DROP PROCEDURE IF EXISTS `updateProvider`;
delimiter ;;
CREATE PROCEDURE `updateProvider`(IN pId INT,
IN pBusiness_name VARCHAR(50),
IN pContact_name VARCHAR(100),
IN pContact_email VARCHAR(50),
IN pContact_phone VARCHAR(10),
IN pAddress VARCHAR(255))
BEGIN
	START TRANSACTION;
		UPDATE providers
		SET business_name = pBusiness_name,
				contact_name = pContact_name,
				contact_email = pContact_email,
				contact_phone = pContact_phone,
				address = pAddress
		WHERE id = pId;
	COMMIT;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for updateSaleOrder
-- ----------------------------
DROP PROCEDURE IF EXISTS `updateSaleOrder`;
delimiter ;;
CREATE PROCEDURE `updateSaleOrder`(IN pId INT, IN pStatus INT)
BEGIN
	START TRANSACTION;
		/*We update the status of the sales order to the new one we obtain in the function parameters*/
		UPDATE sale_orders
		SET sale_orders_status_id = pStatus
		WHERE id = pId;
	COMMIT;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
