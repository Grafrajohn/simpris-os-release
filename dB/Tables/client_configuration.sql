CREATE TABLE `client_configuration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `configTypeID` int(11) DEFAULT NULL,
  `configID` int(11) DEFAULT NULL,
  `valueChar` varchar(500) DEFAULT NULL,
  `valueNum` decimal(9,2) DEFAULT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`,`clientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Client level configuration';