CREATE TABLE `queue_user` (
  `id` int(11) NOT NULL,
  `queueID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `createdDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `queueID_idx` (`queueID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Users of queues';