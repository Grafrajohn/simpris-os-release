CREATE TABLE `account` (
  `accountID` int(11) NOT NULL AUTO_INCREMENT,
  `accountName` varchar(100) NOT NULL,
  `authenticationID` varchar(45) DEFAULT NULL,
  `authenticationID2` varchar(45) DEFAULT NULL,
  `authenticationID3` varchar(45) DEFAULT NULL,
  `membershipTypeID` int(11) NOT NULL,
  `membershipRenewalDate` datetime DEFAULT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(75) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updateDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`accountID`),
  UNIQUE KEY `ix_account` (`accountName`,`email`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8 COMMENT='Account is what is registered as the paying account. There is a one to one relationship between account and client.';

CREATE TABLE `answer` (
  `answerID` int(11) NOT NULL AUTO_INCREMENT,
  `questionID` int(11) NOT NULL,
  `answer` varchar(5000) NOT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`answerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=544 DEFAULT CHARSET=utf8;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=171 DEFAULT CHARSET=utf8;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_7e96b11fa306a2e0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `board` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userID` int(11) NOT NULL,
  `itemID` int(11) NOT NULL,
  `itemType` int(11) NOT NULL,
  `columnNo` int(11) NOT NULL,
  `itemOrder` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COMMENT='Kanban board table';

CREATE TABLE `client` (
  `clientID` int(11) NOT NULL AUTO_INCREMENT,
  `accountID` int(11) NOT NULL,
  `userID` mediumint(11) NOT NULL,
  `clientName` varchar(100) NOT NULL,
  `address1` varchar(45) NOT NULL,
  `address2` varchar(45) NOT NULL,
  `address3` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `region` varchar(45) NOT NULL,
  `country` varchar(50) NOT NULL,
  `postcode` varchar(45) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updateDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`clientID`),
  KEY `FK_client_account` (`accountID`),
  KEY `ix_client` (`clientName`),
  CONSTRAINT `FK_client_account` FOREIGN KEY (`accountID`) REFERENCES `account` (`accountID`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8 COMMENT='Client might be a design agency and organisations might be their customers';

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

CREATE TABLE `comment` (
  `commentID` int(11) NOT NULL AUTO_INCREMENT,
  `parentID` int(11) NOT NULL,
  `parentTypeID` int(11) NOT NULL,
  `commentTypeID` int(11) NOT NULL,
  `commentText` varchar(5000) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`commentID`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8;

CREATE TABLE `country` (
  `countryID` int(10) NOT NULL,
  `countryName` varchar(100) NOT NULL,
  PRIMARY KEY (`countryID`),
  UNIQUE KEY `ix_country` (`countryName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `djang_content_type_id_58fcbaa5a9e45863_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_2cbcf755a38a186b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=182 DEFAULT CHARSET=utf8;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `document` (
    `documentID` INT(11) NOT NULL AUTO_INCREMENT,
    `documentTypeID` INT(11) NOT NULL DEFAULT '0',
    `documentParentID` INT(11) NOT NULL DEFAULT '0',
    `documentName` VARCHAR(100) NOT NULL,
    `documentFileName` VARCHAR(100) NOT NULL,
    `documentTitle` VARCHAR(100) DEFAULT NULL,
    `createdDate` DATETIME NOT NULL,
    `createdBy` INT(11) NOT NULL,
    `deletedDate` DATETIME DEFAULT NULL,
    `deletedBy` INT(11) DEFAULT NULL,
    PRIMARY KEY (`documentID`)
)  ENGINE=INNODB AUTO_INCREMENT=29 DEFAULT CHARSET=UTF8;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `groups` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

CREATE TABLE `idea` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `parentID` int(11) NOT NULL,
  `parentTypeID` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

CREATE TABLE `interaction` (
  `interactionID` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `interactionTypeID` int(11) NOT NULL,
  `details` varchar(4000) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `organisationID` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`interactionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `invoice` (
  `invoiceID` int(10) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `userID` mediumint(10) NOT NULL,
  `statusID` int(10) NOT NULL DEFAULT '1' COMMENT 'eg paid, written off etc',
  `supersededBy` int(10) DEFAULT NULL COMMENT 'Invoice which superseded this one',
  `description` varchar(50) NOT NULL COMMENT 'Invoice which superseded this one',
  `comments` varchar(500) NOT NULL COMMENT 'Invoice which superseded this one',
  `createdDate` datetime NOT NULL,
  `createdBy` mediumint(8) NOT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` mediumint(8) DEFAULT NULL,
  `invoicecol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`invoiceID`),
  KEY `ix_invoice_client` (`clientID`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

CREATE TABLE `invoiceline` (
  `invoiceID` int(10) NOT NULL,
  `lineNo` int(10) NOT NULL,
  `taskID` int(10) NOT NULL,
  `timeID` int(10) NOT NULL,
  `itemDescription` varchar(150) NOT NULL,
  `tax1Rate` decimal(10,2) unsigned NOT NULL,
  `tax2Rate` decimal(10,2) unsigned NOT NULL,
  `tax3Rate` decimal(10,2) unsigned NOT NULL,
  `hourlyRate` decimal(10,2) unsigned NOT NULL,
  `noHours` decimal(10,1) unsigned NOT NULL,
  `agreedRate` decimal(10,1) unsigned NOT NULL COMMENT 'Where rate agreed instead of hourly rate',
  `tax1` decimal(10,2) unsigned NOT NULL,
  `tax2` decimal(10,2) unsigned NOT NULL,
  `tax3` decimal(10,2) unsigned NOT NULL,
  `grossTotal` decimal(10,2) unsigned NOT NULL COMMENT 'Total before tax',
  `netTotal` decimal(10,2) unsigned NOT NULL COMMENT 'Total after tax',
  PRIMARY KEY (`invoiceID`,`lineNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `login_attempts` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `ip_address` varbinary(16) NOT NULL,
  `login` varchar(100) NOT NULL,
  `time` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `lookup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL DEFAULT '0',
  `lookupTypeID` int(11) NOT NULL,
  `lookupSubTypeID` int(11) NOT NULL,
  `lookupOrder` int(11) NOT NULL,
  `lookupValueNum` int(11) DEFAULT NULL,
  `lookupValueChar` varchar(50) DEFAULT NULL,
  `lookupDescription` varchar(200) NOT NULL,
  `disabled` bit(1) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_lookup_typeid` (`lookupTypeID`),
  KEY `ix_lookup_subtypeid` (`lookupSubTypeID`),
  KEY `ix_unique_lookup` (`clientID`,`lookupTypeID`,`lookupSubTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=utf8;

CREATE TABLE `lookup_type` (
  `id` int(11) unsigned NOT NULL,
  `lookupType` varchar(100) NOT NULL DEFAULT '',
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `menus_cachekey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `language` varchar(255) NOT NULL,
  `site` int(10) unsigned NOT NULL,
  `key` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `meta` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` mediumint(8) unsigned DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `mainOrganisationID` int(11) DEFAULT NULL COMMENT 'Organisation to which the user belongs',
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `opinion` (
  `opinionID` int(11) NOT NULL AUTO_INCREMENT,
  `userID` int(11) NOT NULL,
  `itemType` int(11) NOT NULL COMMENT 'Type of thing the opinion expressed about: project, tasklist, task',
  `itemID` int(11) NOT NULL,
  `opinionType` int(11) DEFAULT NULL,
  `opinion` varchar(250) DEFAULT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`opinionID`),
  UNIQUE KEY `ix_opinion` (`userID`,`itemType`,`itemID`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COMMENT='Users express opinions on a project/tasklist/task ';

CREATE TABLE `organisation` (
  `organisationID` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `organisationName` varchar(100) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`organisationID`),
  KEY `fk_org_project` (`organisationID`),
  KEY `FK_organisation_client` (`clientID`),
  KEY `ix_organisation` (`organisationName`,`clientID`),
  CONSTRAINT `FK_organisation_client` FOREIGN KEY (`clientID`) REFERENCES `client` (`clientID`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8;

CREATE TABLE `organisation_archive` (
  `organisationID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `organisationName` varchar(100) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `payrate` (
  `payrateID` int(11) NOT NULL AUTO_INCREMENT,
  `payrateDescription` varchar(20) NOT NULL,
  `rate` decimal(10,2) NOT NULL,
  `rateper` int(11) NOT NULL,
  `taskType` int(11) DEFAULT NULL,
  `effectiveDate` datetime NOT NULL,
  `createdDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `createdBy` int(11) NOT NULL,
  `updateDate` datetime DEFAULT NULL,
  `updateBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`payrateID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `phase` (
  `phaseID` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `phaseName` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `phaseDescription` varchar(500) CHARACTER SET utf8mb4 DEFAULT NULL,
  `startDate` datetime DEFAULT NULL,
  `endDate` datetime DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`phaseID`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8 COMMENT='Phases of projects';

CREATE TABLE `problem` (
  `problemID` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `organisationID` int(11) NOT NULL,
  `problemTypeID` int(11) NOT NULL,
  `problemSubTypeID` int(11) DEFAULT NULL,
  `problemHeader` varchar(50) NOT NULL,
  `problemDescription` varchar(2000) NOT NULL,
  `noOfPeopleAffected` int(11) NOT NULL,
  `scope` int(11) NOT NULL,
  `problemStatusID` int(11) DEFAULT NULL,
  `queueID` int(11) DEFAULT NULL,
  `problemPriorityID` int(11) DEFAULT NULL,
  `assignedTo` int(11) DEFAULT NULL,
  `completedDate` datetime DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`problemID`),
  UNIQUE KEY `ix_problem` (`organisationID`,`problemHeader`),
  KEY `FK_problem_organisation` (`organisationID`),
  KEY `ix_problem_client` (`clientID`),
  KEY `ix_problem_type` (`problemTypeID`),
  CONSTRAINT `FK_problem_organisation` FOREIGN KEY (`organisationID`) REFERENCES `organisation` (`organisationID`)
) ENGINE=InnoDB AUTO_INCREMENT=240 DEFAULT CHARSET=utf8;

CREATE TABLE `problem_archive` (
  `problemID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `organisationID` int(11) NOT NULL,
  `problemTypeID` int(11) NOT NULL,
  `problemSubTypeID` int(11) DEFAULT NULL,
  `problemHeader` varchar(50) NOT NULL,
  `problemDescription` varchar(2000) NOT NULL,
  `noOfPeopleAffected` int(11) NOT NULL,
  `scope` int(11) NOT NULL,
  `problemStatusID` int(11) DEFAULT NULL,
  `problemPriorityID` int(11) DEFAULT NULL,
  `queueID` int(11) DEFAULT NULL,
  `assignedTo` int(11) DEFAULT NULL,
  `completedDate` datetime DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `problemlink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problemID` int(11) NOT NULL,
  `problemLinkID` int(11) NOT NULL,
  `problemLinkType` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_tasklink_unique` (`problemID`,`problemLinkID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COMMENT='Link problems to projects, tasks, etc';

CREATE TABLE `programme` (
  `programmeID` int(10) NOT NULL AUTO_INCREMENT,
  `clientID` int(10) NOT NULL DEFAULT '0',
  `programmeName` varchar(50) NOT NULL,
  `programmeDescription` varchar(500) DEFAULT NULL,
  `manager` int(11) DEFAULT NULL,
  `createdBy` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`programmeID`),
  UNIQUE KEY `ix_program` (`clientID`,`programmeName`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='Progammes are a way of organising projects i.e. many projects to a programme';

CREATE TABLE `project` (
  `projectID` int(11) NOT NULL AUTO_INCREMENT,
  `organisationID` int(11) NOT NULL,
  `programmeID` int(11) DEFAULT NULL,
  `clientID` int(11) NOT NULL,
  `projectName` varchar(50) NOT NULL,
  `projectDescription` varchar(500) DEFAULT NULL,
  `stakeholderID` int(11) DEFAULT NULL,
  `projectManagerID` int(11) DEFAULT NULL,
  `deliverables` varchar(1500) DEFAULT NULL,
  `budget` decimal(10,0) DEFAULT NULL,
  `importance` int(11) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`projectID`),
  KEY `FK_project_organisation` (`organisationID`),
  KEY `ix_project_client` (`clientID`),
  CONSTRAINT `FK_project_organisation` FOREIGN KEY (`organisationID`) REFERENCES `organisation` (`organisationID`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8 COMMENT='Main project table';

CREATE TABLE `project_archive` (
  `projectID` int(11) NOT NULL,
  `organisationID` int(11) NOT NULL,
  `programmeID` int(11) DEFAULT NULL,
  `clientID` int(11) NOT NULL,
  `projectName` varchar(50) NOT NULL,
  `projectDescription` varchar(500) DEFAULT NULL,
  `stakeholderID` int(11) DEFAULT NULL,
  `projectManagerID` int(11) DEFAULT NULL,
  `deliverables` varchar(1500) DEFAULT NULL,
  `budget` decimal(10,0) DEFAULT NULL,
  `importance` int(11) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `question` (
  `questionID` int(11) NOT NULL AUTO_INCREMENT,
  `questionName` varchar(45) DEFAULT NULL,
  `questionText` varchar(5000) DEFAULT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`questionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `questionnaire` (
  `questionnaireID` int(11) NOT NULL AUTO_INCREMENT,
  `questionnaireName` varchar(45) NOT NULL,
  `contactUserID` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`questionnaireID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='questionnaire table';

CREATE TABLE `questionnaire_question` (
  `questionnaireID` int(11) NOT NULL,
  `questionID` int(11) NOT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`questionnaireID`,`questionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `queue` (
  `queueID` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `queueName` varchar(45) NOT NULL,
  `queueDescription` varchar(450) DEFAULT NULL,
  `createdBy` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`queueID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='queue for tasks and problems';

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

CREATE TABLE `queue_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `queueUserID` int(11) NOT NULL,
  `queueID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `createdDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `queueID_idx` (`queueID`),
  CONSTRAINT `id` FOREIGN KEY (`id`) REFERENCES `auth_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `queueID` FOREIGN KEY (`queueID`) REFERENCES `queue` (`queueID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='Users of queues';

CREATE TABLE `status` (
  `statusID` int(11) NOT NULL,
  `userID` mediumint(9) DEFAULT NULL,
  `itemID` int(11) DEFAULT NULL,
  `itemType` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `statuscol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`statusID`),
  UNIQUE KEY `ix_status` (`userID`,`itemID`,`itemType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='statuses of various objects e.g. project etc';

CREATE TABLE `step` (
  `stepID` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `taskID` int(11) NOT NULL,
  `description` varchar(100) NOT NULL,
  `status` int(11) NOT NULL DEFAULT '1',
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`stepID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Task steps';

CREATE TABLE `task` (
  `taskID` int(11) NOT NULL AUTO_INCREMENT,
  `taskListID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `taskTypeID` int(11) NOT NULL,
  `taskName` varchar(50) NOT NULL,
  `taskDescription` varchar(10000) NOT NULL,
  `taskStatusID` int(11) DEFAULT NULL,
  `taskPriorityID` int(11) DEFAULT NULL,
  `assignedTo` int(11) DEFAULT NULL,
  `taskStartDate` datetime DEFAULT NULL,
  `taskTimeEstimate` decimal(10,1) DEFAULT NULL,
  `taskPercentComplete` int(11) DEFAULT NULL,
  `completionDate` datetime DEFAULT NULL,
  `phaseID` int(11) DEFAULT NULL,
  `taskLinkID` int(11) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`taskID`),
  KEY `fk_task_tasklist` (`taskListID`),
  KEY `fk_tasklist` (`taskListID`),
  KEY `ix_task_client` (`clientID`)
) ENGINE=InnoDB AUTO_INCREMENT=245 DEFAULT CHARSET=utf8;

CREATE TABLE `task_archive` (
  `taskID` int(11) NOT NULL,
  `taskListID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `taskTypeID` int(11) NOT NULL,
  `taskName` varchar(50) NOT NULL,
  `taskDescription` varchar(10000) NOT NULL DEFAULT '',
  `taskStatusID` int(11) DEFAULT NULL,
  `taskPriorityID` int(11) DEFAULT NULL,
  `assignedTo` int(11) DEFAULT NULL,
  `taskStartDate` datetime DEFAULT NULL,
  `taskTimeEstimate` decimal(10,1) DEFAULT NULL,
  `taskPercentComplete` int(11) DEFAULT NULL,
  `completionDate` datetime DEFAULT NULL,
  `phaseID` int(11) DEFAULT NULL,
  `taskLinkID` int(11) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `task_template` (
  `tasktemplateID` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) DEFAULT NULL,
  `tasktemplateName` varchar(100) DEFAULT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`tasktemplateID`),
  UNIQUE KEY `ix_tasktemplate` (`tasktemplateName`,`clientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Task templates with set of task steps';

CREATE TABLE `tasklist` (
  `taskListID` int(11) NOT NULL AUTO_INCREMENT,
  `projectID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `taskListName` varchar(50) NOT NULL,
  `taskListDescription` varchar(500) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`taskListID`),
  UNIQUE KEY `projectID_taskListName` (`projectID`,`taskListName`),
  UNIQUE KEY `ix_tasklist` (`taskListName`,`projectID`),
  KEY `fk_tasklist_project` (`projectID`),
  KEY `ix_tasklist_client` (`clientID`),
  CONSTRAINT `FK_tasklist_project` FOREIGN KEY (`projectID`) REFERENCES `project` (`projectID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;

CREATE TABLE `tasklist_archive` (
  `taskListID` int(11) NOT NULL,
  `projectID` int(11) NOT NULL,
  `clientID` int(11) DEFAULT NULL,
  `taskListName` varchar(50) NOT NULL,
  `taskListDescription` varchar(500) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedID` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `taskstep` (
  `taskstepID` int(11) NOT NULL AUTO_INCREMENT,
  `taskID` int(11) DEFAULT NULL,
  `steporder` int(11) DEFAULT NULL,
  PRIMARY KEY (`taskstepID`),
  UNIQUE KEY `ix_taskstep` (`taskID`,`steporder`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Steps within tasks.';

CREATE TABLE `taxrate` (
  `taxrateID` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `taxrateDescription` varchar(100) NOT NULL,
  `taxrate` decimal(10,2) NOT NULL,
  `effectiveDate` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `createdDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`taxrateID`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8 COMMENT='tax rates';

CREATE TABLE `team` (
  `teamID` int(11) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `teamName` varchar(100) NOT NULL,
  `teamDescription` varchar(1000) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

CREATE TABLE `team_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teamID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `createdBy` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='Members of teams';

CREATE TABLE `test_table` (
  `testint` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `time` (
  `timeID` int(10) NOT NULL AUTO_INCREMENT,
  `clientID` int(11) NOT NULL,
  `timeDay` datetime NOT NULL,
  `hours` float NOT NULL,
  `taskID` int(11) NOT NULL,
  `timeTypeID` int(11) NOT NULL,
  `userID` mediumint(11) NOT NULL,
  `comments` varchar(50) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`timeID`),
  KEY `FK1_time_task` (`taskID`),
  KEY `ix_time_client` (`clientID`),
  CONSTRAINT `FK1_time_task` FOREIGN KEY (`taskID`) REFERENCES `task` (`taskID`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8 COMMENT='time recording';

CREATE TABLE `user_attributes` (
  `userID` int(11) NOT NULL,
  `vip` char(1) NOT NULL DEFAULT 'n',
  `countryID` int(11) DEFAULT NULL,
  `mobilePhoneNo` varchar(20) DEFAULT NULL,
  `faxNo` varchar(20) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='User attirbutes per user data such as VIP user etc';

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

CREATE TABLE `user_cookie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userID` bigint(20) NOT NULL,
  `uuID` varchar(128) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(40) NOT NULL,
  `created_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `user_payrate` (
  `userID` int(10) NOT NULL,
  `payrateID` int(10) NOT NULL,
  `effectiveDate` datetime NOT NULL,
  `defaultRate` decimal(10,2) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Amount paid to users';

CREATE TABLE `user_status` (
  `statusID` int(11) NOT NULL,
  `userID` mediumint(9) DEFAULT NULL,
  `itemID` int(11) DEFAULT NULL,
  `itemType` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `statuscol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`statusID`),
  UNIQUE KEY `ix_unique` (`userID`,`itemID`,`itemType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='users statuses for various entities e.g. project, task etc e.g. user worried about this task';

CREATE TABLE `user_taxrate` (
  `userID` int(11) NOT NULL,
  `taxrateID` decimal(10,2) NOT NULL,
  `effectiveDate` datetime DEFAULT NULL,
  `defaultRate` decimal(10,2) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tax rate for user invoicing';

CREATE TABLE `useractivity` (
  `activityID` int(11) NOT NULL AUTO_INCREMENT,
  `userID` mediumint(11) NOT NULL,
  `activityData` varchar(100) DEFAULT NULL,
  `client_id` int(11) NOT NULL,
  `activityDate` datetime NOT NULL,
  `activityType` varchar(10) NOT NULL,
  `activity_module` varchar(10) NOT NULL,
  `activity_submodule` varchar(10) NOT NULL,
  PRIMARY KEY (`activityID`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8;

CREATE TABLE `userorganisation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userID` mediumint(11) NOT NULL,
  `organisationID` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_org` (`organisationID`),
  CONSTRAINT `FK_userorganisation_organisation` FOREIGN KEY (`organisationID`) REFERENCES `organisation` (`organisationID`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

CREATE TABLE `userproject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userID` mediumint(11) NOT NULL,
  `projectID` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_project` (`projectID`),
  CONSTRAINT `fk_user_project` FOREIGN KEY (`projectID`) REFERENCES `project` (`projectID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8;

CREATE TABLE `userreport` (
  `userID` int(10) NOT NULL,
  `reportID` int(10) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `users` (
  `id` mediumint(8) unsigned NOT NULL,
  `clientID` int(11) NOT NULL,
  `ip_address` varbinary(16) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(40) NOT NULL,
  `salt` varchar(40) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `activation_code` varchar(40) DEFAULT NULL,
  `forgotten_password_code` varchar(40) DEFAULT NULL,
  `forgotten_password_time` int(11) unsigned DEFAULT NULL,
  `remember_code` varchar(40) DEFAULT NULL,
  `created_on` int(11) unsigned NOT NULL,
  `last_login` int(11) unsigned DEFAULT NULL,
  `active` tinyint(1) unsigned DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `company` int(11) unsigned DEFAULT NULL COMMENT 'Changed from VARCHAR by GFJ - main org ID',
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `users_archive` (
  `id` mediumint(8) unsigned NOT NULL,
  `clientID` int(11) NOT NULL,
  `ip_address` varbinary(16) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(40) NOT NULL,
  `salt` varchar(40) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `activation_code` varchar(40) DEFAULT NULL,
  `forgotten_password_code` varchar(40) DEFAULT NULL,
  `forgotten_password_time` int(11) unsigned DEFAULT NULL,
  `remember_code` varchar(40) DEFAULT NULL,
  `created_on` int(11) unsigned NOT NULL,
  `last_login` int(11) unsigned DEFAULT NULL,
  `active` tinyint(1) unsigned DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `company` int(11) unsigned DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `users_groups` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` mediumint(8) unsigned NOT NULL,
  `group_id` mediumint(8) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8;

CREATE TABLE `usertask` (
  `userID` mediumint(11) NOT NULL,
  `taskID` int(11) NOT NULL,
  PRIMARY KEY (`userID`,`taskID`),
  KEY `FK_usertask_task` (`taskID`),
  CONSTRAINT `FK_usertask_task` FOREIGN KEY (`taskID`) REFERENCES `task` (`taskID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;