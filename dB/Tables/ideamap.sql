CREATE TABLE `ideamap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) unsigned zerofill NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) unsigned zerofill DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;