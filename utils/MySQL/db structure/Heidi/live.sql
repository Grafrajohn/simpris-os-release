-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               5.5.41-0ubuntu0.14.04.1 - (Ubuntu)
-- Server OS:                    debian-linux-gnu
-- HeidiSQL Version:             9.2.0.4967
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table simpricity.account
CREATE TABLE IF NOT EXISTS `account` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Account is what is registered as the paying account. There is a one to one relationship between account and client.';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.answer
CREATE TABLE IF NOT EXISTS `answer` (
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

-- Data exporting was unselected.


-- Dumping structure for table simpricity.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_activities
CREATE TABLE IF NOT EXISTS `bf_activities` (
  `activity_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL DEFAULT '0',
  `activity` varchar(255) NOT NULL,
  `module` varchar(255) NOT NULL,
  `created_on` datetime NOT NULL,
  `deleted` tinyint(12) NOT NULL DEFAULT '0',
  `itemID` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_email_queue
CREATE TABLE IF NOT EXISTS `bf_email_queue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `to_email` varchar(128) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `message` text NOT NULL,
  `alt_message` text,
  `max_attempts` int(11) NOT NULL DEFAULT '3',
  `attempts` int(11) NOT NULL DEFAULT '0',
  `success` tinyint(1) NOT NULL DEFAULT '0',
  `date_published` datetime DEFAULT NULL,
  `last_attempt` datetime DEFAULT NULL,
  `date_sent` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_login_attempts
CREATE TABLE IF NOT EXISTS `bf_login_attempts` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ip_address` varchar(40) NOT NULL,
  `login` varchar(50) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_permissions
CREATE TABLE IF NOT EXISTS `bf_permissions` (
  `permission_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(100) NOT NULL,
  `status` enum('active','inactive','deleted') DEFAULT 'active',
  PRIMARY KEY (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_roles
CREATE TABLE IF NOT EXISTS `bf_roles` (
  `role_id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(60) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `default` tinyint(1) NOT NULL DEFAULT '0',
  `can_delete` tinyint(1) NOT NULL DEFAULT '1',
  `login_destination` varchar(255) NOT NULL DEFAULT '/',
  `deleted` int(1) NOT NULL DEFAULT '0',
  `default_context` varchar(255) NOT NULL DEFAULT 'content',
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_role_permissions
CREATE TABLE IF NOT EXISTS `bf_role_permissions` (
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`role_id`,`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_schema_version
CREATE TABLE IF NOT EXISTS `bf_schema_version` (
  `type` varchar(40) NOT NULL,
  `version` int(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_sessions
CREATE TABLE IF NOT EXISTS `bf_sessions` (
  `session_id` varchar(40) NOT NULL DEFAULT '0',
  `ip_address` varchar(45) NOT NULL DEFAULT '0',
  `user_agent` varchar(120) NOT NULL,
  `last_activity` int(10) unsigned NOT NULL DEFAULT '0',
  `user_data` text,
  PRIMARY KEY (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_settings
CREATE TABLE IF NOT EXISTS `bf_settings` (
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `module` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `value` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `unique - name` (`name`),
  KEY `index - name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_users
CREATE TABLE IF NOT EXISTS `bf_users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL DEFAULT '4',
  `email` varchar(120) NOT NULL,
  `username` varchar(30) NOT NULL DEFAULT '',
  `password_hash` varchar(40) NOT NULL,
  `reset_hash` varchar(40) DEFAULT NULL,
  `salt` varchar(7) NOT NULL,
  `last_login` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `last_ip` varchar(40) NOT NULL DEFAULT '',
  `created_on` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `banned` tinyint(1) NOT NULL DEFAULT '0',
  `ban_message` varchar(255) DEFAULT NULL,
  `reset_by` int(10) DEFAULT NULL,
  `display_name` varchar(255) DEFAULT '',
  `display_name_changed` date DEFAULT NULL,
  `timezone` char(4) NOT NULL DEFAULT 'UM6',
  `language` varchar(20) NOT NULL DEFAULT 'english',
  `active` tinyint(1) NOT NULL DEFAULT '0',
  `activate_hash` varchar(40) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_user_cookies
CREATE TABLE IF NOT EXISTS `bf_user_cookies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(40) NOT NULL,
  `token` varchar(128) NOT NULL,
  `created_on` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `token` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.bf_user_meta
CREATE TABLE IF NOT EXISTS `bf_user_meta` (
  `meta_id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(20) unsigned NOT NULL DEFAULT '0',
  `meta_key` varchar(255) NOT NULL DEFAULT '',
  `meta_value` text,
  PRIMARY KEY (`meta_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.client
CREATE TABLE IF NOT EXISTS `client` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Client might be a design agency and organisations might be their customers';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.comment
CREATE TABLE IF NOT EXISTS `comment` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.country
CREATE TABLE IF NOT EXISTS `country` (
  `countryID` int(10) NOT NULL,
  `countryName` varchar(100) NOT NULL,
  PRIMARY KEY (`countryID`),
  UNIQUE KEY `ix_country` (`countryName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
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
  CONSTRAINT `django_admin_log_user_id_2cbcf755a38a186b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_58fcbaa5a9e45863_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.document
CREATE TABLE IF NOT EXISTS `document` (
  `documentID` int(11) NOT NULL AUTO_INCREMENT,
  `documentTypeID` int(11) NOT NULL DEFAULT '0',
  `documentParentID` int(11) NOT NULL DEFAULT '0',
  `documentName` varchar(100) NOT NULL,
  `documentFileName` varchar(100) NOT NULL,
  `documentTitle` varchar(100) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`documentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for function simpricity.fn_get_client
DELIMITER //
CREATE DEFINER=`root`@`localhost` FUNCTION `fn_get_client`(parm_userID int) RETURNS int(11)
BEGIN

declare var_clientID int;

select cli.clientID into var_clientID
from organisation org join client on org.clientID = cli.clientID
join users usr on usr.company = org.organisationID 
where userID = @userID; 

RETURN var_clientID;
END//
DELIMITER ;


-- Dumping structure for function simpricity.fn_get_my_users
DELIMITER //
CREATE DEFINER=`root`@`localhost` FUNCTION `fn_get_my_users`(parm_userID int) RETURNS int(11)
BEGIN

declare var_count integer;

select count(*) into var_count
from users usr
join userorganisation uorg on usr.id = uorg.userID 
where id = parm_userID; 

RETURN var_count;

END//
DELIMITER ;


-- Dumping structure for function simpricity.fn_get_organisation
DELIMITER //
CREATE DEFINER=`root`@`localhost` FUNCTION `fn_get_organisation`(parm_userID int) RETURNS int(11)
BEGIN

declare var_organisationID int;

select org.organisationID into var_organisationID
from organisation
join users usr on usr.company = org.organisationID 
where userID = @userID; 

RETURN var_organisationID;

END//
DELIMITER ;


-- Dumping structure for function simpricity.fn_get_project_organisation
DELIMITER //
CREATE DEFINER=`root`@`localhost` FUNCTION `fn_get_project_organisation`(`parm_projectID` INT) RETURNS int(11)
BEGIN

DECLARE var_organisation int;

select organisationID into var_organisation from project where projectID = parm_projectID;

RETURN var_organisation;
END//
DELIMITER ;


-- Dumping structure for function simpricity.fn_past_date
DELIMITER //
CREATE DEFINER=`root`@`localhost` FUNCTION `fn_past_date`(`parm_noOfDays` INT) RETURNS date
    DETERMINISTIC
BEGIN



DECLARE var_mydate datetime;



set var_mydate = date_add(curdate(), interval parm_noOfDays day);



return var_mydate;



END//
DELIMITER ;


-- Dumping structure for table simpricity.groups
CREATE TABLE IF NOT EXISTS `groups` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.invoice
CREATE TABLE IF NOT EXISTS `invoice` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.invoiceline
CREATE TABLE IF NOT EXISTS `invoiceline` (
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

-- Data exporting was unselected.


-- Dumping structure for table simpricity.login_attempts
CREATE TABLE IF NOT EXISTS `login_attempts` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `ip_address` varbinary(16) NOT NULL,
  `login` varchar(100) NOT NULL,
  `time` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.lookup
CREATE TABLE IF NOT EXISTS `lookup` (
  `clientID` int(11) NOT NULL DEFAULT '0',
  `lookupTypeID` int(11) NOT NULL,
  `lookupSubTypeID` int(11) NOT NULL,
  `lookupOrder` int(11) NOT NULL,
  `lookupValueNum` int(11) DEFAULT NULL,
  `lookupValueChar` varchar(50) DEFAULT NULL,
  `lookupDescription` varchar(200) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`clientID`,`lookupTypeID`,`lookupSubTypeID`),
  KEY `ix_lookup_typeid` (`lookupTypeID`),
  KEY `ix_lookup_subtypeid` (`lookupSubTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.meta
CREATE TABLE IF NOT EXISTS `meta` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` mediumint(8) unsigned DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `mainOrganisationID` int(11) DEFAULT NULL COMMENT 'Organisation to which the user belongs',
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.opinion
CREATE TABLE IF NOT EXISTS `opinion` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Users express opinions on a project/tasklist/task ';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.organisation
CREATE TABLE IF NOT EXISTS `organisation` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.organisation_archive
CREATE TABLE IF NOT EXISTS `organisation_archive` (
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

-- Data exporting was unselected.


-- Dumping structure for table simpricity.payrate
CREATE TABLE IF NOT EXISTS `payrate` (
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

-- Data exporting was unselected.


-- Dumping structure for table simpricity.problem
CREATE TABLE IF NOT EXISTS `problem` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.problemlink
CREATE TABLE IF NOT EXISTS `problemlink` (
  `problemID` int(11) NOT NULL,
  `problemLinkID` int(11) NOT NULL,
  `problemLinkType` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`problemID`,`problemLinkID`,`problemLinkType`),
  UNIQUE KEY `ix_tasklink_unique` (`problemID`,`problemLinkID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Link problems to projects, tasks, etc';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.problem_archive
CREATE TABLE IF NOT EXISTS `problem_archive` (
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
  `assignedTo` int(11) DEFAULT NULL,
  `completedDate` datetime DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.programme
CREATE TABLE IF NOT EXISTS `programme` (
  `programmeID` int(10) NOT NULL AUTO_INCREMENT,
  `clientID` int(10) NOT NULL DEFAULT '0',
  `programmeName` varchar(50) NOT NULL,
  `programmeDescription` varchar(500) DEFAULT NULL,
  `createdBy` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`programmeID`),
  UNIQUE KEY `ix_program` (`clientID`,`programmeName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Progammes are a way of organising projects i.e. many projects to a programme';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.project
CREATE TABLE IF NOT EXISTS `project` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Main project table';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.project_archive
CREATE TABLE IF NOT EXISTS `project_archive` (
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

-- Data exporting was unselected.


-- Dumping structure for table simpricity.question
CREATE TABLE IF NOT EXISTS `question` (
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

-- Data exporting was unselected.


-- Dumping structure for table simpricity.questionnaire
CREATE TABLE IF NOT EXISTS `questionnaire` (
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

-- Data exporting was unselected.


-- Dumping structure for table simpricity.questionnaire_question
CREATE TABLE IF NOT EXISTS `questionnaire_question` (
  `questionnaireID` int(11) NOT NULL,
  `questionID` int(11) NOT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`questionnaireID`,`questionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for procedure simpricity.selectProjectDetail
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `selectProjectDetail`(IN `parm_projectID` INT)
BEGIN







select *



from project 



where projectID = parm_projectID;







END//
DELIMITER ;


-- Dumping structure for procedure simpricity.selectProjectsMy
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `selectProjectsMy`(IN parm_userID INT)
BEGIN







select *



from project pr inner join userProject up



on pr.projectID = up.projectID



where up.userID = parm_userID;







END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_check_recent_activity
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_check_recent_activity`()
BEGIN

(select 'account', accountName, createdDate
from account)
union
(select 'client', clientName, createdDate
from client)
union
(select 'project', projectName, createdDate
from project)
union
(select 'task', taskDescription, createdDate
from task)
order by 1,3 desc
limit 10;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_gantt_project
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_gantt_project`(IN `parm_projectID` INT)
BEGIN







select '[' as jsonRow



union



select CONCAT('{ "name": "', tsk.taskDescription, '","desc": "', tsk.taskDescription, '", 



"values": [{"from": "/Date(',tsk.createdDate,')/", "to": "/Date(',tsk.createdDate,')/", "desc": "<b>',



tsk.taskDescription,'</b><br><b>Data</b>: [',tsk.createdDate,' - ',tsk.createdDate,'] ", "customClass": "ganttRed", "label": "',



tsk.taskDescription,'"}]},') 



from project pro inner join tasklist tkl on pro.projectID = tkl.projectID



inner join task tsk on tsk.taskListID = tkl.taskListID



where pro.projectID = parm_projectID



union



select ']';







END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_get_project_potential_users
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_get_project_potential_users`(IN `parm_projectID` INT(11))
BEGIN
declare var_orgID int;
	select fn_get_project_organisation(parm_projectID) into var_orgID;

    select distinct
        `us`.`first_name` AS `first_name`,
        `us`.`last_name` AS `last_name`,
        `us`.`id` AS `userID`
    from
        `users` `us`
	where (us.id in (select userID from userorganisation where organisationID = var_orgID)
	or us.company = var_orgID)
	and us.id not in (select userID from userproject where projectID = parm_projectID);
END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_get_project_users
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_get_project_users`(IN `parm_projectID` INT(11))
    READS SQL DATA
BEGIN

    select 
        `us`.`first_name` AS `first_name`,
        `us`.`last_name` AS `last_name`,
        `us`.`id` AS `userID`
    from
        `users` `us`
        join `userproject` `usp` ON `us`.`id` = `usp`.`userID`
		where usp.projectID = parm_projectID;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_insert_invoice_line
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_insert_invoice_line`(IN `parm_invoiceID` INT, IN `parm_timeID` INT, IN `parm_lineNo` INT, IN parm_userID int)
BEGIN

declare var_taskID INT;
declare var_hours float;
declare var_description varchar(150);
declare var_hourlyrate decimal(10,2);
declare var_taxrate1 decimal(10,2);
declare var_taxrate2 decimal(10,2);
declare var_taxrate3 decimal(10,2);
declare var_tax1 decimal(10,2);
declare var_tax2 decimal(10,2);
declare var_tax3 decimal(10,2);
declare var_grossTotal decimal(10,2);
declare var_netTotal decimal(10,2);

select tk.taskID, IFNULL(tm.hours,0), tk.taskDescription into var_taskID, var_hours, var_description 
from time tm join task tk on tm.taskID = tk.taskID 
where timeID = parm_timeID;

select IFNULL(defaultRate,0) into var_hourlyrate
from user_payrate
where userID = parm_userID;

if var_hourlyRate IS NULL then set var_hourlyRate = 0;
end if;

select ifnull(defaultRate,0) into var_taxrate1
from user_taxrate
where userID = parm_userID;

if var_taxrate1 is null then set var_taxrate1 = 0;
end if;

set var_taxrate2 = 0;
set var_taxrate3 = 0;

set var_grossTotal = var_hourlyRate * var_hours;

set var_tax1 = var_grossTotal * var_taxrate1;
set var_tax2 = var_grossTotal * var_taxrate2;
set var_tax3 = var_grossTotal * var_taxrate3;

set var_netTotal = var_grossTotal - (var_tax1 + var_tax2 + var_tax3);

INSERT INTO `simpricity`.`invoiceline`

(invoiceID,

`lineNo`,

`taskID`,

`timeID`,

`itemDescription`,

`tax1Rate`,

`tax2Rate`,

`tax3Rate`,

`hourlyRate`,

`noHours`,

`agreedRate`,

`tax1`,

`tax2`,

`tax3`,

`grossTotal`,

`netTotal`)

VALUES

(

parm_invoiceID,

parm_lineNo,

var_TaskID,

parm_timeID,

var_description,

var_taxrate1,

var_taxrate2,

var_taxrate3,

var_hourlyrate,

var_hours,

var_hourlyrate,

var_tax1,

var_tax2,

var_tax3,

var_grossTotal,

var_netTotal

);

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_metric_client_revenue
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_metric_client_revenue`(IN parm_userID INT)
BEGIN

declare varTotal decimal(12,2);

select sum(invl.netTotal) into varTotal
from userorganisation uorg
inner join organisation org on uorg.organisationID = org.organisationID
inner join project prj on org.organisationID = prj.organisationID
inner join tasklist tkl on prj.projectID = tkl.projectID
inner join task tsk on tkl.taskListID = tsk.taskListID
inner join invoiceline invl on tsk.taskID = invl.taskID
where uorg.userID = parm_userID;

select concat(org.organisationName, ' : ', sum(invl.netTotal)) as col1,sum(invl.netTotal*100)/varTotal as col2
from userorganisation uorg
inner join organisation org on uorg.organisationID = org.organisationID
inner join project prj on org.organisationID = prj.organisationID
inner join tasklist tkl on prj.projectID = tkl.projectID
inner join task tsk on tkl.taskListID = tsk.taskListID
inner join invoiceline invl on tsk.taskID = invl.taskID
where uorg.userID = parm_userID
group by org.organisationID,org.organisationName;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_metric_my_client_revenue
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_metric_my_client_revenue`(IN parm_userID INT)
BEGIN

declare varTotal decimal(12,2);

select sum(invl.netTotal) into varTotal
from organisation org
inner join project prj on org.organisationID = prj.organisationID
inner join tasklist tkl on prj.projectID = tkl.projectID
inner join task tsk on tkl.taskListID = tsk.taskListID
inner join invoiceline invl on tsk.taskID = invl.taskID
where tsk.assignedTo = parm_userID;

select concat(org.organisationName, ' : ', sum(invl.netTotal)) as col1,sum(invl.netTotal*100)/varTotal as col2
from organisation org
inner join project prj on org.organisationID = prj.organisationID
inner join tasklist tkl on prj.projectID = tkl.projectID
inner join task tsk on tkl.taskListID = tsk.taskListID
inner join invoiceline invl on tsk.taskID = invl.taskID
where tsk.assignedTo = parm_userID
group by org.organisationID,org.organisationName;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_metric_my_problems_project
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_metric_my_problems_project`(IN parm_userID INT)
BEGIN

declare varTotal int;
set varTotal = 0;

select count(prb.problemID) into varTotal
from project prj
inner join problemlink plk on prj.projectID = plk.problemLinkID and plk.problemLinkType = 1
inner join problem prb on prb.problemID = plk.problemLinkID and prb.completedDate is null and prb.deletedDate is null
where prb.assignedTo = parm_userID;

if varTotal > 0 then
select concat(prj.projectName,' : ',count(prb.problemID)) as col1,count(prb.problemID*100)/varTotal as col2
from project prj
inner join problemlink plk on prj.projectID = plk.problemLinkID and plk.problemLinkType = 1
inner join problem prb on prb.problemID = plk.problemLinkID and prb.completedDate is null and prb.deletedDate is null
where prb.assignedTo = parm_userID;
end if;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_metric_problems_project
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_metric_problems_project`(IN parm_userID INT)
BEGIN

declare varTotal int;

select count(prb.problemID) into varTotal
from userorganisation uorg
inner join organisation org on uorg.organisationID = org.organisationID
inner join project prj on org.organisationID = prj.organisationID
inner join problemlink plk on prj.projectID = plk.problemLinkID and plk.problemLinkType = 1
inner join problem prb on prb.problemID = plk.problemLinkID and prb.completedDate is null and prb.deletedDate is null
where uorg.userID = parm_userID;

select concat(prj.projectName,' : ',count(prb.problemID)) as col1,count(prb.problemID*100)/varTotal as col2
from userorganisation uorg
inner join organisation org on uorg.organisationID = org.organisationID
inner join project prj on org.organisationID = prj.organisationID
inner join problemlink plk on prj.projectID = plk.problemLinkID and plk.problemLinkType = 1
inner join problem prb on prb.problemID = plk.problemLinkID and prb.completedDate is null and prb.deletedDate is null
where uorg.userID = parm_userID
group by prb.problemID;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_metric_problem_proj
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_metric_problem_proj`(IN parm_userID INT)
BEGIN

select org.organisationID as col1,org.organisationName as col2,sum(invl.netTotal) as col3
from userorganisation uorg
inner join organisation org on uorg.organisationID = org.organisationID
inner join project prj on org.organisationID = prj.organisationID
inner join tasklist tkl on prj.projectID = tkl.projectID
inner join task tsk on tkl.taskListID = tsk.taskListID
inner join invoiceline invl on tsk.taskID = invl.taskID
where uorg.userID = parm_userID
group by org.organisationID,org.organisationName;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_report_my_overdue_projects
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_my_overdue_projects`(IN parm_userID INT)
BEGIN

select prj.projectID as col1,prj.projectName as col2,prj.projectDescription as col3,max(tsk.taskStartDate) as col4,tsk.taskTimeEstimate
from project prj
join tasklist tkl on tkl.projectID = prj.projectID
join task tsk on tsk.tasklistID = tkl.tasklistID and tsk.taskStatusID not in (7,8,9)
and date_add(tsk.taskStartDate, INTERVAL tsk.taskTimeEstimate DAY) < current_timestamp
where prj.stakeholderID = parm_userID
or prj.projectManagerID = parm_userID
or prj.createdBy = parm_userID
or prj.updatedBy = parm_userID
or tkl.createdBy = parm_userID
or tkl.updatedBy = parm_userID
or tsk.assignedTo = parm_userID
or tsk.createdBy = parm_userID
or tsk.updatedBy = parm_userID
group by prj.projectID;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_report_my_overdue_tasks_proj
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_my_overdue_tasks_proj`(parm_userID int)
BEGIN

select tsk.taskID as col1,tsk.taskDescription as col2,prj.projectName as col3,date_add(tsk.taskStartDate,interval tsk.taskTimeEstimate day) as col4
from project prj
join tasklist tkl on tkl.projectID = prj.projectID
join task tsk on tsk.tasklistID = tkl.tasklistID and tsk.taskStatusID not in (7,8,9)
and date_add(tsk.taskStartDate, INTERVAL tsk.taskTimeEstimate DAY) < current_timestamp
where prj.stakeholderID = parm_userID
or prj.projectManagerID = parm_userID
or prj.createdBy = parm_userID
or prj.updatedBy = parm_userID
or tkl.createdBy = parm_userID
or tkl.updatedBy = parm_userID
or tsk.assignedTo = parm_userID
or tsk.createdBy = parm_userID
or tsk.updatedBy = parm_userID;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_report_my_tasks_complete
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_my_tasks_complete`(IN parm_userID INT)
BEGIN

select tsk.taskID as col1,tsk.taskDescription as col2,prj.projectName as col3,date_add(tsk.taskStartDate,interval tsk.taskTimeEstimate day) as col4
from project prj
join userproject upr on prj.projectID = upr.projectID
join tasklist tkl on tkl.projectID = prj.projectID
join task tsk on tsk.tasklistID = tkl.tasklistID and tsk.taskStatusID not in (7,8,9)
join users usr on usr.ID = upr.userID and usr.ID = parm_userID
where tsk.assignedTo = parm_userID
and (tsk.taskPercentComplete = 100
or tsk.taskStatusID = 7);

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_report_overdue_projects
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_overdue_projects`(IN parm_userID INT)
BEGIN

select prj.projectID as col1,prj.projectName as col2,prj.projectDescription as col3,max(tsk.taskStartDate) as col4,tsk.taskTimeEstimate
from project prj
join userproject upr on prj.projectID = upr.projectID
join tasklist tkl on tkl.projectID = prj.projectID
join task tsk on tsk.tasklistID = tkl.tasklistID and tsk.taskStatusID not in (7,8,9)
and date_add(tsk.taskStartDate, INTERVAL tsk.taskTimeEstimate DAY) < current_timestamp
join users usr on usr.ID = upr.userID and usr.ID = parm_userID
group by prj.projectID;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_report_overdue_tasks_proj
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_overdue_tasks_proj`(IN parm_userID INT)
BEGIN

select tsk.taskID as col1,tsk.taskDescription as col2,prj.projectName as col3,date_add(tsk.taskStartDate,interval tsk.taskTimeEstimate day) as col4
from project prj
join userproject upr on prj.projectID = upr.projectID
join tasklist tkl on tkl.projectID = prj.projectID
join task tsk on tsk.tasklistID = tkl.tasklistID and tsk.taskStatusID not in (7,8,9)
and date_add(tsk.taskStartDate, INTERVAL tsk.taskTimeEstimate DAY) < current_timestamp
join users usr on usr.ID = upr.userID and usr.ID = parm_userID;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_report_vip
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_vip`(IN parm_userID INT)
BEGIN

select prj.projectID as col1,usr.username as col2,prj.projectname as col3,lk.lookupvaluechar as col4
from users usr join userproject upr on usr.ID = upr.userID
join project prj on prj.projectID = upr.projectID 
join opinion opn on opn.userID = usr.id and opn.itemID = prj.projectID 
join lookup lk on lk.lookupsubtypeid = opn.opiniontype where lk.lookuptypeid = 20;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_selectGanttData
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_selectGanttData`(IN `parm_projectID` INT)
BEGIN



select pro.projectID, pro.projectName, tsk.taskDescription as 'name', tsk.taskDescription as 'desc', tsk.createdDate + 0 as 'from', 

tsk.createdDate + 1000000 as 'to'

from project pro left join tasklist tkl on pro.projectID = tkl.projectID

right join task tsk on tsk.taskListID = tkl.taskListID

where pro.projectID = parm_projectID;



END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_select_project_index_sidebar
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_select_project_index_sidebar`(IN `parm_userID` INT)
BEGIN

select 'New projects' as projectName,'' as column2,'' as id, 0 as column4
union
SELECT distinct proj.projectName, proj.createdDate,proj.projectID,3
from project proj join userproject upr on proj.projectID = upr.projectID
where proj.createdDate > fn_past_date(-10)
and upr.userID = parm_userID
union
select 'Changed projects','' as column2,'' as id, 5
union
SELECT proj.projectName, proj.updatedDate,proj.projectID, 7
from project proj join userproject upr on proj.projectID = upr.projectID
where proj.updatedDate > fn_past_date(-10)
and upr.userID = parm_userID
union
select 'New users','' as column2,'' as id, 9
union
SELECT proj.projectName, usr.username,proj.projectID, 11
from project proj left join userproject upr on proj.projectID = upr.projectID
join users usr on upr.userID = usr.id
where usr.created_on > fn_past_date(-10)
and usr.id = parm_userID
and proj.projectID in (select projectID from userproject where userid = parm_userID)
union
select 'New tasklists','' as column2,'' as id, 13
union
SELECT proj.projectName,tsk.taskListName,proj.projectID, 15
from project proj join userproject upr on proj.projectID = upr.projectID
join tasklist tsk on tsk.projectID = proj.projectID
where tsk.createdDate > fn_past_date(-10)
and upr.userID = parm_userID
order by 4,1,2
limit 40;

END//
DELIMITER ;


-- Dumping structure for procedure simpricity.sr_select_task_links
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_select_task_links`(in parm_taskID int, in parm_taskListID int)
BEGIN

    select distinct
        `tk`.`taskID` AS `taskID`,
        concat(left(`tk`.`taskDescription`, 30), '...') AS `taskDescription`
    from
        `task` `tk`
        join `tasklist` `tkl` ON `tk`.`taskListID` = `tkl`.`taskListID`
        join `project` `pr` ON `tkl`.`projectID` = `pr`.`projectID`
    where
        isnull(`pr`.`deletedDate`)
            and isnull(`tkl`.`deletedDate`)
            and isnull(`tk`.`deletedDate`)
			and pr.projectID in 
        (select pri.projectID 
		from `task` `tki`
        join `tasklist` `tkli` ON `tki`.`taskListID` = `tkli`.`taskListID`
        join `project` `pri` ON `tkli`.`projectID` = `pri`.`projectID`
		where tki.taskID = parm_taskID or tki.taskListID = parm_taskListID)
	order by tk.taskID;

END//
DELIMITER ;


-- Dumping structure for table simpricity.status
CREATE TABLE IF NOT EXISTS `status` (
  `statusID` int(11) NOT NULL,
  `userID` mediumint(9) DEFAULT NULL,
  `itemID` int(11) DEFAULT NULL,
  `itemType` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `statuscol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`statusID`),
  UNIQUE KEY `ix_status` (`userID`,`itemID`,`itemType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='statuses of various objects e.g. project etc';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.task
CREATE TABLE IF NOT EXISTS `task` (
  `taskID` int(11) NOT NULL AUTO_INCREMENT,
  `taskListID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `taskTypeID` int(11) NOT NULL,
  `taskDescription` varchar(10000) NOT NULL,
  `taskStatusID` int(11) DEFAULT NULL,
  `taskPriorityID` int(11) DEFAULT NULL,
  `assignedTo` int(11) DEFAULT NULL,
  `taskStartDate` datetime DEFAULT NULL,
  `taskTimeEstimate` decimal(10,1) DEFAULT NULL,
  `taskPercentComplete` int(11) DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.tasklist
CREATE TABLE IF NOT EXISTS `tasklist` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.tasklist_archive
CREATE TABLE IF NOT EXISTS `tasklist_archive` (
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

-- Data exporting was unselected.


-- Dumping structure for table simpricity.taskstep
CREATE TABLE IF NOT EXISTS `taskstep` (
  `taskstepID` int(11) NOT NULL AUTO_INCREMENT,
  `taskID` int(11) DEFAULT NULL,
  `steporder` int(11) DEFAULT NULL,
  PRIMARY KEY (`taskstepID`),
  UNIQUE KEY `ix_taskstep` (`taskID`,`steporder`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Steps within tasks.';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.task_archive
CREATE TABLE IF NOT EXISTS `task_archive` (
  `taskID` int(11) NOT NULL,
  `taskListID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `taskTypeID` int(11) NOT NULL,
  `taskDescription` varchar(500) NOT NULL,
  `taskStatusID` int(11) DEFAULT NULL,
  `taskPriorityID` int(11) DEFAULT NULL,
  `assignedTo` int(11) DEFAULT NULL,
  `taskStartDate` datetime DEFAULT NULL,
  `taskTimeEstimate` decimal(10,1) DEFAULT NULL,
  `taskPercentComplete` int(11) DEFAULT NULL,
  `taskLinkID` int(11) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.task_template
CREATE TABLE IF NOT EXISTS `task_template` (
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

-- Data exporting was unselected.


-- Dumping structure for table simpricity.taxrate
CREATE TABLE IF NOT EXISTS `taxrate` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='tax rates';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.team
CREATE TABLE IF NOT EXISTS `team` (
  `teamID` int(11) NOT NULL,
  `teamName` varchar(100) NOT NULL,
  `teamDescription` varchar(1000) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`teamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.test_table
CREATE TABLE IF NOT EXISTS `test_table` (
  `testint` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.time
CREATE TABLE IF NOT EXISTS `time` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='time recording';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.useractivity
CREATE TABLE IF NOT EXISTS `useractivity` (
  `activityID` int(11) NOT NULL AUTO_INCREMENT,
  `userID` mediumint(11) NOT NULL,
  `activityTypeID` mediumint(11) NOT NULL,
  `activityData` varchar(100) DEFAULT NULL,
  `activityProjectID` int(11) DEFAULT NULL,
  `activityTaskListID` int(11) DEFAULT NULL,
  `activityTaskID` int(11) DEFAULT NULL,
  `problemID` int(11) DEFAULT NULL,
  `activityDate` datetime NOT NULL,
  PRIMARY KEY (`activityID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.userorganisation
CREATE TABLE IF NOT EXISTS `userorganisation` (
  `userID` mediumint(11) NOT NULL,
  `organisationID` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedID` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedID` int(11) DEFAULT NULL,
  PRIMARY KEY (`userID`,`organisationID`),
  KEY `fk_user_org` (`organisationID`),
  CONSTRAINT `FK_userorganisation_organisation` FOREIGN KEY (`organisationID`) REFERENCES `organisation` (`organisationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.userproject
CREATE TABLE IF NOT EXISTS `userproject` (
  `userID` mediumint(11) NOT NULL,
  `projectID` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`userID`,`projectID`),
  KEY `fk_user_project` (`projectID`),
  CONSTRAINT `fk_user_project` FOREIGN KEY (`projectID`) REFERENCES `project` (`projectID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.userreport
CREATE TABLE IF NOT EXISTS `userreport` (
  `userID` int(10) NOT NULL,
  `reportID` int(10) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.users_archive
CREATE TABLE IF NOT EXISTS `users_archive` (
  `id` mediumint(8) unsigned NOT NULL,
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

-- Data exporting was unselected.


-- Dumping structure for table simpricity.users_groups
CREATE TABLE IF NOT EXISTS `users_groups` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` mediumint(8) unsigned NOT NULL,
  `group_id` mediumint(8) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.usertask
CREATE TABLE IF NOT EXISTS `usertask` (
  `userID` mediumint(11) NOT NULL,
  `taskID` int(11) NOT NULL,
  PRIMARY KEY (`userID`,`taskID`),
  KEY `FK_usertask_task` (`taskID`),
  CONSTRAINT `FK_usertask_task` FOREIGN KEY (`taskID`) REFERENCES `task` (`taskID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.user_attributes
CREATE TABLE IF NOT EXISTS `user_attributes` (
  `userID` int(11) NOT NULL,
  `vip` char(1) NOT NULL DEFAULT 'n',
  `countryID` int(11) DEFAULT NULL,
  `mobilePhoneNo` varchar(20) DEFAULT NULL,
  `faxNo` varchar(20) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='User attirbutes per user data such as VIP user etc';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.user_configuration
CREATE TABLE IF NOT EXISTS `user_configuration` (
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

-- Data exporting was unselected.


-- Dumping structure for table simpricity.user_cookie
CREATE TABLE IF NOT EXISTS `user_cookie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userID` bigint(20) NOT NULL,
  `uuID` varchar(128) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(40) NOT NULL,
  `created_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table simpricity.user_payrate
CREATE TABLE IF NOT EXISTS `user_payrate` (
  `userID` int(10) NOT NULL,
  `payrateID` int(10) NOT NULL,
  `effectiveDate` datetime NOT NULL,
  `defaultRate` decimal(10,2) DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Amount paid to users';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.user_status
CREATE TABLE IF NOT EXISTS `user_status` (
  `statusID` int(11) NOT NULL,
  `userID` mediumint(9) DEFAULT NULL,
  `itemID` int(11) DEFAULT NULL,
  `itemType` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `statuscol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`statusID`),
  UNIQUE KEY `ix_unique` (`userID`,`itemID`,`itemType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='users statuses for various entities e.g. project, task etc e.g. user worried about this task';

-- Data exporting was unselected.


-- Dumping structure for table simpricity.user_taxrate
CREATE TABLE IF NOT EXISTS `user_taxrate` (
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

-- Data exporting was unselected.


-- Dumping structure for view simpricity.vw_select_organisation_detail_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_organisation_detail_sidebar` (
	`description` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARCHAR(49) NULL COLLATE 'utf8mb4_general_ci',
	`id` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`organisationID` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.vw_select_organisation_index_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_organisation_index_sidebar` (
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARCHAR(100) NULL COLLATE 'utf8_general_ci',
	`id` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`userID` VARCHAR(8) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.vw_select_problem_detail_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_problem_detail_sidebar` (
	`description` VARCHAR(13) NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARCHAR(40) NULL COLLATE 'utf8mb4_general_ci',
	`id` CHAR(0) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`problemID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.vw_select_problem_index_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_problem_index_sidebar` (
	`problemName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARCHAR(40) NULL COLLATE 'utf8mb4_general_ci',
	`id` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`userID` VARCHAR(8) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.vw_select_project_detail_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_project_detail_sidebar` (
	`description` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARCHAR(49) NULL COLLATE 'utf8mb4_general_ci',
	`id` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`projectID` BIGINT(20) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.vw_select_project_index_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_project_index_sidebar` (
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARCHAR(100) NULL COLLATE 'utf8_general_ci',
	`id` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`userID` VARCHAR(8) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.vw_select_task_detail_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_task_detail_sidebar` (
	`description` VARCHAR(32) NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARCHAR(40) NULL COLLATE 'utf8mb4_general_ci',
	`id` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`taskID` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.vw_select_task_index_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_task_index_sidebar` (
	`taskDescription` TEXT NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARCHAR(101) NULL COLLATE 'utf8_general_ci',
	`id` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`userID` VARCHAR(8) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.vw_select_time_detail_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_time_detail_sidebar` (
	`description` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARCHAR(40) NULL COLLATE 'utf8mb4_general_ci',
	`id` CHAR(0) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`userID` MEDIUMINT(8) UNSIGNED NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.vw_select_time_index_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_time_index_sidebar` (
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARBINARY(53) NULL,
	`id` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`userID` VARCHAR(8) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.vw_select_user_detail_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_user_detail_sidebar` (
	`description` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARCHAR(40) NULL COLLATE 'utf8mb4_general_ci',
	`id` CHAR(0) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`userID` MEDIUMINT(8) UNSIGNED NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.vw_select_user_index_sidebar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `vw_select_user_index_sidebar` (
	`userName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`column2` VARCHAR(40) NULL COLLATE 'utf8mb4_general_ci',
	`id` VARCHAR(8) NOT NULL COLLATE 'utf8_general_ci',
	`column4` BIGINT(20) NOT NULL,
	`userID` VARCHAR(8) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_account_detail
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_account_detail` (
	`accountid` INT(11) NOT NULL,
	`accountName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`authenticationID` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`clientID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_actual_problem_links
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_actual_problem_links` (
	`problemID` INT(11) NOT NULL,
	`problemLinkID` INT(11) NOT NULL,
	`problemLinkType` INT(11) NOT NULL,
	`createdDate` DATETIME NOT NULL,
	`createdBy` INT(11) NOT NULL,
	`deletedDate` DATETIME NULL,
	`deletedBy` INT(11) NULL,
	`problemLinkName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_client_admin_group
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_client_admin_group` (
	`groupID` MEDIUMINT(8) UNSIGNED NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_client_users
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_client_users` (
	`clientID` INT(11) NOT NULL,
	`organisationID` INT(11) NOT NULL,
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(8) UNSIGNED NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_comments_parent
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_comments_parent` (
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`commentID` INT(11) NOT NULL,
	`parentID` INT(11) NOT NULL,
	`parentTypeID` INT(11) NOT NULL,
	`commentTypeID` INT(11) NOT NULL,
	`commentText` VARCHAR(5000) NOT NULL COLLATE 'utf8_general_ci',
	`createdDate` VARCHAR(116) NULL COLLATE 'utf8mb4_general_ci',
	`createdBy` INT(11) NOT NULL,
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`documentFileName` VARCHAR(100) NULL COLLATE 'utf8_general_ci',
	`documentName` VARCHAR(100) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_email_queue
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_email_queue` (
	`to_email` VARCHAR(128) NOT NULL COLLATE 'utf8_general_ci',
	`subject` VARCHAR(255) NOT NULL COLLATE 'utf8_general_ci',
	`message` TEXT NOT NULL COLLATE 'utf8_general_ci',
	`date_published` DATETIME NULL,
	`date_sent` DATETIME NULL,
	`success` TINYINT(1) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_importances
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_importances` (
	`importanceID` INT(11) NULL,
	`importanceName` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_invoice_detail
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_invoice_detail` (
	`invoiceID` INT(10) NOT NULL,
	`userID` MEDIUMINT(10) NOT NULL,
	`statusID` INT(10) NOT NULL COMMENT 'eg paid, written off etc',
	`supersededBy` INT(10) NULL COMMENT 'Invoice which superseded this one',
	`createdDate` DATETIME NOT NULL,
	`createdBy` MEDIUMINT(8) NOT NULL,
	`description` VARCHAR(50) NOT NULL COMMENT 'Invoice which superseded this one' COLLATE 'utf8_general_ci',
	`comments` VARCHAR(500) NOT NULL COMMENT 'Invoice which superseded this one' COLLATE 'utf8_general_ci',
	`lineNo` INT(10) NOT NULL,
	`taskID` INT(10) NOT NULL,
	`itemDescription` VARCHAR(150) NOT NULL COLLATE 'utf8_general_ci',
	`tax1Rate` DECIMAL(10,2) UNSIGNED NOT NULL,
	`tax2Rate` DECIMAL(10,2) UNSIGNED NOT NULL,
	`tax3Rate` DECIMAL(10,2) UNSIGNED NOT NULL,
	`hourlyRate` DECIMAL(10,2) UNSIGNED NOT NULL,
	`noHours` DECIMAL(10,1) UNSIGNED NOT NULL,
	`agreedRate` DECIMAL(10,1) UNSIGNED NOT NULL COMMENT 'Where rate agreed instead of hourly rate',
	`tax1` DECIMAL(10,2) UNSIGNED NOT NULL,
	`tax2` DECIMAL(10,2) UNSIGNED NOT NULL,
	`tax3` DECIMAL(10,2) UNSIGNED NOT NULL,
	`grossTotal` DECIMAL(10,2) UNSIGNED NOT NULL COMMENT 'Total before tax',
	`netTotal` DECIMAL(10,2) UNSIGNED NOT NULL COMMENT 'Total after tax'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_lookups_by_type
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_lookups_by_type` (
	`clientID` INT(11) NOT NULL,
	`lookupTypeID` INT(11) NOT NULL,
	`lookupSubTypeID` INT(11) NOT NULL,
	`lookupOrder` INT(11) NOT NULL,
	`lookupValueNum` INT(11) NULL,
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`lookupDescription` VARCHAR(200) NOT NULL COLLATE 'utf8_general_ci',
	`createdDate` DATETIME NOT NULL,
	`createdBy` INT(11) NOT NULL,
	`updatedDate` DATETIME NULL,
	`updatedBy` INT(11) NULL,
	`deletedDate` DATETIME NULL,
	`deletedBy` INT(11) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_assignedprojects
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_assignedprojects` (
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`deletedDate` DATETIME NULL,
	`userID` MEDIUMINT(11) NOT NULL,
	`updatedDate` DATETIME NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_attention_required
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_attention_required` (
	`type` VARCHAR(7) NOT NULL COLLATE 'utf8_general_ci',
	`ordercol` BIGINT(20) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectID` INT(11) NOT NULL,
	`taskDescription` TEXT NULL COLLATE 'utf8_general_ci',
	`itemID` INT(11) NOT NULL,
	`assignedTo` INT(11) NULL,
	`organisationID` INT(11) NOT NULL,
	`deletedDate` DATETIME NULL,
	`userID` MEDIUMINT(11) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_client
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_client` (
	`clientID` INT(11) NOT NULL,
	`user_id` MEDIUMINT(8) UNSIGNED NOT NULL,
	`deletedDate` DATETIME NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_critical_work
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_critical_work` (
	`type` VARCHAR(7) NOT NULL COLLATE 'utf8_general_ci',
	`ordercol` BIGINT(20) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectID` INT(11) NOT NULL,
	`taskDescription` TEXT NOT NULL COLLATE 'utf8_general_ci',
	`itemID` INT(11) NOT NULL,
	`assignedTo` INT(11) NULL,
	`organisationID` INT(11) NOT NULL,
	`deletedDate` DATETIME NULL,
	`id` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_important_work
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_important_work` (
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectID` INT(11) NOT NULL,
	`taskDescription` TEXT NOT NULL COLLATE 'utf8_general_ci',
	`taskID` INT(11) NULL,
	`assignedTo` INT(11) NULL,
	`organisationID` INT(11) NOT NULL,
	`deletedDate` DATETIME NULL,
	`userID` MEDIUMINT(11) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_invoices
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_invoices` (
	`invoiceID` INT(10) NOT NULL,
	`statusID` INT(10) NOT NULL COMMENT 'eg paid, written off etc',
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`createdDate` DATETIME NOT NULL,
	`noHours` DECIMAL(32,1) NULL,
	`grossTotal` DECIMAL(32,2) NULL,
	`netTotal` DECIMAL(32,2) NULL,
	`userID` MEDIUMINT(10) NOT NULL,
	`deletedDate` DATETIME NULL,
	`id` INT(10) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_invoice_times
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_invoice_times` (
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskListName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskDescription` VARCHAR(10000) NOT NULL COLLATE 'utf8_general_ci',
	`timeDay` VARCHAR(40) NULL COLLATE 'utf8mb4_general_ci',
	`hours` FLOAT NOT NULL,
	`userID` MEDIUMINT(11) NOT NULL,
	`timeID` INT(10) NOT NULL,
	`deletedDate` DATETIME NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_items
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_items` (
	`projectID` INT(11) NULL,
	`userID` INT(11) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_organisations
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_organisations` (
	`clientID` INT(11) NOT NULL,
	`organisationID` INT(11) NOT NULL,
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(11) NULL,
	`deletedDate` DATETIME NULL,
	`id` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_organisation_events
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_organisation_events` (
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`createdDate` DATETIME NULL,
	`userID` MEDIUMINT(11) NOT NULL,
	`organisationID` INT(11) NOT NULL,
	`type` BIGINT(20) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_org_tasks
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_org_tasks` (
	`userID` MEDIUMINT(11) NOT NULL,
	`taskDescription` TEXT NOT NULL COLLATE 'utf8_general_ci',
	`taskID` INT(11) NOT NULL,
	`deletedDate` DATETIME NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_priorities
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_priorities` (
	`clientID` INT(11) NOT NULL,
	`lookupDescription` VARCHAR(200) NOT NULL COLLATE 'utf8_general_ci',
	`lookupValueNum` INT(11) NULL,
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`lookupOrder` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_problems
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_problems` (
	`problemID` INT(11) NOT NULL,
	`organisationID` INT(11) NOT NULL,
	`problemType` VARCHAR(200) NULL COLLATE 'utf8_general_ci',
	`problemHeader` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`assignedTo` INT(11) NULL,
	`problemScope` VARCHAR(200) NULL COLLATE 'utf8_general_ci',
	`problemStatus` VARCHAR(200) NULL COLLATE 'utf8_general_ci',
	`problemPriority` VARCHAR(200) NULL COLLATE 'utf8_general_ci',
	`problemScopeID` INT(11) NULL,
	`createdBy` INT(11) NOT NULL,
	`id` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_problem_priorities
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_problem_priorities` (
	`clientID` INT(11) NOT NULL,
	`lookupTypeID` INT(11) NOT NULL,
	`lookupSubTypeID` INT(11) NOT NULL,
	`lookupOrder` INT(11) NOT NULL,
	`lookupValueNum` INT(11) NULL,
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`lookupDescription` VARCHAR(200) NOT NULL COLLATE 'utf8_general_ci',
	`createdDate` DATETIME NOT NULL,
	`createdBy` INT(11) NOT NULL,
	`updatedDate` DATETIME NULL,
	`updatedBy` INT(11) NULL,
	`deletedDate` DATETIME NULL,
	`deletedBy` INT(11) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_problem_scope
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_problem_scope` (
	`clientID` INT(11) NOT NULL,
	`lookupTypeID` INT(11) NOT NULL,
	`lookupSubTypeID` INT(11) NOT NULL,
	`lookupOrder` INT(11) NOT NULL,
	`lookupValueNum` INT(11) NULL,
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`lookupDescription` VARCHAR(200) NOT NULL COLLATE 'utf8_general_ci',
	`createdDate` DATETIME NOT NULL,
	`createdBy` INT(11) NOT NULL,
	`updatedDate` DATETIME NULL,
	`updatedBy` INT(11) NULL,
	`deletedDate` DATETIME NULL,
	`deletedBy` INT(11) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_problem_statuses
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_problem_statuses` (
	`clientID` INT(11) NOT NULL,
	`lookupTypeID` INT(11) NOT NULL,
	`lookupSubTypeID` INT(11) NOT NULL,
	`lookupOrder` INT(11) NOT NULL,
	`lookupValueNum` INT(11) NULL,
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`lookupDescription` VARCHAR(200) NOT NULL COLLATE 'utf8_general_ci',
	`createdDate` DATETIME NOT NULL,
	`createdBy` INT(11) NOT NULL,
	`updatedDate` DATETIME NULL,
	`updatedBy` INT(11) NULL,
	`deletedDate` DATETIME NULL,
	`deletedBy` INT(11) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_projects
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_projects` (
	`projectID` INT(11) NOT NULL,
	`organisationID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`createdDate` DATETIME NOT NULL,
	`createdBy` INT(11) NOT NULL,
	`updatedDate` DATETIME NULL,
	`updatedBy` INT(11) NULL,
	`deletedDate` DATETIME NULL,
	`deletedBy` INT(11) NULL,
	`userID` MEDIUMINT(11) NOT NULL,
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`id` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_reports
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_reports` (
	`lookupValueNum` INT(11) NULL,
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`userID` INT(10) NOT NULL,
	`deletedDate` DATETIME NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_statuses
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_statuses` (
	`clientID` INT(11) NOT NULL,
	`lookupDescription` VARCHAR(200) NOT NULL COLLATE 'utf8_general_ci',
	`lookupValueNum` INT(11) NULL,
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_tasks
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_tasks` (
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskListID` INT(11) NOT NULL,
	`taskListName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskID` INT(11) NOT NULL,
	`taskDescription` VARCHAR(10000) NOT NULL COLLATE 'utf8_general_ci',
	`assignedTo` INT(11) NULL,
	`deletedDate` DATETIME NULL,
	`id` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_tasktypes
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_tasktypes` (
	`clientID` INT(11) NOT NULL,
	`lookupDescription` VARCHAR(200) NOT NULL COLLATE 'utf8_general_ci',
	`lookupValueNum` INT(11) NULL,
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_time
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_time` (
	`timeID` INT(10) NOT NULL,
	`timeDay` VARCHAR(40) NULL COLLATE 'utf8mb4_general_ci',
	`timeDayraw` DATETIME NOT NULL,
	`hours` FLOAT NOT NULL,
	`taskID` INT(11) NOT NULL,
	`timeTypeID` INT(11) NOT NULL,
	`userID` MEDIUMINT(11) NOT NULL,
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`deletedDate` DATETIME NULL,
	`comments` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`taskDescription` VARCHAR(10000) NOT NULL COLLATE 'utf8_general_ci',
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`id` INT(10) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_timesheet
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_timesheet` (
	`timeID` INT(10) NOT NULL,
	`timeDay` DATETIME NOT NULL,
	`timeDayF` VARCHAR(40) NULL COLLATE 'utf8mb4_general_ci',
	`taskDescription` TEXT NULL COLLATE 'utf8_general_ci',
	`hours` DOUBLE NULL,
	`userID` INT(8) UNSIGNED NULL,
	`timetypeID` INT(11) NOT NULL,
	`lookupTypeID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_my_users
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_my_users` (
	`user_id` MEDIUMINT(8) UNSIGNED NOT NULL,
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`organisationID` INT(11) NOT NULL,
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`active` TINYINT(4) UNSIGNED NULL,
	`name` VARCHAR(101) NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(11) NOT NULL,
	`activeDesc` VARCHAR(3) NOT NULL COLLATE 'utf8_general_ci',
	`id` MEDIUMINT(8) UNSIGNED NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_new_user_emails
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_new_user_emails` (
	`email` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`id` MEDIUMINT(8) UNSIGNED NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_organisations
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_organisations` (
	`organisationID` INT(11) NOT NULL,
	`clientID` INT(11) NOT NULL,
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`createdDate` DATETIME NOT NULL,
	`createdBy` INT(11) NOT NULL,
	`updatedDate` DATETIME NULL,
	`updatedBy` INT(11) NULL,
	`deletedDate` DATETIME NULL,
	`deletedBy` INT(11) NULL,
	`userID` INT(11) UNSIGNED NULL,
	`id` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_organisation_activity
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_organisation_activity` (
	`activityID` INT(11) NOT NULL,
	`userID` MEDIUMINT(11) NOT NULL,
	`activityData` VARCHAR(100) NULL COLLATE 'utf8_general_ci',
	`organisationID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_organisation_project_managers
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_organisation_project_managers` (
	`organisationID` INT(11) NOT NULL,
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(8) UNSIGNED NOT NULL,
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_organisation_project_users
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_organisation_project_users` (
	`organisationID` INT(11) NOT NULL,
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(8) UNSIGNED NOT NULL,
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_organisation_users
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_organisation_users` (
	`organisationID` INT(11) NOT NULL,
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_problems
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_problems` (
	`clientID` INT(11) NOT NULL,
	`problemID` INT(11) NOT NULL,
	`organisationID` INT(11) NOT NULL,
	`problemType` VARCHAR(200) NULL COLLATE 'utf8_general_ci',
	`problemDescription` VARCHAR(2000) NOT NULL COLLATE 'utf8_general_ci',
	`noOfPeopleAffected` INT(11) NOT NULL,
	`scope` INT(11) NOT NULL,
	`problemHeader` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`assignedTo` INT(11) NULL,
	`lookupDescription` VARCHAR(200) NULL COLLATE 'utf8_general_ci',
	`problemScope` VARCHAR(200) NULL COLLATE 'utf8_general_ci',
	`problemStatus` VARCHAR(200) NULL COLLATE 'utf8_general_ci',
	`problemPriority` VARCHAR(200) NULL COLLATE 'utf8_general_ci',
	`problemScopeID` INT(11) NULL,
	`problemPriorityID` INT(11) NULL,
	`problemStatusID` INT(11) NULL,
	`createdBy` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_problem_activity
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_problem_activity` (
	`itemID` INT(11) NOT NULL,
	`activity` VARCHAR(6) NOT NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_problem_assignees
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_problem_assignees` (
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`userid` MEDIUMINT(11) NOT NULL,
	`problemID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_problem_edit
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_problem_edit` (
	`clientID` INT(11) NOT NULL,
	`problemID` INT(11) NOT NULL,
	`organisationID` INT(11) NOT NULL,
	`problemDescription` VARCHAR(2000) NOT NULL COLLATE 'utf8_general_ci',
	`noOfPeopleAffected` INT(11) NOT NULL,
	`problemScopeID` INT(11) NOT NULL,
	`problemSubTypeID` INT(11) NULL,
	`problemTypeID` INT(11) NOT NULL,
	`problemStatusID` INT(11) NULL,
	`problemPriorityID` INT(11) NULL,
	`problemHeader` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`assignedTo` INT(11) NULL,
	`createdBy` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_problem_json
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_problem_json` (
	`Name_exp_1` VARCHAR(343) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_projectgantt_jq
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_projectgantt_jq` (
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`updatedDate` DATETIME NULL,
	`updatedBy` INT(11) NULL,
	`taskListID` INT(11) NOT NULL,
	`taskListName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskListDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`taskID` INT(11) NOT NULL,
	`taskDescription` VARCHAR(10000) NOT NULL COLLATE 'utf8_general_ci',
	`taskOrderID` BIGINT(11) NOT NULL,
	`deletedDate` DATETIME NULL,
	`taskStartDate` BIGINT(14) NOT NULL,
	`assignedTo` INT(11) NULL,
	`taskEndDate` BIGINT(14) NULL,
	`taskTimeEstimate` DECIMAL(10,1) NULL,
	`taskStartDate_unformatted` DATETIME NULL,
	`time_estimate` DECIMAL(10,1) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_activity
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_activity` (
	`activityID` INT(11) NOT NULL,
	`userID` MEDIUMINT(11) NOT NULL,
	`activityTypeID` MEDIUMINT(11) NOT NULL,
	`activityData` VARCHAR(100) NULL COLLATE 'utf8_general_ci',
	`activityProjectID` INT(11) NULL,
	`activityTaskListID` INT(11) NULL,
	`activityTaskID` INT(11) NULL,
	`activityDate` DATETIME NOT NULL,
	`taskID` INT(11) NULL,
	`taskListID` INT(11) NULL,
	`taskTypeID` INT(11) NULL,
	`taskDescription` VARCHAR(10000) NULL COLLATE 'utf8_general_ci',
	`taskStatusID` INT(11) NULL,
	`taskPriorityID` INT(11) NULL,
	`assignedTo` INT(11) NULL,
	`createdDate` DATETIME NULL,
	`createdBy` INT(11) NULL,
	`updatedDate` DATETIME NULL,
	`updatedBy` INT(11) NULL,
	`deletedDate` DATETIME NULL,
	`deletedBy` INT(11) NULL,
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_assignees
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_assignees` (
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`userid` MEDIUMINT(11) NOT NULL,
	`taskID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_detail
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_detail` (
	`projectID` INT(11) NOT NULL,
	`organisationID` INT(11) NOT NULL,
	`programmeID` INT(11) NULL,
	`clientID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`stakeholderID` INT(11) NULL,
	`projectManagerID` INT(11) NULL,
	`deliverables` VARCHAR(1500) NULL COLLATE 'utf8_general_ci',
	`budget` DECIMAL(10,0) NULL,
	`importance` INT(11) NULL,
	`createdDate` DATETIME NOT NULL,
	`createdBy` INT(11) NOT NULL,
	`updatedDate` DATETIME NULL,
	`updatedBy` INT(11) NULL,
	`deletedDate` DATETIME NULL,
	`deletedBy` INT(11) NULL,
	`organisationName` VARCHAR(100) NULL COLLATE 'utf8_general_ci',
	`shFirstName` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`shLastName` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`importanceDescription` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`pmFirstName` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`pmLastName` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(8) UNSIGNED NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_documents
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_documents` (
	`documentID` INT(11) NOT NULL,
	`documentTypeID` INT(11) NOT NULL,
	`documentParentID` INT(11) NOT NULL,
	`documentName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`documentFileName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`documentTitle` VARCHAR(100) NULL COLLATE 'utf8_general_ci',
	`createdDate` DATETIME NOT NULL,
	`createdBy` INT(11) NOT NULL,
	`deletedDate` DATETIME NULL,
	`deletedBy` INT(11) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_gantt
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_gantt` (
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`updatedDate` DATETIME NULL,
	`updatedBy` INT(11) NULL,
	`taskListID` INT(11) NULL,
	`taskListName` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`taskListDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`taskID` INT(11) NULL,
	`taskDescription` VARCHAR(10000) NULL COLLATE 'utf8_general_ci',
	`deletedDate` DATETIME NULL,
	`taskStartDate` DATETIME NULL,
	`assignedTo` INT(11) NULL,
	`taskEndDate` DATETIME NULL,
	`taskTimeEstimate` DECIMAL(10,1) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_opinion
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_opinion` (
	`opinionID` INT(11) NOT NULL,
	`projectID` INT(11) NOT NULL,
	`userID` INT(11) NOT NULL,
	`itemID` INT(11) NOT NULL,
	`itemType` INT(11) NOT NULL COMMENT 'Type of thing the opinion expressed about: project, tasklist, task',
	`opinionType` INT(11) NULL,
	`opinion` VARCHAR(250) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_opinion_detail
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_opinion_detail` (
	`opinionID` INT(11) NOT NULL,
	`projectID` INT(11) NOT NULL,
	`userID` INT(11) NOT NULL,
	`itemID` INT(11) NOT NULL,
	`itemType` INT(11) NOT NULL COMMENT 'Type of thing the opinion expressed about: project, tasklist, task',
	`opinionType` INT(11) NULL,
	`opinionDescription` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`userName` VARCHAR(101) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_pie
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_pie` (
	`projectID` INT(11) NOT NULL,
	`taskListName` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`countTasks` BIGINT(21) NOT NULL,
	`deletedDate` DATETIME NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_tasklists
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_tasklists` (
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`clientID` INT(11) NOT NULL,
	`taskListID` INT(11) NOT NULL,
	`taskListName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(11) NOT NULL,
	`deletedDate` DATETIME NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_tasks
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_tasks` (
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`taskListID` INT(11) NOT NULL,
	`taskListName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskListDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`taskID` INT(11) NULL,
	`taskDescription` VARCHAR(10000) NULL COLLATE 'utf8_general_ci',
	`taskDescriptionShort` VARCHAR(83) NULL COLLATE 'utf8_general_ci',
	`taskTypeID` INT(11) NULL,
	`taskStatusID` INT(11) NULL,
	`taskPriorityID` INT(11) NULL,
	`assignedTo` INT(11) NULL,
	`taskStatus` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`taskPriority` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_users
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_users` (
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`userid` MEDIUMINT(11) NOT NULL,
	`projectID` INT(11) NOT NULL,
	`taskListID` INT(11) NOT NULL,
	`taskID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_project_user_emails
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_project_user_emails` (
	`email` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`projectID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_registered_user
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_registered_user` (
	`userID` MEDIUMINT(8) UNSIGNED NOT NULL,
	`email` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`company` INT(11) UNSIGNED NULL COMMENT 'Changed from VARCHAR by GFJ - main org ID',
	`phone` VARCHAR(20) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_search
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_search` (
	`projectID` INT(11) NOT NULL,
	`organisationID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`taskListID` INT(11) NULL,
	`taskListName` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`taskListDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`taskID` INT(11) NULL,
	`taskDescription` VARCHAR(10000) NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(11) NOT NULL,
	`id` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_subscribers_recent
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_subscribers_recent` (
	`accountName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`authenticationID` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`authenticationID2` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`authenticationID3` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`clientName` VARCHAR(100) NULL COLLATE 'utf8_general_ci',
	`city` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`country` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`createdDate` DATETIME NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_subscription
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_subscription` (
	`authenticationID` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`authenticationID2` VARCHAR(45) NULL COLLATE 'utf8_general_ci',
	`organisationID` INT(11) NOT NULL,
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`firstname` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`lastname` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`phone` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`email` VARCHAR(75) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_suggest_problem_links
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_suggest_problem_links` (
	`id` INT(11) NOT NULL,
	`value` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_suggest_project_links
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_suggest_project_links` (
	`id` INT(11) NOT NULL,
	`value` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_tasklist_activity
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_tasklist_activity` (
	`taskListID` INT(11) NOT NULL,
	`date` DATETIME NULL,
	`userID` BIGINT(20) NULL,
	`name` VARCHAR(101) NULL COLLATE 'utf8_general_ci',
	`activity` VARCHAR(12) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_tasklist_project
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_tasklist_project` (
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskListID` INT(11) NOT NULL,
	`taskListName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskListDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`clientID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_tasklist_task
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_tasklist_task` (
	`taskListID` INT(11) NOT NULL,
	`taskListName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskListDescription` VARCHAR(500) NULL COLLATE 'utf8_general_ci',
	`clientID` INT(11) NOT NULL,
	`taskID` INT(11) NOT NULL,
	`taskDescription` VARCHAR(10000) NOT NULL COLLATE 'utf8_general_ci',
	`taskName` VARCHAR(83) NOT NULL COLLATE 'utf8_general_ci',
	`taskPriorityID` INT(11) NULL,
	`taskStatusID` INT(11) NULL,
	`taskStatus` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`taskPriority` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_tasklist_users
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_tasklist_users` (
	`id` MEDIUMINT(8) UNSIGNED NOT NULL,
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`taskListID` INT(11) NOT NULL,
	`projectID` INT(11) NOT NULL,
	`clientID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_task_dependency
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_task_dependency` (
	`taskID` INT(11) NOT NULL,
	`taskListID` INT(11) NOT NULL,
	`clientID` INT(11) NOT NULL,
	`taskTypeID` INT(11) NOT NULL,
	`taskDescription` VARCHAR(10000) NOT NULL COLLATE 'utf8_general_ci',
	`taskStatusID` INT(11) NULL,
	`taskPriorityID` INT(11) NULL,
	`assignedTo` INT(11) NULL,
	`taskStartDate` DATETIME NULL,
	`taskTimeEstimate` DECIMAL(10,1) NULL,
	`taskPercentComplete` INT(11) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_task_detail
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_task_detail` (
	`taskID` INT(11) NOT NULL,
	`taskDescription` VARCHAR(10000) NOT NULL COLLATE 'utf8_general_ci',
	`taskTypeID` INT(11) NOT NULL,
	`taskPriority` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`taskStatus` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`taskPriorityID` INT(11) NULL,
	`taskStatusID` INT(11) NULL,
	`assignedTo` INT(11) NULL,
	`assignedToName` VARCHAR(101) NULL COLLATE 'utf8_general_ci',
	`taskStartDate` VARCHAR(10) NULL COLLATE 'utf8mb4_general_ci',
	`taskTimeEstimate` DECIMAL(10,1) NULL,
	`taskPercentComplete` INT(11) NULL,
	`taskLinkID` INT(11) NULL,
	`linkedTaskID` INT(11) NULL,
	`linkedTaskDescription` VARCHAR(10000) NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`tasklistName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_task_documents
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_task_documents` (
	`documentID` INT(11) NOT NULL,
	`documentTypeID` INT(11) NOT NULL,
	`documentParentID` INT(11) NOT NULL,
	`documentName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`documentFileName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`documentTitle` VARCHAR(100) NULL COLLATE 'utf8_general_ci',
	`createdDate` DATETIME NOT NULL,
	`createdBy` INT(11) NOT NULL,
	`deletedDate` DATETIME NULL,
	`deletedBy` INT(11) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_task_links
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_task_links` (
	`taskID` INT(11) NOT NULL,
	`taskListID` INT(11) NOT NULL,
	`taskIDIn` INT(11) NOT NULL,
	`taskListIDIn` INT(11) NOT NULL,
	`taskDescription` VARCHAR(23) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_task_statuses
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_task_statuses` (
	`clientID` INT(11) NOT NULL,
	`lookupDescription` VARCHAR(200) NOT NULL COLLATE 'utf8_general_ci',
	`lookupValueNum` INT(11) NULL,
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`lookupOrder` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_task_users
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_task_users` (
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`userid` MEDIUMINT(11) NOT NULL,
	`projectID` INT(11) NOT NULL,
	`taskListID` INT(11) NOT NULL,
	`taskID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_task_user_emails
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_task_user_emails` (
	`email` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`taskID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_time_calendar
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_time_calendar` (
	`id` INT(10) NOT NULL,
	`title` VARCHAR(10000) NOT NULL COLLATE 'utf8_general_ci',
	`start` VARCHAR(10) NULL COLLATE 'utf8mb4_general_ci',
	`url` INT(10) NOT NULL,
	`assignedTo` INT(11) NULL,
	`userID` MEDIUMINT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_time_detail
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_time_detail` (
	`timeID` INT(10) NOT NULL,
	`timeDay` VARCHAR(40) NULL COLLATE 'utf8mb4_general_ci',
	`hours` FLOAT NOT NULL,
	`taskID` INT(11) NOT NULL,
	`timeTypeID` INT(11) NOT NULL,
	`userID` MEDIUMINT(11) NOT NULL,
	`taskDescription` VARCHAR(10000) NOT NULL COLLATE 'utf8_general_ci',
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`comments` VARCHAR(50) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_time_grid
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_time_grid` (
	`project` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectid` INT(11) NOT NULL,
	`tasklist` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`tasklistid` INT(11) NOT NULL,
	`id` INT(10) NOT NULL,
	`task` VARCHAR(10000) NOT NULL COLLATE 'utf8_general_ci',
	`taskid` INT(11) NOT NULL,
	`timeDay` DATETIME NOT NULL,
	`timeDayDate` DATE NULL,
	`starthour` VARCHAR(7) NULL COLLATE 'utf8mb4_general_ci',
	`startmin` VARCHAR(2) NULL COLLATE 'utf8mb4_general_ci',
	`hours` DOUBLE(17,0) NOT NULL,
	`mins` DOUBLE NOT NULL,
	`minsformat` DOUBLE NOT NULL,
	`assignedTo` INT(11) NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_time_task
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_time_task` (
	`project` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`projectid` INT(11) NOT NULL,
	`tasklist` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`tasklistid` INT(11) NOT NULL,
	`task` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskid` INT(11) NOT NULL,
	`assignedTo` INT(11) NULL,
	`id` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_time_type
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_time_type` (
	`lookupValueNum` INT(11) NULL,
	`lookupValueChar` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`clientID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_users
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_users` (
	`id` MEDIUMINT(8) UNSIGNED NOT NULL,
	`username` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`email` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`active` TINYINT(1) UNSIGNED NULL,
	`phone` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_user_assigned
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_user_assigned` (
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskListID` INT(11) NOT NULL,
	`taskListName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`taskID` INT(11) NOT NULL,
	`taskDescription` VARCHAR(10000) NOT NULL COLLATE 'utf8_general_ci',
	`assignedTo` INT(11) NULL,
	`deletedDate` DATETIME NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_user_attributes
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_user_attributes` (
	`userID` INT(11) NOT NULL,
	`vip` CHAR(1) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_user_context_full
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_user_context_full` (
	`id` MEDIUMINT(8) UNSIGNED NOT NULL,
	`clientID` INT(11) NOT NULL,
	`username` VARCHAR(30) NOT NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`organisationname` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`isSuperUser` TINYINT(1) NOT NULL,
	`isStaff` TINYINT(1) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_user_context_minimal
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_user_context_minimal` (
	`id` MEDIUMINT(8) UNSIGNED NOT NULL,
	`clientID` INT(11) NOT NULL,
	`username` VARCHAR(30) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_user_current_projects
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_user_current_projects` (
	`userID` MEDIUMINT(11) NOT NULL,
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_user_detail
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_user_detail` (
	`id` MEDIUMINT(8) UNSIGNED NOT NULL,
	`username` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`email` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`active` TINYINT(1) UNSIGNED NULL,
	`phone` VARCHAR(20) NULL COLLATE 'utf8_general_ci',
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`vip` CHAR(1) NULL COLLATE 'utf8_general_ci',
	`pay_rate` DECIMAL(10,2) NULL,
	`tax_rate` DECIMAL(10,2) NULL,
	`clientID` INT(11) NOT NULL
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_user_group
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_user_group` (
	`userID` MEDIUMINT(8) UNSIGNED NOT NULL,
	`group_id` MEDIUMINT(8) UNSIGNED NOT NULL,
	`name` VARCHAR(20) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_user_group_detail
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_user_group_detail` (
	`userID` MEDIUMINT(8) UNSIGNED NOT NULL,
	`group_id` MEDIUMINT(8) UNSIGNED NOT NULL,
	`name` VARCHAR(20) NOT NULL COLLATE 'utf8_general_ci',
	`description` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_user_login
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_user_login` (
	`id` MEDIUMINT(8) UNSIGNED NOT NULL,
	`username` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`email` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`active` TINYINT(1) UNSIGNED NULL,
	`password` VARCHAR(40) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_user_potential_projects
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_user_potential_projects` (
	`organisationID` INT(11) NOT NULL,
	`organisationName` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`userID` MEDIUMINT(8) UNSIGNED NOT NULL,
	`first_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`last_name` VARCHAR(50) NULL COLLATE 'utf8_general_ci',
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for view simpricity.v_user_projects
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_user_projects` (
	`userID` MEDIUMINT(11) NOT NULL,
	`organisationID` INT(11) NOT NULL,
	`projectID` INT(11) NOT NULL,
	`projectName` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;


-- Dumping structure for trigger simpricity.problem_BUPD
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='';
DELIMITER //
CREATE TRIGGER `problem_BUPD` BEFORE UPDATE ON `problem` FOR EACH ROW BEGIN
    INSERT INTO problem_archive 
	SELECT * from problem where problemID = OLD.problemID;
  END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;


-- Dumping structure for trigger simpricity.trg_organisation
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO';
DELIMITER //
CREATE TRIGGER `trg_organisation` BEFORE UPDATE ON `organisation` FOR EACH ROW BEGIN
    INSERT INTO organisation_archive
	select * from organisation where organisationID = old.organisationID;
  END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;


-- Dumping structure for trigger simpricity.trg_project
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO';
DELIMITER //
CREATE TRIGGER `trg_project` BEFORE UPDATE ON `project` FOR EACH ROW BEGIN
    INSERT INTO project_archive 
	SELECT * from project where projectID = OLD.projectID;
  END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;


-- Dumping structure for trigger simpricity.trg_task
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO';
DELIMITER //
CREATE TRIGGER `trg_task` BEFORE UPDATE ON `task` FOR EACH ROW BEGIN
    INSERT INTO task_archive
    select * from task where taskID = OLD.taskID;
  END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;


-- Dumping structure for trigger simpricity.trg_tasklist
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO';
DELIMITER //
CREATE TRIGGER `trg_tasklist` BEFORE UPDATE ON `tasklist` FOR EACH ROW BEGIN
    INSERT INTO tasklist_archive 
	select * from tasklist where taskListID = OLD.taskListID;
  END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;


-- Dumping structure for trigger simpricity.trg_users
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO';
DELIMITER //
CREATE TRIGGER `trg_users` BEFORE UPDATE ON `users` FOR EACH ROW BEGIN
    INSERT INTO users_archive 
	select * from users where id = OLD.id;
  END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;


-- Dumping structure for view simpricity.vw_select_organisation_detail_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_organisation_detail_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_organisation_detail_sidebar` AS select 'Created:' AS `description`,date_format(`org`.`createdDate`,'%d %b %Y') AS `column2`,'' AS `id`,0 AS `column4`,`org`.`organisationID` AS `organisationID` from `organisation` `org` union select 'Last changed:' AS `description`,date_format(`org`.`createdDate`,'%d %b %Y') AS `column2`,'' AS `id`,3 AS `column4`,`org`.`organisationID` AS `organisationID` from `organisation` `org` union select 'Organisation projects' AS `Organisation projects`,'' AS `column2`,'' AS `id`,5 AS `5`,'' AS `organisationID` union select `prj`.`projectName` AS `projectName`,concat('Created: ',date_format(`prj`.`createdDate`,'%d %b %Y')) AS `concat ('Created: ', prj.createdDate)`,`prj`.`projectID` AS `projectID`,7 AS `7`,`org`.`organisationID` AS `organisationID` from (`organisation` `org` join `project` `prj` on((`prj`.`organisationID` = `org`.`organisationID`))) order by 4 limit 40;


-- Dumping structure for view simpricity.vw_select_organisation_index_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_organisation_index_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_organisation_index_sidebar` AS select 'New organisations' AS `organisationName`,'' AS `column2`,'' AS `id`,0 AS `column4`,'' AS `userID` union select `org`.`organisationName` AS `organisationName`,`org`.`createdDate` AS `createdDate`,`org`.`organisationID` AS `id`,3 AS `3`,`usr`.`id` AS `userID` from ((`organisation` `org` join `client` `cl` on((`org`.`clientID` = `cl`.`clientID`))) join `users` `usr` on((`usr`.`company` = `org`.`organisationID`))) where (`org`.`createdDate` > `FN_PAST_DATE`(10)) union select 'Changed organisations' AS `Changed organisations`,'' AS `column2`,'' AS `id`,5 AS `5`,'' AS `userID` union select `org`.`organisationName` AS `organisationName`,`org`.`updatedDate` AS `updatedDate`,`org`.`organisationID` AS `id`,7 AS `7`,`usr`.`id` AS `userID` from ((`organisation` `org` join `client` `cl` on((`org`.`clientID` = `cl`.`clientID`))) join `users` `usr` on((`usr`.`company` = `org`.`organisationID`))) where (`org`.`updatedDate` > `FN_PAST_DATE`(10)) union select 'New users' AS `New users`,'' AS `column2`,'' AS `id`,9 AS `9`,'' AS `userID` union select `org`.`organisationName` AS `organisationName`,`usr`.`username` AS `username`,`org`.`organisationID` AS `id`,11 AS `11`,`usr`.`id` AS `userID` from ((`organisation` `org` join `client` `cl` on((`org`.`clientID` = `cl`.`clientID`))) join `users` `usr` on((`org`.`organisationID` = `usr`.`company`))) where (`usr`.`created_on` > `FN_PAST_DATE`(10)) union select 'New projects' AS `New projects`,'' AS `column2`,'' AS `id`,13 AS `13`,'' AS `userID` union select `org`.`organisationName` AS `organisationName`,`prj`.`projectName` AS `projectName`,`org`.`organisationID` AS `id`,15 AS `15`,`usr`.`id` AS `userID` from (((`organisation` `org` join `client` `cl` on((`org`.`clientID` = `cl`.`clientID`))) join `users` `usr` on((`org`.`organisationID` = `usr`.`company`))) join `project` `prj` on((`prj`.`organisationID` = `org`.`organisationID`))) where (`usr`.`created_on` > `FN_PAST_DATE`(10)) order by 4 limit 40;


-- Dumping structure for view simpricity.vw_select_problem_detail_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_problem_detail_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_problem_detail_sidebar` AS select 'Created:' AS `description`,date_format(`prob`.`createdDate`,'%d %b %Y') AS `column2`,'' AS `id`,0 AS `column4`,`prob`.`problemID` AS `problemID` from `problem` `prob` union select 'Last changed:' AS `description`,date_format(`prob`.`createdDate`,'%d %b %Y') AS `column2`,'' AS `id`,3 AS `column4`,`prob`.`problemID` AS `problemID` from `problem` `prob` order by 4;


-- Dumping structure for view simpricity.vw_select_problem_index_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_problem_index_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_problem_index_sidebar` AS select 'New problems' AS `problemName`,'' AS `column2`,'' AS `id`,0 AS `column4`,'' AS `userID` union select distinct `prob`.`problemHeader` AS `problemHeader`,date_format(`prob`.`createdDate`,'%d %b %Y') AS `createdDate`,`prob`.`problemID` AS `problemID`,3 AS `3`,`uorg`.`userID` AS `userID` from (`problem` `prob` join `userorganisation` `uorg` on((`prob`.`organisationID` = `uorg`.`organisationID`))) where (`prob`.`createdDate` > `fn_past_date`(-(10))) union select 'Changed problems' AS `Changed problems`,'' AS `column2`,'' AS `id`,5 AS `5`,'' AS `userID` union select `prob`.`problemHeader` AS `problemHeader`,date_format(`prob`.`updatedDate`,'%d %b %Y') AS `updatedDate`,`prob`.`problemID` AS `problemID`,7 AS `7`,`uorg`.`userID` AS `userID` from (`problem` `prob` join `userorganisation` `uorg` on((`prob`.`organisationID` = `uorg`.`organisationID`))) where (`prob`.`updatedDate` > `fn_past_date`(-(20))) order by 4,1,2 limit 40;


-- Dumping structure for view simpricity.vw_select_project_detail_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_project_detail_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_project_detail_sidebar` AS select 'Created:' AS `description`,date_format(`proj`.`createdDate`,'%d %b %Y') AS `column2`,'' AS `id`,0 AS `column4`,`proj`.`projectID` AS `projectID` from `project` `proj` union select 'Last changed:' AS `description`,date_format(`proj`.`updatedDate`,'%d %b %Y') AS `column2`,'' AS `id`,3 AS `column4`,`proj`.`projectID` AS `projectID` from `project` `proj` union select 'Project tasks' AS `description`,'' AS `column2`,'' AS `id`,5 AS `column4`,0 AS `projectID` union select `proj`.`projectName` AS `description`,concat('Created: ',date_format(`proj`.`createdDate`,'%d %b %Y')) AS `column2`,`proj`.`projectID` AS `id`,7 AS `column4`,`proj`.`projectID` AS `projectID` from (`project` `proj` join `tasklist` `tsk` on((`proj`.`projectID` = `tsk`.`projectID`))) order by 4 limit 40;


-- Dumping structure for view simpricity.vw_select_project_index_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_project_index_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_project_index_sidebar` AS select 'New projects' AS `projectName`,'' AS `column2`,'' AS `id`,0 AS `column4`,'' AS `userID` union select distinct `proj`.`projectName` AS `projectName`,`proj`.`createdDate` AS `createdDate`,`proj`.`projectID` AS `projectID`,3 AS `3`,`upr`.`userID` AS `userID` from (`project` `proj` join `userproject` `upr` on((`proj`.`projectID` = `upr`.`projectID`))) where (`proj`.`createdDate` > `fn_past_date`(10)) union select 'Changed projects' AS `Changed projects`,'' AS `column2`,'' AS `id`,5 AS `5`,'' AS `userID` union select `proj`.`projectName` AS `projectName`,`proj`.`updatedDate` AS `updatedDate`,`proj`.`projectID` AS `projectID`,7 AS `7`,`upr`.`userID` AS `userID` from (`project` `proj` join `userproject` `upr` on((`proj`.`projectID` = `upr`.`projectID`))) where (`proj`.`updatedDate` > `fn_past_date`(10)) union select 'New users' AS `New users`,'' AS `column2`,'' AS `id`,9 AS `9`,'' AS `userID` union select `proj`.`projectName` AS `projectName`,`usr`.`username` AS `username`,`proj`.`projectID` AS `projectID`,11 AS `11`,`upr2`.`userID` AS `userID` from (((`project` `proj` left join `userproject` `upr` on((`proj`.`projectID` = `upr`.`projectID`))) join `users` `usr` on((`upr`.`userID` = `usr`.`id`))) join `userproject` `upr2` on((`proj`.`projectID` = `upr2`.`projectID`))) where (`usr`.`created_on` > `fn_past_date`(10)) union select 'New tasklists' AS `New tasklists`,'' AS `column2`,'' AS `id`,13 AS `13`,'' AS `userID` union select `proj`.`projectName` AS `projectName`,`tsk`.`taskListName` AS `taskListName`,`proj`.`projectID` AS `projectID`,15 AS `15`,`upr`.`userID` AS `userID` from ((`project` `proj` join `userproject` `upr` on((`proj`.`projectID` = `upr`.`projectID`))) join `tasklist` `tsk` on((`tsk`.`projectID` = `proj`.`projectID`))) where (`tsk`.`createdDate` > `fn_past_date`(10)) order by 4,1,2 limit 40;


-- Dumping structure for view simpricity.vw_select_task_detail_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_task_detail_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_task_detail_sidebar` AS select 'Created:' AS `description`,date_format(`tsk`.`createdDate`,'%d %b %Y') AS `column2`,'' AS `id`,0 AS `column4`,`tsk`.`taskID` AS `taskID` from `task` `tsk` union select 'Last changed:' AS `description`,date_format(`tsk`.`updatedDate`,'%d %b %Y') AS `column2`,'' AS `id`,3 AS `column4`,`tsk`.`taskID` AS `taskID` from `task` `tsk` union select 'Task activity' AS `Task activity`,'' AS `column2`,'' AS `id`,13 AS `13`,'' AS `taskID` union select concat('Comment: ',left(`comment`.`commentText`,20),'...') AS `Comment`,date_format(`comment`.`createdDate`,'%d %b %Y') AS `createdDate`,`comment`.`commentID` AS `commentID`,15 AS `15`,`tsk`.`taskID` AS `taskID` from ((`comment` join `task` `tsk` on((`comment`.`parentID` = `tsk`.`taskID`))) join `lookup` `lk` on(((`lk`.`lookupSubTypeID` = `comment`.`commentTypeID`) and (`lk`.`lookupTypeID` = 6)))) order by 4 limit 40;


-- Dumping structure for view simpricity.vw_select_task_index_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_task_index_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_task_index_sidebar` AS select 'New tasks' AS `taskDescription`,'' AS `column2`,'' AS `id`,0 AS `column4`,'' AS `userID` union select distinct `task`.`taskDescription` AS `taskDescription`,date_format(`task`.`createdDate`,'%d %b %Y') AS `createdDate`,`task`.`taskID` AS `taskID`,3 AS `3`,`upr`.`userID` AS `userID` from ((`task` join `tasklist` `tkl` on((`task`.`taskListID` = `tkl`.`taskListID`))) join `userproject` `upr` on((`upr`.`projectID` = `tkl`.`projectID`))) where (`task`.`createdDate` > `fn_past_date`(-(10))) union select 'Changed tasks' AS `Changed tasks`,'' AS `column2`,'' AS `id`,5 AS `5`,'' AS `userID` union select `task`.`taskDescription` AS `taskDescription`,date_format(`task`.`updatedDate`,'%d %b %Y') AS `updatedDate`,`task`.`taskID` AS `taskID`,7 AS `7`,`upr`.`userID` AS `userID` from ((`task` join `tasklist` `tkl` on((`task`.`taskListID` = `tkl`.`taskListID`))) join `userproject` `upr` on((`upr`.`projectID` = `tkl`.`projectID`))) where (`task`.`updatedDate` > `fn_past_date`(-(10))) union select 'New comments' AS `New comments`,'' AS `column2`,'' AS `id`,9 AS `9`,'' AS `userID` union select 'Comment' AS `Comment`,concat(`users`.`first_name`,' ',`users`.`last_name`) AS `createdBy`,`task`.`taskID` AS `taskID`,11 AS `11`,`upr`.`userID` AS `userID` from ((((`task` join `tasklist` `tkl` on((`task`.`taskListID` = `tkl`.`taskListID`))) join `userproject` `upr` on((`tkl`.`projectID` = `upr`.`projectID`))) join `comment` on((`comment`.`parentID` = `task`.`taskID`))) join `users` on((`users`.`id` = `upr`.`userID`))) where (`comment`.`createdDate` > `fn_past_date`(-(10))) order by 4,1,2 limit 40;


-- Dumping structure for view simpricity.vw_select_time_detail_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_time_detail_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_time_detail_sidebar` AS select 'Created:' AS `description`,date_format(`usr`.`created_on`,'%d %b %Y') AS `column2`,'' AS `id`,0 AS `column4`,`usr`.`id` AS `userID` from `users` `usr` union select 'Last login:' AS `description`,date_format(from_unixtime(`usr`.`last_login`),'%d %b %Y') AS `column2`,'' AS `id`,3 AS `column4`,`usr`.`id` AS `userID` from `users` `usr` order by 4 limit 40;


-- Dumping structure for view simpricity.vw_select_time_index_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_time_index_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_time_index_sidebar` AS select 'My time by project' AS `projectName`,'' AS `column2`,'' AS `id`,0 AS `column4`,'' AS `userID` union select `prj`.`projectName` AS `projectName`,sum(`tme`.`hours`) AS `sum(tme.hours)`,`prj`.`projectID` AS `projectID`,3 AS `column4`,`uorg2`.`userID` AS `userID` from (((((`time` `tme` join `userorganisation` `uorg` on((`tme`.`userID` = `uorg`.`userID`))) join `task` `tsk` on((`tsk`.`taskID` = `tme`.`taskID`))) join `tasklist` `tkl` on((`tkl`.`taskListID` = `tsk`.`taskListID`))) join `project` `prj` on((`prj`.`projectID` = `tkl`.`projectID`))) join `userorganisation` `uorg2` on((`uorg`.`organisationID` = `uorg2`.`organisationID`))) where (`tme`.`createdDate` > `fn_past_date`(-(90))) group by `prj`.`projectID`,`prj`.`projectName`,3 union select 'My time this week' AS `My time this week`,'' AS `column2`,'' AS `id`,5 AS `5`,'' AS `userID` union select `prj`.`projectName` AS `projectName`,sum(`tme`.`hours`) AS `sum(tme.hours)`,`prj`.`projectID` AS `projectID`,3 AS `column4`,`uorg2`.`userID` AS `userID` from (((((`time` `tme` join `userorganisation` `uorg` on((`tme`.`userID` = `uorg`.`userID`))) join `task` `tsk` on((`tsk`.`taskID` = `tme`.`taskID`))) join `tasklist` `tkl` on((`tkl`.`taskListID` = `tsk`.`taskListID`))) join `project` `prj` on((`prj`.`projectID` = `tkl`.`projectID`))) join `userorganisation` `uorg2` on((`uorg`.`organisationID` = `uorg2`.`organisationID`))) where (`tme`.`createdDate` > `fn_past_date`(-(5))) group by `prj`.`projectID`,`prj`.`projectName`,3 union select 'My time this month' AS `My time this month`,'' AS `column2`,'' AS `id`,9 AS `9`,'' AS `userID` union select `prj`.`projectName` AS `projectName`,sum(`tme`.`hours`) AS `sum(tme.hours)`,`prj`.`projectID` AS `projectID`,3 AS `column4`,`uorg2`.`userID` AS `userID` from (((((`time` `tme` join `userorganisation` `uorg` on((`tme`.`userID` = `uorg`.`userID`))) join `task` `tsk` on((`tsk`.`taskID` = `tme`.`taskID`))) join `tasklist` `tkl` on((`tkl`.`taskListID` = `tsk`.`taskListID`))) join `project` `prj` on((`prj`.`projectID` = `tkl`.`projectID`))) join `userorganisation` `uorg2` on((`uorg`.`organisationID` = `uorg2`.`organisationID`))) where (`tme`.`createdDate` > `fn_past_date`(-(30))) group by `prj`.`projectID`,`prj`.`projectName`,3 order by 4,1,2 limit 40;


-- Dumping structure for view simpricity.vw_select_user_detail_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_user_detail_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_user_detail_sidebar` AS select 'Created:' AS `description`,date_format(from_unixtime(`usr`.`created_on`),'%d %b %Y') AS `column2`,'' AS `id`,0 AS `column4`,`usr`.`id` AS `userID` from `users` `usr` union select 'Last login:' AS `description`,date_format(from_unixtime(`usr`.`last_login`),'%d %b %Y') AS `column2`,'' AS `id`,3 AS `column4`,`usr`.`id` AS `userID` from `users` `usr` order by 4 limit 40;


-- Dumping structure for view simpricity.vw_select_user_index_sidebar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `vw_select_user_index_sidebar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_select_user_index_sidebar` AS select 'New users' AS `userName`,'' AS `column2`,'' AS `id`,0 AS `column4`,'' AS `userID` union select distinct `usr`.`username` AS `username`,date_format(from_unixtime(`usr`.`created_on`),'%d %b %Y') AS `created_on`,`usr`.`id` AS `id`,3 AS `3`,`uorg2`.`userID` AS `userID` from ((`users` `usr` join `userorganisation` `uorg` on((`usr`.`id` = `uorg`.`userID`))) join `userorganisation` `uorg2` on((`uorg`.`organisationID` = `uorg2`.`organisationID`))) where (`usr`.`created_on` > `fn_past_date`(-(90))) union select 'Changed users' AS `Changed users`,'' AS `column2`,'' AS `id`,5 AS `5`,'' AS `userID` union select distinct `usr`.`username` AS `username`,date_format(from_unixtime(`usr`.`created_on`),'%d %b %Y') AS `created_on`,`usr`.`id` AS `id`,3 AS `3`,`uorg`.`userID` AS `userID` from ((`users` `usr` join `userorganisation` `uorg` on((`usr`.`id` = `uorg`.`userID`))) join `userorganisation` `uorg2` on((`uorg`.`organisationID` = `uorg2`.`organisationID`))) where (`usr`.`last_login` > `fn_past_date`(-(90))) order by 4,1,2 limit 40;


-- Dumping structure for view simpricity.v_account_detail
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_account_detail`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_account_detail` AS select `acc`.`accountID` AS `accountid`,`acc`.`accountName` AS `accountName`,`acc`.`authenticationID` AS `authenticationID`,`cli`.`clientID` AS `clientID` from (`account` `acc` join `client` `cli` on((`acc`.`accountID` = `cli`.`accountID`)));


-- Dumping structure for view simpricity.v_actual_problem_links
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_actual_problem_links`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_actual_problem_links` AS select `problemlink`.`problemID` AS `problemID`,`problemlink`.`problemLinkID` AS `problemLinkID`,`problemlink`.`problemLinkType` AS `problemLinkType`,`problemlink`.`createdDate` AS `createdDate`,`problemlink`.`createdBy` AS `createdBy`,`problemlink`.`deletedDate` AS `deletedDate`,`problemlink`.`deletedBy` AS `deletedBy`,`problem`.`problemHeader` AS `problemLinkName` from (`problemlink` join `problem` on((`problemlink`.`problemLinkID` = `problem`.`problemID`))) where (`problemlink`.`problemLinkType` = 2) union select `problemlink`.`problemID` AS `problemID`,`problemlink`.`problemLinkID` AS `problemLinkID`,`problemlink`.`problemLinkType` AS `problemLinkType`,`problemlink`.`createdDate` AS `createdDate`,`problemlink`.`createdBy` AS `createdBy`,`problemlink`.`deletedDate` AS `deletedDate`,`problemlink`.`deletedBy` AS `deletedBy`,`project`.`projectName` AS `problemLinkName` from (`problemlink` join `project` on((`problemlink`.`problemLinkID` = `project`.`projectID`))) where (`problemlink`.`problemLinkType` = 1);


-- Dumping structure for view simpricity.v_client_admin_group
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_client_admin_group`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_client_admin_group` AS select `groups`.`id` AS `groupID` from `groups` where (`groups`.`name` = 'clientAdmin');


-- Dumping structure for view simpricity.v_client_users
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_client_users`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_client_users` AS select `org`.`clientID` AS `clientID`,`org`.`organisationID` AS `organisationID`,`org`.`organisationName` AS `organisationName`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name`,`usr`.`id` AS `userID` from ((`userorganisation` `uorg` join `users` `usr` on((`uorg`.`organisationID` = `usr`.`company`))) join `organisation` `org` on((`org`.`organisationID` = `uorg`.`organisationID`))) where (isnull(`uorg`.`deletedDate`) and isnull(`org`.`deletedDate`));


-- Dumping structure for view simpricity.v_comments_parent
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_comments_parent`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_comments_parent` AS select `usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name`,`com`.`commentID` AS `commentID`,`com`.`parentID` AS `parentID`,`com`.`parentTypeID` AS `parentTypeID`,`com`.`commentTypeID` AS `commentTypeID`,`com`.`commentText` AS `commentText`,date_format(`com`.`createdDate`,'%a %D %M %Y %l:%i %p') AS `createdDate`,`com`.`createdBy` AS `createdBy`,`lk`.`lookupValueChar` AS `lookupValueChar`,`doc`.`documentFileName` AS `documentFileName`,`doc`.`documentName` AS `documentName` from (((`comment` `com` join `lookup` `lk` on((`lk`.`lookupValueNum` = `com`.`commentTypeID`))) join `users` `usr` on((`com`.`createdBy` = `usr`.`id`))) left join `document` `doc` on(((`doc`.`documentParentID` = `com`.`commentID`) and (`doc`.`documentTypeID` = 1)))) where (`lk`.`lookupTypeID` = 6);


-- Dumping structure for view simpricity.v_email_queue
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_email_queue`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_email_queue` AS select `bf_email_queue`.`to_email` AS `to_email`,`bf_email_queue`.`subject` AS `subject`,`bf_email_queue`.`message` AS `message`,`bf_email_queue`.`date_published` AS `date_published`,`bf_email_queue`.`date_sent` AS `date_sent`,`bf_email_queue`.`success` AS `success` from `bf_email_queue` where (isnull(`bf_email_queue`.`date_sent`) or (`bf_email_queue`.`success` = 0));


-- Dumping structure for view simpricity.v_importances
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_importances`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_importances` AS select `lookup`.`lookupValueNum` AS `importanceID`,`lookup`.`lookupValueChar` AS `importanceName` from `lookup` where ((`lookup`.`lookupTypeID` = 19) and isnull(`lookup`.`deletedDate`));


-- Dumping structure for view simpricity.v_invoice_detail
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_invoice_detail`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_invoice_detail` AS select `inv`.`invoiceID` AS `invoiceID`,`inv`.`userID` AS `userID`,`inv`.`statusID` AS `statusID`,`inv`.`supersededBy` AS `supersededBy`,`inv`.`createdDate` AS `createdDate`,`inv`.`createdBy` AS `createdBy`,`inv`.`description` AS `description`,`inv`.`comments` AS `comments`,`invl`.`lineNo` AS `lineNo`,`invl`.`taskID` AS `taskID`,`invl`.`itemDescription` AS `itemDescription`,`invl`.`tax1Rate` AS `tax1Rate`,`invl`.`tax2Rate` AS `tax2Rate`,`invl`.`tax3Rate` AS `tax3Rate`,`invl`.`hourlyRate` AS `hourlyRate`,`invl`.`noHours` AS `noHours`,`invl`.`agreedRate` AS `agreedRate`,`invl`.`tax1` AS `tax1`,`invl`.`tax2` AS `tax2`,`invl`.`tax3` AS `tax3`,`invl`.`grossTotal` AS `grossTotal`,`invl`.`netTotal` AS `netTotal` from (`invoice` `inv` join `invoiceline` `invl` on((`inv`.`invoiceID` = `invl`.`invoiceID`)));


-- Dumping structure for view simpricity.v_lookups_by_type
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_lookups_by_type`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_lookups_by_type` AS select `lookup`.`clientID` AS `clientID`,`lookup`.`lookupTypeID` AS `lookupTypeID`,`lookup`.`lookupSubTypeID` AS `lookupSubTypeID`,`lookup`.`lookupOrder` AS `lookupOrder`,`lookup`.`lookupValueNum` AS `lookupValueNum`,`lookup`.`lookupValueChar` AS `lookupValueChar`,`lookup`.`lookupDescription` AS `lookupDescription`,`lookup`.`createdDate` AS `createdDate`,`lookup`.`createdBy` AS `createdBy`,`lookup`.`updatedDate` AS `updatedDate`,`lookup`.`updatedBy` AS `updatedBy`,`lookup`.`deletedDate` AS `deletedDate`,`lookup`.`deletedBy` AS `deletedBy` from `lookup` where isnull(`lookup`.`deletedDate`);


-- Dumping structure for view simpricity.v_my_assignedprojects
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_assignedprojects`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_assignedprojects` AS select `pr`.`projectID` AS `projectID`,`pr`.`projectName` AS `projectName`,`pr`.`projectDescription` AS `projectDescription`,`pr`.`deletedDate` AS `deletedDate`,`up`.`userID` AS `userID`,`pr`.`updatedDate` AS `updatedDate` from (`project` `pr` join `userproject` `up` on((`pr`.`projectID` = `up`.`projectID`)));


-- Dumping structure for view simpricity.v_my_attention_required
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_attention_required`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_attention_required` AS select distinct 'Task' AS `type`,2 AS `ordercol`,`pr`.`projectName` AS `projectName`,`pr`.`projectID` AS `projectID`,`tk`.`taskDescription` AS `taskDescription`,`tk`.`taskID` AS `itemID`,`tk`.`assignedTo` AS `assignedTo`,`pr`.`organisationID` AS `organisationID`,`tk`.`deletedDate` AS `deletedDate`,`upr`.`userID` AS `userID` from (((`project` `pr` join `tasklist` `tl` on((`pr`.`projectID` = `tl`.`projectID`))) join `task` `tk` on((`tl`.`taskListID` = `tk`.`taskListID`))) join `userproject` `upr` on((`upr`.`projectID` = `pr`.`projectID`))) where ((`tk`.`taskPriorityID` = 2) and isnull(`tk`.`deletedDate`)) union select distinct 'Problem' AS `type`,2 AS `ordercol`,`prb`.`problemHeader` AS `problemHeader`,`prb`.`problemID` AS `problemID`,NULL AS `taskDescription`,`prb`.`problemID` AS `itemID`,`prb`.`assignedTo` AS `assignedTo`,`prb`.`organisationID` AS `organisationID`,`prb`.`deletedDate` AS `deletedDate`,NULL AS `userID` from `problem` `prb` where ((`prb`.`problemPriorityID` = 2) and isnull(`prb`.`deletedDate`));


-- Dumping structure for view simpricity.v_my_client
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_client`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_client` AS select `cl`.`clientID` AS `clientID`,`usr`.`id` AS `user_id`,`org`.`deletedDate` AS `deletedDate` from ((`client` `cl` join `organisation` `org` on((`cl`.`clientID` = `org`.`clientID`))) join `users` `usr` on((`org`.`organisationID` = `usr`.`company`)));


-- Dumping structure for view simpricity.v_my_critical_work
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_critical_work`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_critical_work` AS select distinct 'Task' AS `type`,1 AS `ordercol`,`pr`.`projectName` AS `projectName`,`pr`.`projectID` AS `projectID`,`tk`.`taskDescription` AS `taskDescription`,`tk`.`taskID` AS `itemID`,`tk`.`assignedTo` AS `assignedTo`,`pr`.`organisationID` AS `organisationID`,`tk`.`deletedDate` AS `deletedDate`,`pr`.`projectID` AS `id` from (((`project` `pr` join `tasklist` `tl` on((`pr`.`projectID` = `tl`.`projectID`))) join `task` `tk` on((`tl`.`taskListID` = `tk`.`taskListID`))) join `userproject` `upr` on((`upr`.`projectID` = `pr`.`projectID`))) where ((`tk`.`taskPriorityID` = 1) and (`tk`.`taskStatusID` in (1,2,3,4,5,6,19)) and isnull(`tk`.`deletedDate`)) union select distinct 'Problem' AS `type`,1 AS `ordercol`,`prb`.`problemHeader` AS `problemHeader`,`prb`.`problemID` AS `problemID`,`prb`.`problemDescription` AS `problemDescription`,`prb`.`problemID` AS `itemID`,`prb`.`assignedTo` AS `assignedTo`,`prb`.`organisationID` AS `organisationID`,`prb`.`deletedDate` AS `deletedDate`,`prb`.`problemID` AS `id` from `problem` `prb` where ((`prb`.`problemPriorityID` = 1) and isnull(`prb`.`deletedDate`));


-- Dumping structure for view simpricity.v_my_important_work
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_important_work`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_important_work` AS select distinct `pr`.`projectName` AS `projectName`,`pr`.`projectID` AS `projectID`,`tk`.`taskDescription` AS `taskDescription`,`tk`.`taskID` AS `taskID`,`tk`.`assignedTo` AS `assignedTo`,`pr`.`organisationID` AS `organisationID`,`tk`.`deletedDate` AS `deletedDate`,`upr`.`userID` AS `userID` from (((`project` `pr` join `tasklist` `tl` on((`pr`.`projectID` = `tl`.`projectID`))) join `task` `tk` on((`tl`.`taskListID` = `tk`.`taskListID`))) join `userproject` `upr` on((`upr`.`projectID` = `pr`.`projectID`))) where (`tk`.`taskPriorityID` = 1) union select distinct `prb`.`problemHeader` AS `problemHeader`,`prb`.`problemID` AS `problemID`,`prb`.`problemDescription` AS `problemDescription`,NULL AS `taskID`,`prb`.`assignedTo` AS `assignedTo`,`prb`.`organisationID` AS `organisationID`,`prb`.`deletedDate` AS `deletedDate`,NULL AS `userID` from `problem` `prb` where (`prb`.`problemPriorityID` = 1);


-- Dumping structure for view simpricity.v_my_invoices
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_invoices`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_invoices` AS select `inv`.`invoiceID` AS `invoiceID`,`inv`.`statusID` AS `statusID`,`lk`.`lookupValueChar` AS `lookupValueChar`,`inv`.`createdDate` AS `createdDate`,sum(`invl`.`noHours`) AS `noHours`,sum(`invl`.`grossTotal`) AS `grossTotal`,sum(`invl`.`netTotal`) AS `netTotal`,`inv`.`userID` AS `userID`,`inv`.`deletedDate` AS `deletedDate`,`inv`.`invoiceID` AS `id` from ((`invoice` `inv` join `invoiceline` `invl` on((`inv`.`invoiceID` = `invl`.`invoiceID`))) left join `lookup` `lk` on((`lk`.`lookupSubTypeID` = `inv`.`statusID`))) where (`lk`.`lookupTypeID` = 18) group by `inv`.`invoiceID`;


-- Dumping structure for view simpricity.v_my_invoice_times
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_invoice_times`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_invoice_times` AS select `pr`.`projectName` AS `projectName`,`tkl`.`taskListName` AS `taskListName`,`tsk`.`taskDescription` AS `taskDescription`,date_format(`tm`.`timeDay`,'%e %b %Y') AS `timeDay`,`tm`.`hours` AS `hours`,`tm`.`userID` AS `userID`,`tm`.`timeID` AS `timeID`,`tm`.`deletedDate` AS `deletedDate` from (((`time` `tm` join `task` `tsk` on((`tm`.`taskID` = `tsk`.`taskID`))) join `tasklist` `tkl` on((`tkl`.`taskListID` = `tsk`.`taskListID`))) join `project` `pr` on((`pr`.`projectID` = `tkl`.`projectID`)));


-- Dumping structure for view simpricity.v_my_items
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_items`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_items` AS select `upr`.`projectID` AS `projectID`,`upr`.`userID` AS `userID` from `userproject` `upr` union select `uor`.`organisationID` AS `organisationID`,`uor`.`userID` AS `userID` from `userorganisation` `uor` union select `tsk`.`taskID` AS `taskID`,`tsk`.`assignedTo` AS `assignedTo` from `task` `tsk` union select `usr`.`company` AS `mainOrganisationID`,`usr`.`id` AS `user_id` from `users` `usr`;


-- Dumping structure for view simpricity.v_my_organisations
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_organisations`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_organisations` AS select `cl`.`clientID` AS `clientID`,`org`.`organisationID` AS `organisationID`,`org`.`organisationName` AS `organisationName`,`uo`.`userID` AS `userID`,`org`.`deletedDate` AS `deletedDate`,`cl`.`clientID` AS `id` from ((`organisation` `org` left join `userorganisation` `uo` on((`org`.`organisationID` = `uo`.`organisationID`))) join `client` `cl` on((`cl`.`clientID` = `org`.`clientID`))) union select `cl`.`clientID` AS `clientID`,`org`.`organisationID` AS `organisationID`,`org`.`organisationName` AS `organisationName`,`usr`.`id` AS `userID`,`org`.`deletedDate` AS `deletedDate`,`cl`.`clientID` AS `id` from ((`organisation` `org` left join `users` `usr` on((`org`.`organisationID` = `usr`.`company`))) join `client` `cl` on((`cl`.`clientID` = `org`.`clientID`)));


-- Dumping structure for view simpricity.v_my_organisation_events
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_organisation_events`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_organisation_events` AS select `org`.`organisationName` AS `organisationName`,`org`.`createdDate` AS `createdDate`,`cl`.`userID` AS `userID`,`org`.`organisationID` AS `organisationID`,3 AS `type` from (`organisation` `org` join `client` `cl` on((`org`.`clientID` = `cl`.`clientID`))) where (`org`.`createdDate` > `fn_past_date`(-(10))) union select `org`.`organisationName` AS `organisationName`,`org`.`updatedDate` AS `updatedDate`,`cl`.`userID` AS `userID`,`org`.`organisationID` AS `organisationID`,5 AS `type` from (`organisation` `org` join `client` `cl` on((`org`.`clientID` = `cl`.`clientID`))) where (`org`.`updatedDate` > `fn_past_date`(-(10))) union select `org`.`organisationName` AS `organisationName`,`org`.`createdDate` AS `createdDate`,`cl`.`userID` AS `userID`,`org`.`organisationID` AS `organisationID`,7 AS `type` from (`organisation` `org` join `client` `cl` on((`org`.`clientID` = `cl`.`clientID`))) where (`org`.`updatedDate` > `fn_past_date`(-(10)));


-- Dumping structure for view simpricity.v_my_org_tasks
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_org_tasks`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_org_tasks` AS select distinct `upr`.`userID` AS `userID`,concat(`prj`.`projectName`,' - ',`tsk`.`taskDescription`) AS `taskDescription`,`tsk`.`taskID` AS `taskID`,`tsk`.`deletedDate` AS `deletedDate` from (((`task` `tsk` join `tasklist` `tkl`) join `project` `prj`) join `userproject` `upr`) where ((`upr`.`projectID` = `prj`.`projectID`) and (`prj`.`projectID` = `tkl`.`projectID`) and (`tsk`.`taskListID` = `tkl`.`taskListID`));


-- Dumping structure for view simpricity.v_my_priorities
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_priorities`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_priorities` AS select `lookup`.`clientID` AS `clientID`,`lookup`.`lookupDescription` AS `lookupDescription`,`lookup`.`lookupValueNum` AS `lookupValueNum`,`lookup`.`lookupValueChar` AS `lookupValueChar`,`lookup`.`lookupOrder` AS `lookupOrder` from `lookup` where (`lookup`.`lookupTypeID` = 4);


-- Dumping structure for view simpricity.v_my_problems
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_problems`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_problems` AS select `pro`.`problemID` AS `problemID`,`pro`.`organisationID` AS `organisationID`,`lookty`.`lookupDescription` AS `problemType`,`pro`.`problemHeader` AS `problemHeader`,`pro`.`assignedTo` AS `assignedTo`,`looksc`.`lookupDescription` AS `problemScope`,`lookstat`.`lookupDescription` AS `problemStatus`,`lookpr`.`lookupDescription` AS `problemPriority`,`looksc`.`lookupValueNum` AS `problemScopeID`,`pro`.`createdBy` AS `createdBy`,`pro`.`problemID` AS `id` from ((((`problem` `pro` left join `lookup` `lookty` on((`pro`.`problemTypeID` = `lookty`.`lookupSubTypeID`))) left join `lookup` `looksc` on((`pro`.`scope` = `looksc`.`lookupSubTypeID`))) left join `lookup` `lookstat` on((`pro`.`problemStatusID` = `lookstat`.`lookupSubTypeID`))) left join `lookup` `lookpr` on((`pro`.`problemPriorityID` = `lookpr`.`lookupSubTypeID`))) where ((`lookty`.`lookupTypeID` = 8) and (`looksc`.`lookupTypeID` = 10) and (`lookstat`.`lookupTypeID` = 11) and (`lookpr`.`lookupTypeID` = 12) and isnull(`pro`.`deletedBy`));


-- Dumping structure for view simpricity.v_my_problem_priorities
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_problem_priorities`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_problem_priorities` AS select `lookup`.`clientID` AS `clientID`,`lookup`.`lookupTypeID` AS `lookupTypeID`,`lookup`.`lookupSubTypeID` AS `lookupSubTypeID`,`lookup`.`lookupOrder` AS `lookupOrder`,`lookup`.`lookupValueNum` AS `lookupValueNum`,`lookup`.`lookupValueChar` AS `lookupValueChar`,`lookup`.`lookupDescription` AS `lookupDescription`,`lookup`.`createdDate` AS `createdDate`,`lookup`.`createdBy` AS `createdBy`,`lookup`.`updatedDate` AS `updatedDate`,`lookup`.`updatedBy` AS `updatedBy`,`lookup`.`deletedDate` AS `deletedDate`,`lookup`.`deletedBy` AS `deletedBy` from `lookup` where (`lookup`.`lookupTypeID` = 12);


-- Dumping structure for view simpricity.v_my_problem_scope
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_problem_scope`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_problem_scope` AS select `lookup`.`clientID` AS `clientID`,`lookup`.`lookupTypeID` AS `lookupTypeID`,`lookup`.`lookupSubTypeID` AS `lookupSubTypeID`,`lookup`.`lookupOrder` AS `lookupOrder`,`lookup`.`lookupValueNum` AS `lookupValueNum`,`lookup`.`lookupValueChar` AS `lookupValueChar`,`lookup`.`lookupDescription` AS `lookupDescription`,`lookup`.`createdDate` AS `createdDate`,`lookup`.`createdBy` AS `createdBy`,`lookup`.`updatedDate` AS `updatedDate`,`lookup`.`updatedBy` AS `updatedBy`,`lookup`.`deletedDate` AS `deletedDate`,`lookup`.`deletedBy` AS `deletedBy` from `lookup` where (`lookup`.`lookupTypeID` = 10);


-- Dumping structure for view simpricity.v_my_problem_statuses
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_problem_statuses`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_problem_statuses` AS select `lookup`.`clientID` AS `clientID`,`lookup`.`lookupTypeID` AS `lookupTypeID`,`lookup`.`lookupSubTypeID` AS `lookupSubTypeID`,`lookup`.`lookupOrder` AS `lookupOrder`,`lookup`.`lookupValueNum` AS `lookupValueNum`,`lookup`.`lookupValueChar` AS `lookupValueChar`,`lookup`.`lookupDescription` AS `lookupDescription`,`lookup`.`createdDate` AS `createdDate`,`lookup`.`createdBy` AS `createdBy`,`lookup`.`updatedDate` AS `updatedDate`,`lookup`.`updatedBy` AS `updatedBy`,`lookup`.`deletedDate` AS `deletedDate`,`lookup`.`deletedBy` AS `deletedBy` from `lookup` where (`lookup`.`lookupTypeID` = 11);


-- Dumping structure for view simpricity.v_my_projects
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_projects`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_projects` AS select `project`.`projectID` AS `projectID`,`project`.`organisationID` AS `organisationID`,`project`.`projectName` AS `projectName`,`project`.`projectDescription` AS `projectDescription`,`project`.`createdDate` AS `createdDate`,`project`.`createdBy` AS `createdBy`,`project`.`updatedDate` AS `updatedDate`,`project`.`updatedBy` AS `updatedBy`,`project`.`deletedDate` AS `deletedDate`,`project`.`deletedBy` AS `deletedBy`,`userproject`.`userID` AS `userID`,`organisation`.`organisationName` AS `organisationName`,`project`.`projectID` AS `id` from ((`project` join `userproject` on((`project`.`projectID` = `userproject`.`projectID`))) join `organisation` on((`project`.`organisationID` = `organisation`.`organisationID`)));


-- Dumping structure for view simpricity.v_my_reports
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_reports`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_reports` AS select `lk`.`lookupValueNum` AS `lookupValueNum`,`lk`.`lookupValueChar` AS `lookupValueChar`,`usrr`.`userID` AS `userID`,`usrr`.`deletedDate` AS `deletedDate` from (`userreport` `usrr` join `lookup` `lk` on((`usrr`.`reportID` = `lk`.`lookupValueNum`))) where (isnull(`lk`.`deletedDate`) and (`lk`.`lookupTypeID` = 15));


-- Dumping structure for view simpricity.v_my_statuses
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_statuses`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_statuses` AS select `lookup`.`clientID` AS `clientID`,`lookup`.`lookupDescription` AS `lookupDescription`,`lookup`.`lookupValueNum` AS `lookupValueNum`,`lookup`.`lookupValueChar` AS `lookupValueChar` from `lookup` where (`lookup`.`lookupTypeID` = 3);


-- Dumping structure for view simpricity.v_my_tasks
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_tasks`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_tasks` AS select `project`.`projectID` AS `projectID`,`project`.`projectName` AS `projectName`,`tasklist`.`taskListID` AS `taskListID`,`tasklist`.`taskListName` AS `taskListName`,`task`.`taskID` AS `taskID`,`task`.`taskDescription` AS `taskDescription`,`task`.`assignedTo` AS `assignedTo`,`task`.`deletedDate` AS `deletedDate`,`task`.`taskID` AS `id` from ((`task` join `tasklist` on((`task`.`taskListID` = `tasklist`.`taskListID`))) join `project` on((`project`.`projectID` = `tasklist`.`projectID`)));


-- Dumping structure for view simpricity.v_my_tasktypes
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_tasktypes`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_tasktypes` AS select `lookup`.`clientID` AS `clientID`,`lookup`.`lookupDescription` AS `lookupDescription`,`lookup`.`lookupValueNum` AS `lookupValueNum`,`lookup`.`lookupValueChar` AS `lookupValueChar` from `lookup` where (`lookup`.`lookupTypeID` = 5);


-- Dumping structure for view simpricity.v_my_time
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_time`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_time` AS select `time`.`timeID` AS `timeID`,date_format(`time`.`timeDay`,'%Y %b %d') AS `timeDay`,`time`.`timeDay` AS `timeDayraw`,`time`.`hours` AS `hours`,`time`.`taskID` AS `taskID`,`time`.`timeTypeID` AS `timeTypeID`,`time`.`userID` AS `userID`,`users`.`first_name` AS `first_name`,`users`.`last_name` AS `last_name`,`time`.`deletedDate` AS `deletedDate`,`time`.`comments` AS `comments`,`task`.`taskDescription` AS `taskDescription`,`lookup`.`lookupValueChar` AS `lookupValueChar`,`time`.`timeID` AS `id` from (((`time` join `users` on((`time`.`userID` = `users`.`id`))) join `task` on((`time`.`taskID` = `task`.`taskID`))) join `lookup` on((`time`.`timeTypeID` = `lookup`.`lookupValueNum`))) where (`lookup`.`lookupTypeID` = 13);


-- Dumping structure for view simpricity.v_my_timesheet
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_timesheet`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_timesheet` AS select `time`.`timeID` AS `timeID`,`time`.`timeDay` AS `timeDay`,date_format(`time`.`timeDay`,'%e %b %Y') AS `timeDayF`,`task`.`taskDescription` AS `taskDescription`,sum(`time`.`hours`) AS `hours`,`users`.`id` AS `userID`,`time`.`timeTypeID` AS `timetypeID`,`lookup`.`lookupTypeID` AS `lookupTypeID` from (((`time` join `users` on((`time`.`userID` = `users`.`id`))) join `task` on((`time`.`taskID` = `task`.`taskID`))) join `lookup` on(((`time`.`timeTypeID` = `lookup`.`lookupValueNum`) and (`lookup`.`lookupTypeID` = 13)))) group by `users`.`id`,date_format(`time`.`timeDay`,'%e %b %Y'),`task`.`taskDescription` with rollup;


-- Dumping structure for view simpricity.v_my_users
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_my_users`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_my_users` AS select distinct `usr`.`id` AS `user_id`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name`,`org`.`organisationID` AS `organisationID`,`org`.`organisationName` AS `organisationName`,`usr`.`active` AS `active`,concat(`usr`.`first_name`,' ',`usr`.`last_name`) AS `name`,`uo`.`userID` AS `userID`,if((`usr`.`active` = 1),'Yes','No') AS `activeDesc`,`usr`.`id` AS `id` from ((`organisation` `org` join `userorganisation` `uo` on((`org`.`organisationID` = `uo`.`organisationID`))) join `users` `usr` on((`org`.`organisationID` = `usr`.`company`))) union select distinct `usr`.`id` AS `user_id`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name`,`org`.`organisationID` AS `organisationID`,`org`.`organisationName` AS `organisationName`,`usr`.`active` AS `active`,concat(`usr`.`first_name`,' ',`usr`.`last_name`) AS `name`,`usr`.`id` AS `userID`,if((`usr`.`active` = 1),'Yes','No') AS `activeDesc`,`usr`.`id` AS `id` from (`organisation` `org` join `users` `usr` on((`org`.`organisationID` = `usr`.`company`)));


-- Dumping structure for view simpricity.v_new_user_emails
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_new_user_emails`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_new_user_emails` AS select distinct `us`.`email` AS `email`,`us`.`first_name` AS `first_name`,`us`.`last_name` AS `last_name`,`us`.`id` AS `id` from `users` `us`;


-- Dumping structure for view simpricity.v_organisations
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_organisations`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_organisations` AS select `org`.`organisationID` AS `organisationID`,`org`.`clientID` AS `clientID`,`org`.`organisationName` AS `organisationName`,`org`.`createdDate` AS `createdDate`,`org`.`createdBy` AS `createdBy`,`org`.`updatedDate` AS `updatedDate`,`org`.`updatedBy` AS `updatedBy`,`org`.`deletedDate` AS `deletedDate`,`org`.`deletedBy` AS `deletedBy`,`usr`.`company` AS `userID`,`org`.`organisationID` AS `id` from (`organisation` `org` join `users` `usr`) where (`org`.`organisationID` = `usr`.`company`) union select `org`.`organisationID` AS `organisationID`,`org`.`clientID` AS `clientID`,`org`.`organisationName` AS `organisationName`,`org`.`createdDate` AS `createdDate`,`org`.`createdBy` AS `createdBy`,`org`.`updatedDate` AS `updatedDate`,`org`.`updatedBy` AS `updatedBy`,`org`.`deletedDate` AS `deletedDate`,`org`.`deletedBy` AS `deletedBy`,`uorg`.`userID` AS `userID`,`org`.`organisationID` AS `id` from (`organisation` `org` join `userorganisation` `uorg`) where (`org`.`organisationID` = `uorg`.`organisationID`);


-- Dumping structure for view simpricity.v_organisation_activity
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_organisation_activity`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_organisation_activity` AS select `usa`.`activityID` AS `activityID`,`usa`.`userID` AS `userID`,`usa`.`activityData` AS `activityData`,`pro`.`organisationID` AS `organisationID` from ((`organisation` `org` join `project` `pro` on((`org`.`organisationID` = `pro`.`organisationID`))) join `useractivity` `usa` on((`usa`.`activityProjectID` = `pro`.`projectID`)));


-- Dumping structure for view simpricity.v_organisation_project_managers
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_organisation_project_managers`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_organisation_project_managers` AS select `org`.`organisationID` AS `organisationID`,`org`.`organisationName` AS `organisationName`,`usr`.`id` AS `userID`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name`,`proj`.`projectID` AS `projectID`,`proj`.`projectName` AS `projectName` from (((`userorganisation` `uorg` join `users` `usr` on((`uorg`.`organisationID` = `usr`.`company`))) join `organisation` `org` on((`org`.`organisationID` = `uorg`.`organisationID`))) join `project` `proj` on((`org`.`organisationID` = `proj`.`organisationID`))) where (isnull(`uorg`.`deletedDate`) and isnull(`org`.`deletedDate`));


-- Dumping structure for view simpricity.v_organisation_project_users
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_organisation_project_users`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_organisation_project_users` AS select `org`.`organisationID` AS `organisationID`,`org`.`organisationName` AS `organisationName`,`usr`.`id` AS `userID`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name`,`proj`.`projectID` AS `projectID`,`proj`.`projectName` AS `projectName` from (((`userorganisation` `uorg` join `users` `usr` on((`uorg`.`organisationID` = `usr`.`company`))) join `organisation` `org` on((`org`.`organisationID` = `uorg`.`organisationID`))) join `project` `proj` on((`org`.`organisationID` = `proj`.`organisationID`))) where (isnull(`uorg`.`deletedDate`) and isnull(`org`.`deletedDate`) and (not(`usr`.`id` in (select `upr`.`userID` from `userproject` `upr` where (`upr`.`projectID` = `proj`.`projectID`)))));


-- Dumping structure for view simpricity.v_organisation_users
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_organisation_users`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_organisation_users` AS select `org`.`organisationID` AS `organisationID`,`org`.`organisationName` AS `organisationName`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name` from ((`userorganisation` `uorg` join `users` `usr` on((`uorg`.`organisationID` = `usr`.`company`))) join `organisation` `org` on((`org`.`organisationID` = `uorg`.`organisationID`))) where (isnull(`uorg`.`deletedDate`) and isnull(`org`.`deletedDate`));


-- Dumping structure for view simpricity.v_problems
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_problems`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_problems` AS select `pro`.`clientID` AS `clientID`,`pro`.`problemID` AS `problemID`,`pro`.`organisationID` AS `organisationID`,`lookty`.`lookupDescription` AS `problemType`,`pro`.`problemDescription` AS `problemDescription`,`pro`.`noOfPeopleAffected` AS `noOfPeopleAffected`,`pro`.`scope` AS `scope`,`pro`.`problemHeader` AS `problemHeader`,`pro`.`assignedTo` AS `assignedTo`,`lookpty`.`lookupDescription` AS `lookupDescription`,`looksc`.`lookupDescription` AS `problemScope`,`lookst`.`lookupDescription` AS `problemStatus`,`lookpr`.`lookupDescription` AS `problemPriority`,`looksc`.`lookupValueNum` AS `problemScopeID`,`lookpr`.`lookupValueNum` AS `problemPriorityID`,`lookst`.`lookupValueNum` AS `problemStatusID`,`pro`.`createdBy` AS `createdBy` from (((((`problem` `pro` left join `lookup` `lookty` on(((`pro`.`problemTypeID` = `lookty`.`lookupSubTypeID`) and (`lookty`.`lookupTypeID` = 8)))) left join `lookup` `lookpty` on(((`pro`.`problemTypeID` = `lookpty`.`lookupSubTypeID`) and (`lookpty`.`lookupTypeID` = 9)))) left join `lookup` `looksc` on(((`pro`.`scope` = `looksc`.`lookupSubTypeID`) and (`looksc`.`lookupTypeID` = 10)))) left join `lookup` `lookst` on(((`pro`.`problemStatusID` = `lookst`.`lookupSubTypeID`) and (`lookst`.`lookupTypeID` = 11)))) left join `lookup` `lookpr` on(((`pro`.`problemPriorityID` = `lookpr`.`lookupSubTypeID`) and (`lookpr`.`lookupTypeID` = 12))));


-- Dumping structure for view simpricity.v_problem_activity
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_problem_activity`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_problem_activity` AS select `pra`.`problemID` AS `itemID`,'Update' AS `activity`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name` from (`problem_archive` `pra` join `users` `usr` on((`usr`.`id` = `pra`.`updatedBy`)));


-- Dumping structure for view simpricity.v_problem_assignees
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_problem_assignees`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_problem_assignees` AS select distinct `us`.`first_name` AS `first_name`,`us`.`last_name` AS `last_name`,`uo`.`userID` AS `userid`,`pr`.`problemID` AS `problemID` from ((`userorganisation` `uo` join `users` `us` on((`us`.`id` = `uo`.`userID`))) join `problem` `pr` on((`pr`.`organisationID` = `uo`.`organisationID`)));


-- Dumping structure for view simpricity.v_problem_edit
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_problem_edit`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_problem_edit` AS select `pro`.`clientID` AS `clientID`,`pro`.`problemID` AS `problemID`,`pro`.`organisationID` AS `organisationID`,`pro`.`problemDescription` AS `problemDescription`,`pro`.`noOfPeopleAffected` AS `noOfPeopleAffected`,`pro`.`scope` AS `problemScopeID`,`pro`.`problemSubTypeID` AS `problemSubTypeID`,`pro`.`problemTypeID` AS `problemTypeID`,`pro`.`problemStatusID` AS `problemStatusID`,`pro`.`problemPriorityID` AS `problemPriorityID`,`pro`.`problemHeader` AS `problemHeader`,`pro`.`assignedTo` AS `assignedTo`,`pro`.`createdBy` AS `createdBy` from `problem` `pro`;


-- Dumping structure for view simpricity.v_problem_json
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_problem_json`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_problem_json` AS select concat('[',group_concat(concat('{problemHeader:\'',`problem`.`problemHeader`,'\''),concat(',problemID:\'',`problem`.`problemID`,'\'}') separator ','),']') AS `Name_exp_1` from `problem`;


-- Dumping structure for view simpricity.v_projectgantt_jq
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_projectgantt_jq`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_projectgantt_jq` AS select `prj`.`projectID` AS `projectID`,`prj`.`projectName` AS `projectName`,`prj`.`projectDescription` AS `projectDescription`,`prj`.`updatedDate` AS `updatedDate`,`prj`.`updatedBy` AS `updatedBy`,`tsl`.`taskListID` AS `taskListID`,`tsl`.`taskListName` AS `taskListName`,`tsl`.`taskListDescription` AS `taskListDescription`,`tsk`.`taskID` AS `taskID`,`tsk`.`taskDescription` AS `taskDescription`,ifnull(`tsk`.`taskLinkID`,`tsk`.`taskID`) AS `taskOrderID`,`prj`.`deletedDate` AS `deletedDate`,ifnull((unix_timestamp((`tsk2`.`taskStartDate` + interval `tsk2`.`taskTimeEstimate` day)) * 1000),ifnull((unix_timestamp(`tsk`.`taskStartDate`) * 1000),(unix_timestamp(`tsk`.`createdDate`) * 1000))) AS `taskStartDate`,`tsk`.`assignedTo` AS `assignedTo`,(unix_timestamp((`tsk`.`taskStartDate` + interval `tsk`.`taskTimeEstimate` day)) * 1000) AS `taskEndDate`,`tsk`.`taskTimeEstimate` AS `taskTimeEstimate`,`tsk`.`taskStartDate` AS `taskStartDate_unformatted`,`tsk`.`taskTimeEstimate` AS `time_estimate` from (((`project` `prj` join `tasklist` `tsl` on((`prj`.`projectID` = `tsl`.`projectID`))) join `task` `tsk` on((`tsk`.`taskListID` = `tsl`.`taskListID`))) left join `task` `tsk2` on((`tsk`.`taskID` = `tsk2`.`taskLinkID`))) where isnull(`tsk`.`deletedDate`) order by `prj`.`projectID`,ifnull(`tsk`.`taskLinkID`,`tsk`.`taskID`),`tsk`.`taskListID`,`tsk`.`assignedTo`,`tsk`.`taskStartDate`;


-- Dumping structure for view simpricity.v_project_activity
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_activity`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_activity` AS select `ac`.`activityID` AS `activityID`,`ac`.`userID` AS `userID`,`ac`.`activityTypeID` AS `activityTypeID`,`ac`.`activityData` AS `activityData`,`ac`.`activityProjectID` AS `activityProjectID`,`ac`.`activityTaskListID` AS `activityTaskListID`,`ac`.`activityTaskID` AS `activityTaskID`,`ac`.`activityDate` AS `activityDate`,`tk`.`taskID` AS `taskID`,`tk`.`taskListID` AS `taskListID`,`tk`.`taskTypeID` AS `taskTypeID`,`tk`.`taskDescription` AS `taskDescription`,`tk`.`taskStatusID` AS `taskStatusID`,`tk`.`taskPriorityID` AS `taskPriorityID`,`tk`.`assignedTo` AS `assignedTo`,`tk`.`createdDate` AS `createdDate`,`tk`.`createdBy` AS `createdBy`,`tk`.`updatedDate` AS `updatedDate`,`tk`.`updatedBy` AS `updatedBy`,`tk`.`deletedDate` AS `deletedDate`,`tk`.`deletedBy` AS `deletedBy`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name` from ((`useractivity` `ac` left join `task` `tk` on((`ac`.`activityTaskID` = `tk`.`taskID`))) left join `users` `usr` on((`ac`.`userID` = `usr`.`id`)));


-- Dumping structure for view simpricity.v_project_assignees
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_assignees`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_assignees` AS select distinct `us`.`first_name` AS `first_name`,`us`.`last_name` AS `last_name`,`up`.`userID` AS `userid`,`tk`.`taskID` AS `taskID` from (((`userproject` `up` join `tasklist` `tl` on((`up`.`projectID` = `tl`.`projectID`))) join `task` `tk` on((`tl`.`taskListID` = `tk`.`taskListID`))) join `users` `us` on((`us`.`id` = `up`.`userID`)));


-- Dumping structure for view simpricity.v_project_detail
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_detail`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_detail` AS select distinct `project`.`projectID` AS `projectID`,`project`.`organisationID` AS `organisationID`,`project`.`programmeID` AS `programmeID`,`project`.`clientID` AS `clientID`,`project`.`projectName` AS `projectName`,`project`.`projectDescription` AS `projectDescription`,`project`.`stakeholderID` AS `stakeholderID`,`project`.`projectManagerID` AS `projectManagerID`,`project`.`deliverables` AS `deliverables`,`project`.`budget` AS `budget`,`project`.`importance` AS `importance`,`project`.`createdDate` AS `createdDate`,`project`.`createdBy` AS `createdBy`,`project`.`updatedDate` AS `updatedDate`,`project`.`updatedBy` AS `updatedBy`,`project`.`deletedDate` AS `deletedDate`,`project`.`deletedBy` AS `deletedBy`,`org`.`organisationName` AS `organisationName`,`usr`.`first_name` AS `shFirstName`,`usr`.`last_name` AS `shLastName`,`lk`.`lookupValueChar` AS `importanceDescription`,`usr2`.`first_name` AS `pmFirstName`,`usr2`.`last_name` AS `pmLastName`,`usr3`.`id` AS `userID` from ((((((`project` join `userproject` `upr` on((`project`.`projectID` = `upr`.`projectID`))) join `users` `usr3` on((`upr`.`userID` = `usr3`.`id`))) left join `organisation` `org` on((`project`.`organisationID` = `org`.`organisationID`))) left join `users` `usr` on((`project`.`stakeholderID` = `usr`.`id`))) left join `lookup` `lk` on(((`project`.`importance` = `lk`.`lookupSubTypeID`) and (`lk`.`lookupTypeID` = 19)))) left join `users` `usr2` on((`project`.`projectManagerID` = `usr2`.`id`))) where isnull(`project`.`deletedDate`);


-- Dumping structure for view simpricity.v_project_documents
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_documents`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_documents` AS select `document`.`documentID` AS `documentID`,`document`.`documentTypeID` AS `documentTypeID`,`document`.`documentParentID` AS `documentParentID`,`document`.`documentName` AS `documentName`,`document`.`documentFileName` AS `documentFileName`,`document`.`documentTitle` AS `documentTitle`,`document`.`createdDate` AS `createdDate`,`document`.`createdBy` AS `createdBy`,`document`.`deletedDate` AS `deletedDate`,`document`.`deletedBy` AS `deletedBy` from `document` where ((`document`.`documentTypeID` = 2) and isnull(`document`.`deletedDate`));


-- Dumping structure for view simpricity.v_project_gantt
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_gantt`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_gantt` AS select `prj`.`projectID` AS `projectID`,`prj`.`projectName` AS `projectName`,`prj`.`projectDescription` AS `projectDescription`,`prj`.`updatedDate` AS `updatedDate`,`prj`.`updatedBy` AS `updatedBy`,`tsl`.`taskListID` AS `taskListID`,`tsl`.`taskListName` AS `taskListName`,`tsl`.`taskListDescription` AS `taskListDescription`,`tsk`.`taskID` AS `taskID`,`tsk`.`taskDescription` AS `taskDescription`,`prj`.`deletedDate` AS `deletedDate`,`tsk`.`taskStartDate` AS `taskStartDate`,`tsk`.`assignedTo` AS `assignedTo`,(`tsk`.`taskStartDate` + interval `tsk`.`taskTimeEstimate` day) AS `taskEndDate`,`tsk`.`taskTimeEstimate` AS `taskTimeEstimate` from ((`project` `prj` left join `tasklist` `tsl` on((`prj`.`projectID` = `tsl`.`projectID`))) left join `task` `tsk` on((`tsk`.`taskListID` = `tsl`.`taskListID`))) order by `tsl`.`taskListID`,`tsk`.`assignedTo`,`tsk`.`taskStartDate`;


-- Dumping structure for view simpricity.v_project_opinion
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_opinion`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_opinion` AS select `opinion`.`opinionID` AS `opinionID`,`project`.`projectID` AS `projectID`,`opinion`.`userID` AS `userID`,`opinion`.`itemID` AS `itemID`,`opinion`.`itemType` AS `itemType`,`opinion`.`opinionType` AS `opinionType`,`opinion`.`opinion` AS `opinion` from (`project` join `opinion` on((`project`.`projectID` = `opinion`.`itemID`))) where isnull(`opinion`.`deletedDate`);


-- Dumping structure for view simpricity.v_project_opinion_detail
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_opinion_detail`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_opinion_detail` AS select `opinion`.`opinionID` AS `opinionID`,`project`.`projectID` AS `projectID`,`opinion`.`userID` AS `userID`,`opinion`.`itemID` AS `itemID`,`opinion`.`itemType` AS `itemType`,`opinion`.`opinionType` AS `opinionType`,`lk`.`lookupValueChar` AS `opinionDescription`,concat(`usr`.`first_name`,' ',`usr`.`last_name`) AS `userName` from (((`project` join `opinion` on((`project`.`projectID` = `opinion`.`itemID`))) join `lookup` `lk` on(((`lk`.`lookupSubTypeID` = `opinion`.`opinionType`) and (`lk`.`lookupTypeID` = 20)))) join `users` `usr` on((`opinion`.`userID` = `usr`.`id`))) where isnull(`opinion`.`deletedDate`);


-- Dumping structure for view simpricity.v_project_pie
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_pie`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_pie` AS select `prj`.`projectID` AS `projectID`,`tsl`.`taskListName` AS `taskListName`,count(`tsk`.`taskID`) AS `countTasks`,`tsk`.`deletedDate` AS `deletedDate` from ((`project` `prj` left join `tasklist` `tsl` on((`prj`.`projectID` = `tsl`.`projectID`))) left join `task` `tsk` on((`tsk`.`taskListID` = `tsl`.`taskListID`))) group by `prj`.`projectID`,`tsl`.`taskListDescription`;


-- Dumping structure for view simpricity.v_project_tasklists
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_tasklists`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_tasklists` AS select distinct `pr`.`projectID` AS `projectID`,`pr`.`projectName` AS `projectName`,`pr`.`clientID` AS `clientID`,`tl`.`taskListID` AS `taskListID`,`tl`.`taskListName` AS `taskListName`,`upr`.`userID` AS `userID`,`pr`.`deletedDate` AS `deletedDate` from ((`project` `pr` join `tasklist` `tl` on((`pr`.`projectID` = `tl`.`projectID`))) join `userproject` `upr` on((`upr`.`projectID` = `pr`.`projectID`)));


-- Dumping structure for view simpricity.v_project_tasks
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_tasks`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_tasks` AS select distinct `pr`.`projectID` AS `projectID`,`pr`.`projectName` AS `projectName`,`pr`.`projectDescription` AS `projectDescription`,`tl`.`taskListID` AS `taskListID`,`tl`.`taskListName` AS `taskListName`,`tl`.`taskListDescription` AS `taskListDescription`,`tk`.`taskID` AS `taskID`,`tk`.`taskDescription` AS `taskDescription`,concat(left(`tk`.`taskDescription`,80),'...') AS `taskDescriptionShort`,`tk`.`taskTypeID` AS `taskTypeID`,`tk`.`taskStatusID` AS `taskStatusID`,`tk`.`taskPriorityID` AS `taskPriorityID`,`tk`.`assignedTo` AS `assignedTo`,`lkst`.`lookupValueChar` AS `taskStatus`,`lkpr`.`lookupValueChar` AS `taskPriority` from ((((`project` `pr` join `tasklist` `tl` on((`pr`.`projectID` = `tl`.`projectID`))) left join `task` `tk` on((`tl`.`taskListID` = `tk`.`taskListID`))) left join `lookup` `lkst` on(((`tk`.`taskStatusID` = `lkst`.`lookupValueNum`) and (`lkst`.`lookupTypeID` = 21)))) left join `lookup` `lkpr` on(((`tk`.`taskPriorityID` = `lkpr`.`lookupValueNum`) and (`lkpr`.`lookupTypeID` = 4))));


-- Dumping structure for view simpricity.v_project_users
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_users`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_users` AS select `us`.`first_name` AS `first_name`,`us`.`last_name` AS `last_name`,`up`.`userID` AS `userid`,`up`.`projectID` AS `projectID`,`tl`.`taskListID` AS `taskListID`,`tk`.`taskID` AS `taskID` from (((`userproject` `up` join `tasklist` `tl` on((`up`.`projectID` = `tl`.`projectID`))) join `task` `tk` on((`tk`.`taskListID` = `tk`.`taskListID`))) join `users` `us` on((`us`.`id` = `up`.`userID`)));


-- Dumping structure for view simpricity.v_project_user_emails
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_project_user_emails`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_user_emails` AS select distinct `us`.`email` AS `email`,`us`.`first_name` AS `first_name`,`us`.`last_name` AS `last_name`,`up`.`projectID` AS `projectID` from (((`userproject` `up` join `users` `us` on((`us`.`id` = `up`.`userID`))) join `project` `pr` on(`pr`.`stakeholderID`)) join `project` `pr2` on(`pr2`.`projectManagerID`));


-- Dumping structure for view simpricity.v_registered_user
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_registered_user`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_registered_user` AS select `users`.`id` AS `userID`,`users`.`email` AS `email`,`users`.`first_name` AS `first_name`,`users`.`last_name` AS `last_name`,`users`.`company` AS `company`,`users`.`phone` AS `phone` from `users`;


-- Dumping structure for view simpricity.v_search
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_search`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_search` AS select `pr`.`projectID` AS `projectID`,`pr`.`organisationID` AS `organisationID`,`pr`.`projectName` AS `projectName`,`pr`.`projectDescription` AS `projectDescription`,`tl`.`taskListID` AS `taskListID`,`tl`.`taskListName` AS `taskListName`,`tl`.`taskListDescription` AS `taskListDescription`,`tk`.`taskID` AS `taskID`,`tk`.`taskDescription` AS `taskDescription`,`up`.`userID` AS `userID`,`pr`.`projectID` AS `id` from (((`project` `pr` left join `tasklist` `tl` on((`pr`.`projectID` = `tl`.`projectID`))) left join `task` `tk` on((`tl`.`taskListID` = `tk`.`taskListID`))) join `userproject` `up` on((`up`.`projectID` = `pr`.`projectID`)));


-- Dumping structure for view simpricity.v_subscribers_recent
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_subscribers_recent`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_subscribers_recent` AS select `acc`.`accountName` AS `accountName`,`acc`.`authenticationID` AS `authenticationID`,`acc`.`authenticationID2` AS `authenticationID2`,`acc`.`authenticationID3` AS `authenticationID3`,`cli`.`clientName` AS `clientName`,`cli`.`city` AS `city`,`cli`.`country` AS `country`,`acc`.`createdDate` AS `createdDate` from (`account` `acc` left join `client` `cli` on((`acc`.`accountID` = `cli`.`accountID`))) where ((`acc`.`createdDate` > (curdate() - interval 28 day)) and (`acc`.`membershipTypeID` <> 2));


-- Dumping structure for view simpricity.v_subscription
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_subscription`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_subscription` AS select `ac`.`authenticationID` AS `authenticationID`,`ac`.`authenticationID2` AS `authenticationID2`,`org`.`organisationID` AS `organisationID`,`org`.`organisationName` AS `organisationName`,`ac`.`firstname` AS `firstname`,`ac`.`lastname` AS `lastname`,`ac`.`phone` AS `phone`,`ac`.`email` AS `email` from ((`account` `ac` join `client` `cl` on((`ac`.`accountID` = `cl`.`accountID`))) join `organisation` `org` on((`org`.`clientID` = `cl`.`clientID`)));


-- Dumping structure for view simpricity.v_suggest_problem_links
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_suggest_problem_links`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_suggest_problem_links` AS select `problem`.`problemID` AS `id`,`problem`.`problemHeader` AS `value`,`userorganisation`.`userID` AS `userID` from (`problem` join `userorganisation` on((`problem`.`organisationID` = `userorganisation`.`organisationID`)));


-- Dumping structure for view simpricity.v_suggest_project_links
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_suggest_project_links`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_suggest_project_links` AS select `project`.`projectID` AS `id`,`project`.`projectName` AS `value`,`userproject`.`userID` AS `userID` from (`project` join `userproject` on((`project`.`projectID` = `userproject`.`projectID`)));


-- Dumping structure for view simpricity.v_tasklist_activity
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_tasklist_activity`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_tasklist_activity` AS select `tkl`.`taskListID` AS `taskListID`,`tkl`.`createdDate` AS `date`,`tkl`.`createdBy` AS `userID`,concat(`usr`.`first_name`,' ',`usr`.`last_name`) AS `name`,'Created' AS `activity` from (`tasklist` `tkl` join `users` `usr` on((`usr`.`id` = `tkl`.`createdBy`))) union select `tkl`.`taskListID` AS `taskListID`,`tkl`.`updatedDate` AS `date`,`tkl`.`updatedBy` AS `userID`,concat(`usr`.`first_name`,' ',`usr`.`last_name`) AS `name`,'Last Updated' AS `activity` from (`tasklist` `tkl` join `users` `usr` on((`usr`.`id` = `tkl`.`updatedBy`))) union select `bf`.`itemID` AS `taskListID`,`bf`.`created_on` AS `date`,`bf`.`user_id` AS `userID`,concat(`usr`.`first_name`,' ',`usr`.`last_name`) AS `name`,'Updated' AS `activity` from (`bf_activities` `bf` join `users` `usr` on((`usr`.`id` = `bf`.`user_id`))) where (`bf`.`itemID` = 3);


-- Dumping structure for view simpricity.v_tasklist_project
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_tasklist_project`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_tasklist_project` AS select `prj`.`projectID` AS `projectID`,`prj`.`projectName` AS `projectName`,`tkl`.`taskListID` AS `taskListID`,`tkl`.`taskListName` AS `taskListName`,`tkl`.`taskListDescription` AS `taskListDescription`,`prj`.`clientID` AS `clientID` from (`tasklist` `tkl` join `project` `prj` on((`tkl`.`projectID` = `prj`.`projectID`)));


-- Dumping structure for view simpricity.v_tasklist_task
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_tasklist_task`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_tasklist_task` AS select `tkl`.`taskListID` AS `taskListID`,`tkl`.`taskListName` AS `taskListName`,`tkl`.`taskListDescription` AS `taskListDescription`,`tkl`.`clientID` AS `clientID`,`tsk`.`taskID` AS `taskID`,`tsk`.`taskDescription` AS `taskDescription`,concat(left(`tsk`.`taskDescription`,80),'...') AS `taskName`,`tsk`.`taskPriorityID` AS `taskPriorityID`,`tsk`.`taskStatusID` AS `taskStatusID`,`lk`.`lookupValueChar` AS `taskStatus`,`lk2`.`lookupValueChar` AS `taskPriority` from (((`tasklist` `tkl` join `task` `tsk` on((`tkl`.`taskListID` = `tsk`.`taskListID`))) left join `lookup` `lk` on((`tsk`.`taskStatusID` = `lk`.`lookupSubTypeID`))) left join `lookup` `lk2` on((`tsk`.`taskPriorityID` = `lk2`.`lookupSubTypeID`))) where ((`lk`.`lookupTypeID` = 21) and (`lk2`.`lookupTypeID` = 4));


-- Dumping structure for view simpricity.v_tasklist_users
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_tasklist_users`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_tasklist_users` AS select `usr`.`id` AS `id`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name`,`tl`.`taskListID` AS `taskListID`,`pr`.`projectID` AS `projectID`,`pr`.`clientID` AS `clientID` from (((`tasklist` `tl` join `project` `pr` on((`tl`.`projectID` = `pr`.`projectID`))) join `userproject` `upr` on((`upr`.`projectID` = `pr`.`projectID`))) join `users` `usr` on((`usr`.`id` = `upr`.`userID`)));


-- Dumping structure for view simpricity.v_task_dependency
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_task_dependency`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_task_dependency` AS select `tsk`.`taskID` AS `taskID`,`tkl`.`taskListID` AS `taskListID`,`prj`.`clientID` AS `clientID`,`tsk`.`taskTypeID` AS `taskTypeID`,`tsk`.`taskDescription` AS `taskDescription`,`tsk`.`taskStatusID` AS `taskStatusID`,`tsk`.`taskPriorityID` AS `taskPriorityID`,`tsk`.`assignedTo` AS `assignedTo`,`tsk`.`taskStartDate` AS `taskStartDate`,`tsk`.`taskTimeEstimate` AS `taskTimeEstimate`,`tsk`.`taskPercentComplete` AS `taskPercentComplete` from ((`task` `tsk` join `tasklist` `tkl` on((`tsk`.`taskListID` = `tkl`.`taskListID`))) join `project` `prj` on((`tkl`.`projectID` = `prj`.`projectID`)));


-- Dumping structure for view simpricity.v_task_detail
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_task_detail`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_task_detail` AS select `tsk`.`taskID` AS `taskID`,`tsk`.`taskDescription` AS `taskDescription`,`tsk`.`taskTypeID` AS `taskTypeID`,`lkpr`.`lookupValueChar` AS `taskPriority`,`lkst`.`lookupValueChar` AS `taskStatus`,`lkpr`.`lookupValueNum` AS `taskPriorityID`,`lkst`.`lookupValueNum` AS `taskStatusID`,`tsk`.`assignedTo` AS `assignedTo`,concat(`usr`.`first_name`,' ',`usr`.`last_name`) AS `assignedToName`,date_format(`tsk`.`taskStartDate`,'%Y/%m/%d') AS `taskStartDate`,`tsk`.`taskTimeEstimate` AS `taskTimeEstimate`,`tsk`.`taskPercentComplete` AS `taskPercentComplete`,`tsk`.`taskLinkID` AS `taskLinkID`,`tsk2`.`taskID` AS `linkedTaskID`,`tsk2`.`taskDescription` AS `linkedTaskDescription`,`upr`.`userID` AS `userID`,`prj`.`projectName` AS `projectName`,`tkl`.`taskListName` AS `tasklistName` from (((((((`task` `tsk` join `tasklist` `tkl` on((`tkl`.`taskListID` = `tsk`.`taskListID`))) join `project` `prj` on((`prj`.`projectID` = `tkl`.`projectID`))) join `userproject` `upr` on((`upr`.`projectID` = `prj`.`projectID`))) left join `lookup` `lkpr` on(((`tsk`.`taskPriorityID` = `lkpr`.`lookupValueNum`) and (`lkpr`.`lookupTypeID` = 4)))) left join `lookup` `lkst` on(((`tsk`.`taskStatusID` = `lkst`.`lookupValueNum`) and (`lkst`.`lookupTypeID` = 21)))) left join `users` `usr` on((`tsk`.`assignedTo` = `usr`.`id`))) left join `task` `tsk2` on((`tsk`.`taskLinkID` = `tsk2`.`taskID`)));


-- Dumping structure for view simpricity.v_task_documents
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_task_documents`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_task_documents` AS select `document`.`documentID` AS `documentID`,`document`.`documentTypeID` AS `documentTypeID`,`document`.`documentParentID` AS `documentParentID`,`document`.`documentName` AS `documentName`,`document`.`documentFileName` AS `documentFileName`,`document`.`documentTitle` AS `documentTitle`,`document`.`createdDate` AS `createdDate`,`document`.`createdBy` AS `createdBy`,`document`.`deletedDate` AS `deletedDate`,`document`.`deletedBy` AS `deletedBy` from `document` where ((`document`.`documentTypeID` = 3) and isnull(`document`.`deletedDate`));


-- Dumping structure for view simpricity.v_task_links
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_task_links`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_task_links` AS select distinct `tk`.`taskID` AS `taskID`,`tkl`.`taskListID` AS `taskListID`,`tk2`.`taskID` AS `taskIDIn`,`tkl2`.`taskListID` AS `taskListIDIn`,concat(left(`tk`.`taskDescription`,20),'...') AS `taskDescription` from ((((`task` `tk` join `tasklist` `tkl` on((`tk`.`taskListID` = `tkl`.`taskListID`))) join `project` `pr` on((`tkl`.`projectID` = `pr`.`projectID`))) join `tasklist` `tkl2` on((`tkl2`.`projectID` = `pr`.`projectID`))) join `task` `tk2` on((`tk2`.`taskListID` = `tkl2`.`taskListID`))) where (isnull(`pr`.`deletedDate`) and isnull(`tkl`.`deletedDate`) and isnull(`tk`.`deletedDate`));


-- Dumping structure for view simpricity.v_task_statuses
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_task_statuses`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_task_statuses` AS select `lookup`.`clientID` AS `clientID`,`lookup`.`lookupDescription` AS `lookupDescription`,`lookup`.`lookupValueNum` AS `lookupValueNum`,`lookup`.`lookupValueChar` AS `lookupValueChar`,`lookup`.`lookupOrder` AS `lookupOrder` from `lookup` where (`lookup`.`lookupTypeID` = 21);


-- Dumping structure for view simpricity.v_task_users
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_task_users`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_task_users` AS select `us`.`first_name` AS `first_name`,`us`.`last_name` AS `last_name`,`up`.`userID` AS `userid`,`up`.`projectID` AS `projectID`,`tl`.`taskListID` AS `taskListID`,`tk`.`taskID` AS `taskID` from (((`userproject` `up` join `tasklist` `tl` on((`up`.`projectID` = `tl`.`projectID`))) join `task` `tk` on((`tk`.`taskListID` = `tk`.`taskListID`))) join `users` `us` on((`us`.`id` = `up`.`userID`)));


-- Dumping structure for view simpricity.v_task_user_emails
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_task_user_emails`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_task_user_emails` AS select distinct `us`.`email` AS `email`,`us`.`first_name` AS `first_name`,`us`.`last_name` AS `last_name`,`tk`.`taskID` AS `taskID` from (((`userproject` `up` join `tasklist` `tl` on((`up`.`projectID` = `tl`.`projectID`))) join `task` `tk` on((`tk`.`taskListID` = `tl`.`taskListID`))) join `users` `us` on((`us`.`id` = `up`.`userID`)));


-- Dumping structure for view simpricity.v_time_calendar
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_time_calendar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_time_calendar` AS select `ti`.`timeID` AS `id`,`tk`.`taskDescription` AS `title`,date_format(`ti`.`timeDay`,'%Y %m %d') AS `start`,`ti`.`timeID` AS `url`,`tk`.`assignedTo` AS `assignedTo`,`ti`.`userID` AS `userID` from (`time` `ti` join `task` `tk` on((`ti`.`taskID` = `tk`.`taskID`)));


-- Dumping structure for view simpricity.v_time_detail
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_time_detail`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_time_detail` AS select `time`.`timeID` AS `timeID`,date_format(`time`.`timeDay`,'%d %b %Y') AS `timeDay`,`time`.`hours` AS `hours`,`time`.`taskID` AS `taskID`,`time`.`timeTypeID` AS `timeTypeID`,`time`.`userID` AS `userID`,`task`.`taskDescription` AS `taskDescription`,`lookup`.`lookupValueChar` AS `lookupValueChar`,`users`.`first_name` AS `first_name`,`users`.`last_name` AS `last_name`,`time`.`comments` AS `comments` from (((`time` join `task` on((`time`.`taskID` = `task`.`taskID`))) join `lookup` on((`time`.`timeTypeID` = `lookup`.`lookupValueNum`))) join `users` on((`time`.`userID` = `users`.`id`))) where (`lookup`.`lookupTypeID` = 13);


-- Dumping structure for view simpricity.v_time_grid
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_time_grid`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_time_grid` AS select distinct `pr`.`projectName` AS `project`,`pr`.`projectID` AS `projectid`,`tl`.`taskListName` AS `tasklist`,`tl`.`taskListID` AS `tasklistid`,`ti`.`timeID` AS `id`,`tk`.`taskDescription` AS `task`,`tk`.`taskID` AS `taskid`,`ti`.`timeDay` AS `timeDay`,cast(`ti`.`timeDay` as date) AS `timeDayDate`,date_format(`ti`.`timeDay`,'%H') AS `starthour`,date_format(`ti`.`timeDay`,'%i') AS `startmin`,truncate(`ti`.`hours`,0) AS `hours`,(`ti`.`hours` - truncate(`ti`.`hours`,0)) AS `mins`,((`ti`.`hours` - truncate(`ti`.`hours`,0)) * 60) AS `minsformat`,`tk`.`assignedTo` AS `assignedTo` from (((`time` `ti` join `task` `tk` on((`ti`.`taskID` = `tk`.`taskID`))) join `tasklist` `tl` on((`tl`.`taskListID` = `tk`.`taskListID`))) join `project` `pr` on((`pr`.`projectID` = `tl`.`projectID`)));


-- Dumping structure for view simpricity.v_time_task
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_time_task`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_time_task` AS select `pr`.`projectName` AS `project`,`pr`.`projectID` AS `projectid`,`tl`.`taskListName` AS `tasklist`,`tl`.`taskListID` AS `tasklistid`,left(`tk`.`taskDescription`,50) AS `task`,`tk`.`taskID` AS `taskid`,`tk`.`assignedTo` AS `assignedTo`,`tk`.`taskID` AS `id` from ((`task` `tk` join `tasklist` `tl` on((`tl`.`taskListID` = `tk`.`taskListID`))) join `project` `pr` on((`pr`.`projectID` = `tl`.`projectID`)));


-- Dumping structure for view simpricity.v_time_type
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_time_type`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_time_type` AS select `lookup`.`lookupValueNum` AS `lookupValueNum`,`lookup`.`lookupValueChar` AS `lookupValueChar`,`lookup`.`clientID` AS `clientID` from `lookup` where (isnull(`lookup`.`deletedDate`) and (`lookup`.`lookupTypeID` = 13));


-- Dumping structure for view simpricity.v_users
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_users`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_users` AS select `usr`.`id` AS `id`,`usr`.`username` AS `username`,`usr`.`email` AS `email`,`usr`.`active` AS `active`,`usr`.`phone` AS `phone`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name`,`org`.`organisationName` AS `organisationName` from (`users` `usr` join `organisation` `org` on((`usr`.`company` = `org`.`organisationID`)));


-- Dumping structure for view simpricity.v_user_assigned
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_user_assigned`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_user_assigned` AS select `project`.`projectID` AS `projectID`,`project`.`projectName` AS `projectName`,`tasklist`.`taskListID` AS `taskListID`,`tasklist`.`taskListName` AS `taskListName`,`task`.`taskID` AS `taskID`,`task`.`taskDescription` AS `taskDescription`,`task`.`assignedTo` AS `assignedTo`,`task`.`deletedDate` AS `deletedDate` from ((`task` join `tasklist` on((`task`.`taskListID` = `tasklist`.`taskListID`))) join `project` on((`project`.`projectID` = `tasklist`.`projectID`)));


-- Dumping structure for view simpricity.v_user_attributes
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_user_attributes`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_user_attributes` AS select `user_attributes`.`userID` AS `userID`,`user_attributes`.`vip` AS `vip` from `user_attributes`;


-- Dumping structure for view simpricity.v_user_context_full
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_user_context_full`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_user_context_full` AS select `usr`.`id` AS `id`,`org`.`clientID` AS `clientID`,`ausr`.`username` AS `username`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name`,`org`.`organisationName` AS `organisationname`,`ausr`.`is_superuser` AS `isSuperUser`,`ausr`.`is_staff` AS `isStaff` from ((`users` `usr` join `auth_user` `ausr` on((`usr`.`id` = `ausr`.`id`))) join `organisation` `org` on((`org`.`organisationID` = `usr`.`company`)));


-- Dumping structure for view simpricity.v_user_context_minimal
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_user_context_minimal`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_user_context_minimal` AS select `usr`.`id` AS `id`,`org`.`clientID` AS `clientID`,`ausr`.`username` AS `username` from ((`users` `usr` join `auth_user` `ausr` on((`usr`.`id` = `ausr`.`id`))) join `organisation` `org` on((`org`.`organisationID` = `usr`.`company`)));


-- Dumping structure for view simpricity.v_user_current_projects
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_user_current_projects`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_user_current_projects` AS select `upr`.`userID` AS `userID`,`proj`.`projectID` AS `projectID`,`proj`.`projectName` AS `projectName` from (`userproject` `upr` join `project` `proj` on((`upr`.`projectID` = `proj`.`projectID`))) where (isnull(`upr`.`deletedDate`) and isnull(`proj`.`deletedDate`));


-- Dumping structure for view simpricity.v_user_detail
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_user_detail`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_user_detail` AS select `usr`.`id` AS `id`,`usr`.`username` AS `username`,`usr`.`email` AS `email`,`usr`.`active` AS `active`,`usr`.`phone` AS `phone`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name`,`org`.`organisationName` AS `organisationName`,`attr`.`vip` AS `vip`,`pyr`.`defaultRate` AS `pay_rate`,`txr`.`defaultRate` AS `tax_rate`,`org`.`clientID` AS `clientID` from ((((`users` `usr` join `organisation` `org` on((`usr`.`company` = `org`.`organisationID`))) left join `user_attributes` `attr` on((`usr`.`id` = `attr`.`userID`))) left join `user_payrate` `pyr` on((`usr`.`id` = `pyr`.`userID`))) left join `user_taxrate` `txr` on((`usr`.`id` = `txr`.`userID`)));


-- Dumping structure for view simpricity.v_user_group
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_user_group`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_user_group` AS select `users`.`id` AS `userID`,`users_groups`.`group_id` AS `group_id`,`groups`.`name` AS `name` from ((`users` join `users_groups` on((`users`.`id` = `users_groups`.`user_id`))) join `groups` on((`users_groups`.`group_id` = `groups`.`id`)));


-- Dumping structure for view simpricity.v_user_group_detail
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_user_group_detail`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_user_group_detail` AS select `users`.`id` AS `userID`,`users_groups`.`group_id` AS `group_id`,`groups`.`name` AS `name`,`groups`.`description` AS `description` from ((`users` join `users_groups` on((`users`.`id` = `users_groups`.`user_id`))) join `groups` on((`users_groups`.`group_id` = `groups`.`id`)));


-- Dumping structure for view simpricity.v_user_login
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_user_login`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_user_login` AS select `usr`.`id` AS `id`,`usr`.`username` AS `username`,`usr`.`email` AS `email`,`usr`.`active` AS `active`,`usr`.`password` AS `password` from ((`users` `usr` join `organisation` `org` on((`usr`.`company` = `org`.`organisationID`))) left join `user_attributes` `attr` on((`usr`.`id` = `attr`.`userID`)));


-- Dumping structure for view simpricity.v_user_potential_projects
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_user_potential_projects`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_user_potential_projects` AS select `org`.`organisationID` AS `organisationID`,`org`.`organisationName` AS `organisationName`,`usr`.`id` AS `userID`,`usr`.`first_name` AS `first_name`,`usr`.`last_name` AS `last_name`,`proj`.`projectID` AS `projectID`,`proj`.`projectName` AS `projectName` from (((`userorganisation` `uorg` join `users` `usr` on((`uorg`.`organisationID` = `usr`.`company`))) join `organisation` `org` on((`org`.`organisationID` = `uorg`.`organisationID`))) join `project` `proj` on((`org`.`organisationID` = `proj`.`organisationID`))) where (isnull(`uorg`.`deletedDate`) and isnull(`org`.`deletedDate`) and (not(`proj`.`projectID` in (select `upr`.`projectID` from `userproject` `upr` where (`upr`.`userID` = `usr`.`id`)))));


-- Dumping structure for view simpricity.v_user_projects
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_user_projects`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_user_projects` AS select `uorg`.`userID` AS `userID`,`uorg`.`organisationID` AS `organisationID`,`proj`.`projectID` AS `projectID`,`proj`.`projectName` AS `projectName` from (`userorganisation` `uorg` join `project` `proj` on((`uorg`.`organisationID` = `proj`.`organisationID`))) where (isnull(`uorg`.`deletedDate`) and isnull(`proj`.`deletedDate`));
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
