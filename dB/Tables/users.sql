CREATE TABLE `users` (
  `id` mediumint(8) unsigned NOT NULL,
  `clientID` int(11) NOT NULL,
  `company` int(11) unsigned DEFAULT NULL COMMENT 'Changed from VARCHAR by GFJ - main org ID',
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
