CREATE TABLE `person` (
  `personID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `organisationID` int(11) NOT NULL,
  `title` varchar(10) NOT NULL DEFAULT '',
  `forename` varchar(50) NOT NULL DEFAULT '',
  `initials` varchar(20) NOT NULL DEFAULT '',
  `surname` varchar(50) NOT NULL DEFAULT '',
  `position` int(11) NOT NULL,
  `email` varchar(100) NOT NULL DEFAULT '',
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`personID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;