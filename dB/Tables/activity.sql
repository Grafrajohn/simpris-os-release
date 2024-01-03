CREATE TABLE `activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `entity` varchar(5) NOT NULL,
  `module` varchar(10) NOT NULL,
  `submodule` varchar(10) NOT NULL,
  `action` varchar(10) NOT NULL,
  `createdDate` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Activity in system';