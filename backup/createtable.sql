-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.7.22 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Linux
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 fanhao 的数据库结构
CREATE DATABASE IF NOT EXISTS `fanhao` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `fanhao`;

-- 导出  表 fanhao.fanhao 结构
CREATE TABLE IF NOT EXISTS `fanhao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(64) NOT NULL,
  `title` varchar(128) NOT NULL,
  `star` varchar(64) DEFAULT NULL,
  `starcode` varchar(64) DEFAULT NULL,
  `img` varchar(128) DEFAULT NULL,
  `fname` varchar(128) DEFAULT NULL,
  `ima` tinyint(4) NOT NULL DEFAULT '0',
  `iface` tinyint(4) NOT NULL DEFAULT '0',
  `starnum` tinyint(4) NOT NULL DEFAULT '0',
  `xface` tinyint(4) NOT NULL DEFAULT '0',
  `updateTime` int(11) NOT NULL DEFAULT '0',
  `downed` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=481 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
