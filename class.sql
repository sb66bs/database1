/*
 Navicat Premium Dump SQL

 Source Server         : 课设
 Source Server Type    : MySQL
 Source Server Version : 80042 (8.0.42)
 Source Host           : localhost:3306
 Source Schema         : class

 Target Server Type    : MySQL
 Target Server Version : 80042 (8.0.42)
 File Encoding         : 65001

 Date: 21/05/2025 12:18:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for device
-- ----------------------------
DROP TABLE IF EXISTS `device`;
CREATE TABLE `device`  (
  `DeviceID` int NOT NULL,
  `DeviceName` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Model` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `PurchaseDate` date NULL DEFAULT NULL,
  `PurchaseCost` decimal(10, 2) NULL DEFAULT NULL,
  `Status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`DeviceID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of device
-- ----------------------------
INSERT INTO `device` VALUES (1, '设备A', '型号X1', '2022-01-01', 1000.00, '使用中');
INSERT INTO `device` VALUES (2, '设备B', '型号X2', '2022-02-01', 1500.00, '维修中');
INSERT INTO `device` VALUES (3, '设备C', '型号X3', '2022-03-01', 2000.00, '使用中');
INSERT INTO `device` VALUES (4, '设备D', '型号X4', '2022-04-01', 2500.00, '报废');
INSERT INTO `device` VALUES (5, '设备E', '型号X5', '2022-05-01', 3000.00, '使用中');
INSERT INTO `device` VALUES (6, '设备F', '型号X6', '2022-06-01', 3500.00, '使用中');
INSERT INTO `device` VALUES (7, '设备G', '型号X7', '2022-07-01', 4000.00, '维修中');
INSERT INTO `device` VALUES (8, '设备H', '型号X8', '2022-08-01', 4500.00, '使用中');
INSERT INTO `device` VALUES (9, '设备I', '型号X9', '2022-09-01', 5000.00, '使用中');
INSERT INTO `device` VALUES (10, '设备J', '型号X10', '2022-10-01', 5500.00, '使用中');

-- ----------------------------
-- Table structure for devicerepair
-- ----------------------------
DROP TABLE IF EXISTS `devicerepair`;
CREATE TABLE `devicerepair`  (
  `RepairID` int NOT NULL,
  `DeviceID` int NOT NULL,
  `RepairDate` date NULL DEFAULT NULL,
  `RepairContent` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `RepairCost` decimal(10, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`RepairID`) USING BTREE,
  INDEX `DeviceID`(`DeviceID` ASC) USING BTREE,
  CONSTRAINT `devicerepair_ibfk_1` FOREIGN KEY (`DeviceID`) REFERENCES `device` (`DeviceID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of devicerepair
-- ----------------------------
INSERT INTO `devicerepair` VALUES (1, 2, '2023-02-01', '更换电池', 150.00);
INSERT INTO `devicerepair` VALUES (2, 4, '2023-02-02', '修复电机', 300.00);
INSERT INTO `devicerepair` VALUES (3, 6, '2023-02-03', '更换电缆', 200.00);
INSERT INTO `devicerepair` VALUES (4, 8, '2023-02-04', '软件更新', 100.00);
INSERT INTO `devicerepair` VALUES (5, 10, '2023-02-05', '更换屏幕', 150.00);
INSERT INTO `devicerepair` VALUES (6, 1, '2023-02-06', '更换键盘', 75.00);
INSERT INTO `devicerepair` VALUES (7, 3, '2023-02-07', '清理内部', 50.00);
INSERT INTO `devicerepair` VALUES (8, 5, '2023-02-08', '修理电源', 80.00);
INSERT INTO `devicerepair` VALUES (9, 7, '2023-02-09', '更换电池', 120.00);
INSERT INTO `devicerepair` VALUES (10, 9, '2023-02-10', '更换传感器', 150.00);

-- ----------------------------
-- Table structure for devicescrap
-- ----------------------------
DROP TABLE IF EXISTS `devicescrap`;
CREATE TABLE `devicescrap`  (
  `ScrapID` int NOT NULL,
  `DeviceID` int NOT NULL,
  `ScrapDate` date NULL DEFAULT NULL,
  `ScrapReason` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`ScrapID`) USING BTREE,
  INDEX `DeviceID`(`DeviceID` ASC) USING BTREE,
  CONSTRAINT `devicescrap_ibfk_1` FOREIGN KEY (`DeviceID`) REFERENCES `device` (`DeviceID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of devicescrap
-- ----------------------------
INSERT INTO `devicescrap` VALUES (1, 4, '2023-03-01', '损坏无法修复');
INSERT INTO `devicescrap` VALUES (2, 6, '2023-03-02', '过时设备');
INSERT INTO `devicescrap` VALUES (3, 8, '2023-03-03', '替换为新型号');
INSERT INTO `devicescrap` VALUES (4, 10, '2023-03-04', '无法维修');
INSERT INTO `devicescrap` VALUES (5, 1, '2023-03-05', '过于老旧');
INSERT INTO `devicescrap` VALUES (6, 3, '2023-03-06', '高维修成本');
INSERT INTO `devicescrap` VALUES (7, 5, '2023-03-07', '更新设备');
INSERT INTO `devicescrap` VALUES (8, 7, '2023-03-08', '设备更新');
INSERT INTO `devicescrap` VALUES (9, 9, '2023-03-09', '报废周期到期');
INSERT INTO `devicescrap` VALUES (10, 2, '2023-03-10', '技术升级');

-- ----------------------------
-- Table structure for deviceusage
-- ----------------------------
DROP TABLE IF EXISTS `deviceusage`;
CREATE TABLE `deviceusage`  (
  `UsageID` int NOT NULL,
  `DeviceID` int NOT NULL,
  `UserID` int NOT NULL,
  `UsageDate` date NULL DEFAULT NULL,
  `Status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`UsageID`) USING BTREE,
  INDEX `DeviceID`(`DeviceID` ASC) USING BTREE,
  INDEX `UserID`(`UserID` ASC) USING BTREE,
  CONSTRAINT `deviceusage_ibfk_1` FOREIGN KEY (`DeviceID`) REFERENCES `device` (`DeviceID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `deviceusage_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of deviceusage
-- ----------------------------
INSERT INTO `deviceusage` VALUES (1, 1, 1, '2023-01-01', '使用中');
INSERT INTO `deviceusage` VALUES (2, 2, 2, '2023-01-02', '使用中');
INSERT INTO `deviceusage` VALUES (3, 3, 3, '2023-01-03', '维修中');
INSERT INTO `deviceusage` VALUES (4, 4, 4, '2023-01-04', '已完成');
INSERT INTO `deviceusage` VALUES (5, 5, 5, '2023-01-05', '使用中');
INSERT INTO `deviceusage` VALUES (6, 6, 6, '2023-01-06', '使用中');
INSERT INTO `deviceusage` VALUES (7, 7, 7, '2023-01-07', '使用中');
INSERT INTO `deviceusage` VALUES (8, 8, 8, '2023-01-08', '使用中');
INSERT INTO `deviceusage` VALUES (9, 9, 9, '2023-01-09', '使用中');
INSERT INTO `deviceusage` VALUES (10, 10, 10, '2023-01-10', '维修中');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `UserID` int NOT NULL,
  `Name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Department` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Contact` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`UserID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '张三', 'IT', '1234567890');
INSERT INTO `user` VALUES (2, '李四', '财务部', '1234567891');
INSERT INTO `user` VALUES (3, '王五', '市场部', '1234567892');
INSERT INTO `user` VALUES (4, '赵六', '人力资源部', '1234567893');
INSERT INTO `user` VALUES (5, '孙七', '研发部', '1234567894');
INSERT INTO `user` VALUES (6, '周八', '销售部', '1234567895');
INSERT INTO `user` VALUES (7, '吴九', '客服部', '1234567896');
INSERT INTO `user` VALUES (8, '郑十', '行政部', '1234567897');
INSERT INTO `user` VALUES (9, '王二', '采购部', '1234567898');
INSERT INTO `user` VALUES (10, '李三', '运营部', '1234567899');

-- ----------------------------
-- View structure for admindevicestatus
-- ----------------------------
DROP VIEW IF EXISTS `admindevicestatus`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `admindevicestatus` AS select `device`.`DeviceID` AS `DeviceID`,`device`.`DeviceName` AS `DeviceName`,`device`.`Status` AS `Status`,`device`.`PurchaseDate` AS `PurchaseDate` from `device`;

SET FOREIGN_KEY_CHECKS = 1;
