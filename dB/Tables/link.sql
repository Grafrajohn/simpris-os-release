CREATE TABLE `link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `entityID` int(11) NOT NULL,
  `entityType` int(11) NOT NULL,
  `link_name` varchar(100) NOT NULL,
  `link_url` varchar(100) NOT NULL,
  `link_target` varchar(20) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;