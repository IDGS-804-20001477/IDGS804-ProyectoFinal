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

 Date: 05/04/2023 17:52:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;
SET GLOBAL log_bin_trust_function_creators = 1;

-- ----------------------------
-- Table structure for feedstock_details
-- ----------------------------
DROP TABLE IF EXISTS `feedstock_details`;
CREATE TABLE `feedstock_details`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` float NOT NULL,
  `feedstock_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `feedstock_details_feedstock`(`feedstock_id` ASC) USING BTREE,
  CONSTRAINT `feedstock_details_feedstock` FOREIGN KEY (`feedstock_id`) REFERENCES `feedstocks` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of feedstock_details
-- ----------------------------

-- ----------------------------
-- Table structure for feedstocks
-- ----------------------------
DROP TABLE IF EXISTS `feedstocks`;
CREATE TABLE `feedstocks`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `price` float NOT NULL,
  `status` tinyint NULL DEFAULT 1,
  `measurement_unit_id` int NOT NULL,
  `provider_id` int NOT NULL,
  `min_value` float NOT NULL,
  `max_value` float NOT NULL,
  `created_at` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `feedstock_measurement`(`measurement_unit_id` ASC) USING BTREE,
  INDEX `feedstock_provider`(`provider_id` ASC) USING BTREE,
  CONSTRAINT `feedstock_measurement` FOREIGN KEY (`measurement_unit_id`) REFERENCES `measurement_units` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `feedstock_provider` FOREIGN KEY (`provider_id`) REFERENCES `providers` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of feedstocks
-- ----------------------------

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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of providers
-- ----------------------------

-- ----------------------------
-- Table structure for recipe_details
-- ----------------------------
DROP TABLE IF EXISTS `recipe_details`;
CREATE TABLE `recipe_details`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `recipe_id` int NOT NULL,
  `feedstock_id` int NOT NULL,
  `quantity` float NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_recipe_details_recipe_id_recipe_id`(`recipe_id` ASC) USING BTREE,
  INDEX `fk_recipe_details_feedstock_id_feedstock_id`(`feedstock_id` ASC) USING BTREE,
  CONSTRAINT `fk_recipe_details_feedstock_id_feedstock_id` FOREIGN KEY (`feedstock_id`) REFERENCES `feedstocks` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_recipe_details_recipe_id_recipe_id` FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of recipe_details
-- ----------------------------

-- ----------------------------
-- Table structure for recipes
-- ----------------------------
DROP TABLE IF EXISTS `recipes`;
CREATE TABLE `recipes`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `status` tinyint NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_recipe_product_id_product_id`(`product_id` ASC) USING BTREE,
  CONSTRAINT `fk_recipe_product_id_product_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of recipes
-- ----------------------------

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `status` tinyint NULL DEFAULT NULL,
  `created_at` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES (1, 'admin', NULL, 1, '2023-04-05 12:04:29');
INSERT INTO `role` VALUES (2, 'client', NULL, 1, '2023-04-05 12:04:39');

-- ----------------------------
-- Table structure for roles_users
-- ----------------------------
DROP TABLE IF EXISTS `roles_users`;
CREATE TABLE `roles_users`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NULL DEFAULT NULL,
  `role_id` int NULL DEFAULT NULL,
  `status` tinyint NULL DEFAULT NULL,
  `created_at` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_id`(`user_id` ASC) USING BTREE,
  INDEX `role_id`(`role_id` ASC) USING BTREE,
  CONSTRAINT `roles_users_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `roles_users_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of roles_users
-- ----------------------------
INSERT INTO `roles_users` VALUES (1, 1, 1, 1, '2023-04-05 12:04:56');

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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

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
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

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
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `type` int NOT NULL,
  `active` tinyint(1) NULL DEFAULT NULL,
  `confirmed_at` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'garnicalunamauricio@gmail.com', 'sha256$E5nAz28zbf1xf6Xz$7972d265317d18ccf00badf45350ddf6c6226f688b1761d51eb13f775abe0f08', 2, 1, '2023-04-05 12:04:13');

-- ----------------------------
-- Table structure for user_profile
-- ----------------------------
DROP TABLE IF EXISTS `user_profile`;
CREATE TABLE `user_profile`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `lastname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `user_profile_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_profile
-- ----------------------------

-- ----------------------------
-- Table structure for user_types
-- ----------------------------
DROP TABLE IF EXISTS `user_types`;
CREATE TABLE `user_types`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` tinyint NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_types
-- ----------------------------
INSERT INTO `user_types` VALUES (1, 'SUPERADMIN', 1, '2023-04-05 13:21:21');
INSERT INTO `user_types` VALUES (2, 'CLIENTE', 1, '2023-04-05 13:21:36');
INSERT INTO `user_types` VALUES (3, 'EMPLEADO', 1, '2023-04-05 13:21:46');

-- ----------------------------
-- Function structure for checkFeedstockQuantity
-- ----------------------------
DROP FUNCTION IF EXISTS `checkFeedstockQuantity`;
delimiter ;;
CREATE FUNCTION `checkFeedstockQuantity`(pId INT)
 RETURNS float
BEGIN
	DECLARE feedstock_quantity FLOAT;
	SELECT quantity FROM feedstock_details WHERE feedstock_id = pId INTO feedstock_quantity;
	RETURN feedstock_quantity;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for deleteFeedstock
-- ----------------------------
DROP PROCEDURE IF EXISTS `deleteFeedstock`;
delimiter ;;
CREATE PROCEDURE `deleteFeedstock`(IN pId INT)
BEGIN
	START TRANSACTION;
		/*We eliminate logical form the feedstock*/
		UPDATE Feedstocks
		SET `status` = 0
		WHERE id = pId;
	COMMIT;
END
;;
delimiter ;

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
-- Procedure structure for deleteRecipe
-- ----------------------------
DROP PROCEDURE IF EXISTS `deleteRecipe`;
delimiter ;;
CREATE PROCEDURE `deleteRecipe`(IN pId INT)
BEGIN
	START TRANSACTION;
		/*We logically eliminate the recipe*/
		UPDATE recipes
		SET `status` = 0
		WHERE id = pId;
	COMMIT;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for deleteUser
-- ----------------------------
DROP PROCEDURE IF EXISTS `deleteUser`;
delimiter ;;
CREATE PROCEDURE `deleteUser`(IN pId INT)
BEGIN
	START TRANSACTION;
		/*We logically eliminate the user*/
		UPDATE `user`
		SET active = 0
		WHERE id = pId;
	COMMIT;
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
-- Procedure structure for getFeedstock
-- ----------------------------
DROP PROCEDURE IF EXISTS `getFeedstock`;
delimiter ;;
CREATE PROCEDURE `getFeedstock`(IN pFeedstockId INT)
BEGIN
	SELECT feedstocks.id, feedstocks.`name`, feedstocks.price, feedstock_details.quantity, feedstocks.min_value, feedstocks.max_value, feedstocks.description, feedstocks.measurement_unit_id, feedstocks.provider_id
	FROM feedstocks
	INNER JOIN feedstock_details
		ON feedstock_details.feedstock_id = feedstocks.id
	WHERE feedstocks.id = pFeedstockId;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getFeedstocks
-- ----------------------------
DROP PROCEDURE IF EXISTS `getFeedstocks`;
delimiter ;;
CREATE PROCEDURE `getFeedstocks`(IN pStatus INT)
BEGIN
	SELECT feedstocks.id, feedstocks.`name`, feedstocks.price, feedstock_details.quantity, feedstocks.min_value, feedstocks.max_value, feedstocks.description, feedstocks.measurement_unit_id, feedstocks.provider_id
	FROM feedstocks
	INNER JOIN feedstock_details
		ON feedstock_details.feedstock_id = feedstocks.id
	WHERE feedstocks.`status` = pStatus;
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
-- Procedure structure for getRecipe
-- ----------------------------
DROP PROCEDURE IF EXISTS `getRecipe`;
delimiter ;;
CREATE PROCEDURE `getRecipe`(IN pId INT)
BEGIN
	SELECT recipes.id, recipes.product_id, products.`name`, recipes.description, recipe_details.id as detail_id, recipe_details.feedstock_id, feedstocks.`name` as name_feedstock, recipe_details.quantity
	FROM recipes
	INNER JOIN products
		ON products.id = recipes.product_id
	INNER JOIN recipe_details
		ON recipe_details.recipe_id = recipes.id
	INNER JOIN feedstocks
		ON feedstocks.id = recipe_details.feedstock_id
	WHERE recipes.id = pId;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getRecipes
-- ----------------------------
DROP PROCEDURE IF EXISTS `getRecipes`;
delimiter ;;
CREATE PROCEDURE `getRecipes`(IN pStatus INT)
BEGIN
	SELECT recipes.id, products.`name`, recipes.description
	FROM recipes
	INNER JOIN products
		ON products.id = recipes.product_id
	WHERE recipes.`status` = pStatus;
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
-- Procedure structure for getUser
-- ----------------------------
DROP PROCEDURE IF EXISTS `getUser`;
delimiter ;;
CREATE PROCEDURE `getUser`(IN pId INT)
BEGIN
	SELECT `user`.id, `user`.email, `user`.`password`, user_profile.id as user_profile_id, user_profile.`name`, user_profile.lastname, user_profile.phone, user_profile.address
	FROM `user`
	LEFT JOIN user_profile
		ON user_profile.user_id = `user`.id
	WHERE `user`.id = pId;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getUsers
-- ----------------------------
DROP PROCEDURE IF EXISTS `getUsers`;
delimiter ;;
CREATE PROCEDURE `getUsers`(IN pStatus INT)
BEGIN
	SELECT `user`.id, `user`.email, `user`.`password`, user_profile.id as user_profile_id, user_profile.`name`, user_profile.lastname, user_profile.phone, user_profile.address
	FROM `user`
	LEFT JOIN user_profile
		ON user_profile.user_id = `user`.id
	WHERE `user`.active = pStatus;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getUserTypes
-- ----------------------------
DROP PROCEDURE IF EXISTS `getUserTypes`;
delimiter ;;
CREATE PROCEDURE `getUserTypes`(IN pStatus INT)
BEGIN
	SELECT id, `name`
	FROM user_types
	WHERE `status` = pStatus;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for insertFeedstock
-- ----------------------------
DROP PROCEDURE IF EXISTS `insertFeedstock`;
delimiter ;;
CREATE PROCEDURE `insertFeedstock`(IN pName VARCHAR(150),
IN pDescription VARCHAR(255),
IN pPrice FLOAT,
IN pMinValue FLOAT,
IN pMaxValue FLOAT,

/*measurement_units data*/
IN pMeasurement_unit_id INT,

/*providers data*/
IN pProvider_id INT,

/*Feedstock Details data*/
IN pQuantity FLOAT)
BEGIN
	DECLARE feedstock_id_generate INT;
	
	START TRANSACTION;
		/*We insert a feedstock and get the id*/
		INSERT INTO feedstocks(`name`, description, price, min_value, max_value, measurement_unit_id, provider_id, created_at)
		VALUES(pName, pDescription, pPrice, pMinValue, pMaxValue, pMeasurement_unit_id, pProvider_id, NOW());
		SET feedstock_id_generate = LAST_INSERT_ID();
		
		/*We insert a detail to feedstock*/
		INSERT INTO feedstock_details(quantity, feedstock_id)
		VALUES(pQuantity, feedstock_id_generate);
	COMMIT;
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
-- Procedure structure for insertRecipe
-- ----------------------------
DROP PROCEDURE IF EXISTS `insertRecipe`;
delimiter ;;
CREATE PROCEDURE `insertRecipe`(IN pProduct_id INT,
IN pDescription VARCHAR(255),

/*Recipe detail*/
IN pJson_details JSON)
BEGIN
	DECLARE recipe_header_id, i, _feedstock_id INT;
	DECLARE _quantity FLOAT;
	DECLARE recipe_detail_json VARCHAR(1000);

	START TRANSACTION;
		/*We insert the recipe header*/
		INSERT INTO recipes(product_id, description, created_at)
		VALUES(pProduct_id, pDescription, NOW());
		SET recipe_header_id = LAST_INSERT_ID();
		
		/*Let's go through the detail arrangement of the recipe*/
		SET i = 0;
		WHILE i < JSON_LENGTH(pJson_details) DO
			SELECT JSON_EXTRACT(pJson_Details, CONCAT( '$[', i, ']' )) INTO recipe_detail_json;
			SELECT JSON_EXTRACT(recipe_detail_json, '$.quantity') INTO _quantity;
			SELECT JSON_EXTRACT(recipe_detail_json, '$.feedstock_id') INTO _feedstock_id;
			
			/*We insert the recipe details*/
			INSERT INTO recipe_details(recipe_id, feedstock_id, quantity)
			VALUES(recipe_header_id, _feedstock_id, _quantity);
		END WHILE;
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
-- Procedure structure for insertUser
-- ----------------------------
DROP PROCEDURE IF EXISTS `insertUser`;
delimiter ;;
CREATE PROCEDURE `insertUser`(IN pEmail VARCHAR(100),
IN pPassword VARCHAR(255),
IN pType INT,

/*Data user profile*/
IN pName VARCHAR(50),
IN pLastname VARCHAR(50),
IN pAddress VARCHAR(100),
IN pPhone VARCHAR(10))
BEGIN
	DECLARE user_id_generate INT;

	START TRANSACTION;
		/*We insert the user auth*/
		INSERT INTO `user`(email, `password`, type, active, confirmed_at)
		VALUES(pEmail, pPassword, pType, 1, NOW());
		SET user_id_generate = LAST_INSERT_ID();
		
		/*We insert the user profile*/
		INSERT INTO user_profile(`name`, lastname, address, phone, user_id)
		VALUES(pName, pLastname, pAddress, pPhone, user_id_generate);
	COMMIT;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for updateFeedstock
-- ----------------------------
DROP PROCEDURE IF EXISTS `updateFeedstock`;
delimiter ;;
CREATE PROCEDURE `updateFeedstock`(IN pId INT,
IN pName VARCHAR(150),
IN pDescription VARCHAR(255),
IN pPrice FLOAT,
IN pMinValue FLOAT,
IN pMaxValue FLOAT,

/*measurement_units data*/
IN pMeasurement_unit_id INT,

/*providers data*/
IN pProvider_id INT,

/*Product Details data*/
IN pQuantity FLOAT)
BEGIN
	START TRANSACTION;
		/*We update feedstocks header*/
		UPDATE feedstocks 
		SET `name` = pName,
				description = pDescription,
				price = pPrice,
				min_value = pMinValue,
				max_value = pMaxValue,
				measurement_unit_id = pMeasurement_unit_id,
				provider_id = pProvider_id
		WHERE id = pId;
		
		/*We update feedstock details*/
		UPDATE feedstock_details
		SET quantity = pQuantity
		WHERE feedstock_id = pId;
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
-- Procedure structure for updateRecipe
-- ----------------------------
DROP PROCEDURE IF EXISTS `updateRecipe`;
delimiter ;;
CREATE PROCEDURE `updateRecipe`(IN pId INT,
IN pProduct_id INT,
IN pDescription VARCHAR(255),

/*Recipe detail*/
IN pJson_details JSON)
BEGIN
	DECLARE i, _feedstock_id, _recipe_details_id INT;
	DECLARE _quantity FLOAT;
	DECLARE recipe_detail_json VARCHAR(1000);

	START TRANSACTION;
		/*We update the recipe header*/
		UPDATE recipes
		SET product_id = pProduct_id,
				description = pDescription
		WHERE id = pId;
		
		/*Let's go through the detail arrangement of the recipe*/
		SET i = 0;
		WHILE i < JSON_LENGTH(pJson_details) DO
			SELECT JSON_EXTRACT(pJson_Details, CONCAT( '$[', i, ']' )) INTO recipe_detail_json;
			SELECT JSON_EXTRACT(recipe_detail_json, '$.quantity') INTO _quantity;
			SELECT JSON_EXTRACT(recipe_detail_json, '$.feedstock_id') INTO _feedstock_id;
			SELECT JSON_EXTRACT(recipe_detail_json, '$.id') INTO _recipe_details_id;
			
			/*We update the recipe detail*/
			UPDATE recipe_details
			SET quantity = _quantity,
					feedstock_id = _feedstock_id
			WHERE id = _recipe_details_id;
		END WHILE;
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
	DECLARE quantity_ INT;

	START TRANSACTION;
		/*We update the status of the sales order to the new one we obtain in the function parameters*/
		UPDATE sale_orders
		SET sale_orders_status_id = pStatus
		WHERE id = pId;
		
		IF(pStatus = 4) THEN
			SELECT product_details.id, product_details.quantity
			FROM product_details
			INNER JOIN sale_orders_details
				ON sale_orders_details.product_id = product_details.product_id
			INNER JOIN sale_orders
				ON sale_orders.id = sale_orders_details.sale_orders_id
			WHERE sale_orders.id = pId;
			
			UPDATE product_details
			SET quantity = quantity - quantity_
			WHERE id = pId;
			
			UPDATE sale_orders
			SET sale_orders_status_id = pStatus
			WHERE id = pId;
		END IF;
	COMMIT;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for updateUser
-- ----------------------------
DROP PROCEDURE IF EXISTS `updateUser`;
delimiter ;;
CREATE PROCEDURE `updateUser`(IN pId INT,
IN pEmail VARCHAR(100),
IN pPassword VARCHAR(255),
IN pType INT,

/*Data user profile*/
IN pName VARCHAR(50),
IN pLastname VARCHAR(50),
IN pAddress VARCHAR(100),
IN pPhone VARCHAR(10))
BEGIN
	START TRANSACTION;
		/*We update the user auth*/
		UPDATE `user`
		SET email = pEmail,
				`password` = pPassword,
				type = pType
		WHERE id = pId;
		
		/*We update the user profile*/
		UPDATE user_profile
		SET `name` = pName,
				lastname = pLastname,
				address = pAddress,
				phone = pPhone
		WHERE user_id = pId;
	COMMIT;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
