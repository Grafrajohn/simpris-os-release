CREATE TABLE `error` (
  `errorID` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) DEFAULT NULL,
  `organisationID` int(11) DEFAULT NULL,
  `userID` int(11) DEFAULT NULL,
  `description` varchar(500) DEFAULT '',
  `module` varchar(10) DEFAULT '',
  `submodule` varchar(10) DEFAULT '',
  `action` varchar(10) DEFAULT '',
  `subaction` varchar(10) DEFAULT '',
  `createdDate` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`errorID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;