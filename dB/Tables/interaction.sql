CREATE TABLE `interaction` (
  `interactionID` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `organisationID` int(11) NOT NULL,
  `interactionTypeID` int(11) NOT NULL,
  `details` varchar(4000) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`interactionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;