--
-- File generated with SQLiteStudio v3.0.7 on Wed Mar 16 21:40:42 2016
--
-- Text encoding used: windows-1252
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: organisation
CREATE TABLE `organisation` (
  `organisationID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `organisationName` varchar(100) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`organisationID`));

-- Table: taskstep
CREATE TABLE `taskstep` (
  `taskstepID` int(11) NOT NULL,
  `taskID` int(11) DEFAULT NULL,
  `steporder` int(11) DEFAULT NULL,
  PRIMARY KEY (`taskstepID`)
);

-- Table: opinion
CREATE TABLE `opinion` (
  `opinionID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `itemType` int(11) NOT NULL,--'Type of thing the opinion expressed about: 
  `itemID` int(11) NOT NULL,
  `opinionType` int(11) DEFAULT NULL,
  `opinion` varchar(250) DEFAULT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`opinionID`)
);

-- Table: organisation_archive
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
);

-- Table: payrate
CREATE TABLE `payrate` (
  `payrateID` int(11) NOT NULL,
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
);

-- Table: auth_user_groups
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL ,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Table: board
CREATE TABLE `board` (
  `id` int(11) NOT NULL ,
  `userID` int(11) NOT NULL,
  `itemID` int(11) NOT NULL,
  `itemType` int(11) NOT NULL,
  `columnNo` int(11) NOT NULL,
  `itemOrder` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Table: client
CREATE TABLE `client` (
  `clientID` int(11) NOT NULL ,
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
  PRIMARY KEY (`clientID`)
);

-- Table: invoice
CREATE TABLE `invoice` (
  `invoiceID` int(10) NOT NULL,
  `clientID` int(11) NOT NULL,
  `userID` mediumint(10) NOT NULL,
  `statusID` int(10) NOT NULL DEFAULT '1' ,
  `supersededBy` int(10) DEFAULT NULL ,
  `description` varchar(50) NOT NULL ,
  `comments` varchar(500) NOT NULL ,
  `createdDate` datetime NOT NULL,
  `createdBy` mediumint(8) NOT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` mediumint(8) DEFAULT NULL,
  `invoicecol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`invoiceID`)
-- KEY `ix_invoice_client` (`clientID`)
);

-- Table: question
CREATE TABLE `question` (
  `questionID` int(11) NOT NULL,
  `questionName` varchar(45) DEFAULT NULL,
  `questionText` varchar(5000) DEFAULT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`questionID`)
);

-- Table: problem
CREATE TABLE `problem` (
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
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`problemID`));

-- Table: status
CREATE TABLE `status` (
  `statusID` int(11) NOT NULL,
  `userID` mediumint(9) DEFAULT NULL,
  `itemID` int(11) DEFAULT NULL,
  `itemType` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `statuscol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`statusID`)
);

-- Table: auth_permission
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL ,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Table: meta
CREATE TABLE `meta` (
  `id` mediumint(8)NOT NULL,
  `user_id` mediumint(8)DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `mainOrganisationID` int(11) DEFAULT NULL,--'Organisation to which the user 

  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- Table: django_migrations
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL ,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

-- Table: project
CREATE TABLE `project` (
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
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`projectID`)
);

-- Table: queue_user
CREATE TABLE `queue_user` (
  `id` int(11) NOT NULL,
  `queueID` int(11) NOT NULL,
  `queueUserID` int(11) DEFAULT NULL,
  `queueTeamID` int(11) DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `createdDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- Table: login_attempts
CREATE TABLE `login_attempts` (
  `id` mediumint(8)NOT NULL,
  `ip_address` varbinary(16) NOT NULL,
  `login` varchar(100) NOT NULL,
  `time` int(11)DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- Table: time
CREATE TABLE `time` (
  `timeID` int(10) NOT NULL,
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
  PRIMARY KEY (`timeID`)
);

-- Table: step
CREATE TABLE `step` (
  `stepID` int(11) NOT NULL,
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
);

-- Table: django_admin_log
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL ,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Table: document
CREATE TABLE `document` (
  `documentID` int(11) NOT NULL,
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
);

-- Table: auth_group_permissions
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL ,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Table: team_user
CREATE TABLE `team_user` (
  `id` int(11) NOT NULL,
  `teamID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `createdBy` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- Table: user_payrate
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
);

-- Table: team
CREATE TABLE `team` (
  `teamID` int(11) NOT NULL,
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
);

-- Table: lookup
CREATE TABLE `lookup` (
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
  PRIMARY KEY (`clientID`,`lookupTypeID`,`lookupSubTypeID`)
-- KEY `ix_lookup_typeid` (`lookupTypeID`),
-- KEY `ix_lookup_subtypeid` (`lookupSubTypeID`)
);

-- Table: programme
CREATE TABLE `programme` (
  `programmeID` int(10) NOT NULL,
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
  PRIMARY KEY (`programmeID`)
);

-- Table: user_attributes
CREATE TABLE `user_attributes` (
  `userID` int(11) NOT NULL,
  `vip` char(1) NOT NULL DEFAULT 'n',
  `countryID` int(11) DEFAULT NULL,
  `mobilePhoneNo` varchar(20) DEFAULT NULL,
  `faxNo` varchar(20) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`userID`)
);

-- Table: queue
CREATE TABLE `queue` (
  `queueID` int(11) NOT NULL,
  `queueName` varchar(45) NOT NULL,
  `queueDescription` varchar(450) DEFAULT NULL,
  `createdBy` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`queueID`)
);

-- Table: questionnaire_question
CREATE TABLE `questionnaire_question` (
  `questionnaireID` int(11) NOT NULL,
  `questionID` int(11) NOT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`questionnaireID`,`questionID`)
);

-- Table: groups
CREATE TABLE `groups` (
  `id` mediumint(8) NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Table: auth_user
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL ,
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
  PRIMARY KEY (`id`)
);

-- Table: task_archive
CREATE TABLE `task_archive` (
  `taskID` int(11) NOT NULL,
  `taskListID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `taskTypeID` int(11) NOT NULL,
  `taskName` varchar(50) NOT NULL,
  `taskDescription` varchar(500) NOT NULL,
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
);

-- Table: auth_group
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL ,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
  -- UNIQUE KEY `name` (`name`)
);

-- Table: tasklist
CREATE TABLE `tasklist` (
  `taskListID` int(11) NOT NULL,
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
  PRIMARY KEY (`taskListID`)
);

-- Table: bf_activities
CREATE TABLE `bf_activities` (
  `activity_id` bigint(20) NOT NULL ,
  `user_id` bigint(20) NOT NULL DEFAULT '0',
  `activity` varchar(255) NOT NULL,
  `module` varchar(255) NOT NULL,
  `created_on` datetime NOT NULL,
  `deleted` tinyint(12) NOT NULL DEFAULT '0',
  `itemID` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`activity_id`)
);

-- Table: userorganisation
CREATE TABLE `userorganisation` (
  `id` int(11) NOT NULL,
  `userID` mediumint(11) NOT NULL,
  `organisationID` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`));

-- Table: user_taxrate
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
);

-- Table: user_status
CREATE TABLE `user_status` (
  `statusID` int(11) NOT NULL,
  `userID` mediumint(9) DEFAULT NULL,
  `itemID` int(11) DEFAULT NULL,
  `itemType` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `statuscol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`statusID`)
);

-- Table: tasklist_archive
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
);

-- Table: taxrate
CREATE TABLE `taxrate` (
  `taxrateID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `taxrateDescription` varchar(100) NOT NULL,
  `taxrate` decimal(10,2) NOT NULL,
  `effectiveDate` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `createdDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`taxrateID`)
);

-- Table: answer
CREATE TABLE `answer` (
  `answerID` int(11) NOT NULL ,
  `questionID` int(11) NOT NULL,
  `answer` varchar(5000) NOT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`answerID`)
);

-- Table: comment
CREATE TABLE `comment` (
  `commentID` int(11) NOT NULL ,
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
);

-- Table: invoiceline
CREATE TABLE `invoiceline` (
  `invoiceID` int(10) NOT NULL,
  `lineNo` int(10) NOT NULL,
  `taskID` int(10) NOT NULL,
  `timeID` int(10) NOT NULL,
  `itemDescription` varchar(150) NOT NULL,
  `tax1Rate` decimal(10,2)NOT NULL,
  `tax2Rate` decimal(10,2)NOT NULL,
  `tax3Rate` decimal(10,2)NOT NULL,
  `hourlyRate` decimal(10,2)NOT NULL,
  `noHours` decimal(10,1)NOT NULL,
  `agreedRate` decimal(10,1)NOT NULL,--'Where rate agreed instead of hourly rate',
  `tax1` decimal(10,2)NOT NULL,
  `tax2` decimal(10,2)NOT NULL,
  `tax3` decimal(10,2)NOT NULL,
  `grossTotal` decimal(10,2)NOT NULL,--'Total before tax',
  `netTotal` decimal(10,2)NOT NULL,--'Total after tax',
  PRIMARY KEY (`invoiceID`,`lineNo`)
);

-- Table: task_template
CREATE TABLE `task_template` (
  `tasktemplateID` int(11) NOT NULL,
  `clientID` int(11) DEFAULT NULL,
  `tasktemplateName` varchar(100) DEFAULT NULL,
  `createdDate` datetime DEFAULT NULL,
  `createdBy` int(11) DEFAULT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`tasktemplateID`)
);

-- Table: useractivity
CREATE TABLE `useractivity` (
  `activityID` int(11) NOT NULL,
  `userID` mediumint(11) NOT NULL,
  `activityTypeID` mediumint(11) NOT NULL,
  `activityData` varchar(100) DEFAULT NULL,
  `activity_module_id` int(11) DEFAULT NULL,
  `client_id` int(11) DEFAULT NULL,
  `activityDate` datetime NOT NULL,
  PRIMARY KEY (`activityID`)
);

-- Table: phase
CREATE TABLE `phase` (
  `phaseID` int(11) NOT NULL,
  `clientID` int(11) NOT NULL,
  `phaseName` varchar(50) NOT NULL,
  `phaseDescription` varchar(500) NULL,
  `startDate` datetime DEFAULT NULL,
  `endDate` datetime DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`phaseID`)
);

-- Table: problemlink
CREATE TABLE `problemlink` (
  `id` int(11) NOT NULL,
  `problemID` int(11) NOT NULL,
  `problemLinkID` int(11) NOT NULL,
  `problemLinkType` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- Table: country
CREATE TABLE `country` (
  `countryID` int(10) NOT NULL,
  `countryName` varchar(100) NOT NULL,
  PRIMARY KEY (`countryID`)
  -- UNIQUE KEY `ix_country` (`countryName`)
);

-- Table: account
CREATE TABLE `account` (
  `accountID` int(11) NOT NULL ,
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
  PRIMARY KEY (`accountID`)
  -- UNIQUE KEY `ix_account` (`accountName`,`email`)
);

-- Table: user_configuration
CREATE TABLE `user_configuration` (
  `userID` mediumint(9) NOT NULL,
  `lookupTypeID` int(11)NOT NULL,
  `configurationData` varchar(50) NOT NULL,
  `configurationDataNum` float NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime NOT NULL,
  `updatedBy` int(11) NOT NULL,
  `deletedDate` datetime NOT NULL,
  `deletedBy` int(11) NOT NULL,
  PRIMARY KEY (`userID`,`lookupTypeID`)
);

-- Table: questionnaire
CREATE TABLE `questionnaire` (
  `questionnaireID` int(11) NOT NULL,
  `questionnaireName` varchar(45) NOT NULL,
  `contactUserID` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL,
  PRIMARY KEY (`questionnaireID`)
);

-- Table: problem_archive
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
  `assignedTo` int(11) DEFAULT NULL,
  `completedDate` datetime DEFAULT NULL,
  `createdDate` datetime NOT NULL,
  `createdBy` int(11) NOT NULL,
  `updatedDate` datetime DEFAULT NULL,
  `updatedBy` int(11) DEFAULT NULL,
  `deletedDate` datetime DEFAULT NULL,
  `deletedBy` int(11) DEFAULT NULL
);

-- Table: task
CREATE TABLE `task` (
  `taskID` int(11) NOT NULL,
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
  PRIMARY KEY (`taskID`)
);

-- Table: project_archive
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
);

-- Table: django_content_type
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL ,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Table: user_cookie
CREATE TABLE `user_cookie` (
  `id` int(11) NOT NULL,
  `userID` bigint(20) NOT NULL,
  `uuID` varchar(128) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(40) NOT NULL,
  `created_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Table: auth_user_user_permissions
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL ,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
