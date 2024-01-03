CREATE TABLE `queue_team` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `queueID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `queueTeamID` int(11) NOT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `createdDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
);