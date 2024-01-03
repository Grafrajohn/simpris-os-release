CREATE TABLE `user_configuration` (
  `userID` mediumint(9) NOT NULL,
  `lookupTypeID` int(11) unsigned NOT NULL,
  `configurationData` varchar(50) NOT NULL,
  `configurationDataNum` float NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime NOT NULL,
  `updatedBy` int(11) NOT NULL,
  `deletedDate` datetime NOT NULL,
  `deletedBy` int(11) NOT NULL,
  PRIMARY KEY (`userID`,`lookupTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='User configuration values for system wide settings e.g. skining of system, theme, css etc';