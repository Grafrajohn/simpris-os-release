CREATE
VIEW `v_problems` AS
    SELECT
        `pro`.`clientID` AS `clientID`,
        `pro`.`problemID` AS `problemID`,
        `pro`.`organisationID` AS `organisationID`,
        `lookty`.`lookupDescription` AS `problemType`,
        `pro`.`problemDescription` AS `problemDescription`,
        `pro`.`noOfPeopleAffected` AS `noOfPeopleAffected`,
        `pro`.`scope` AS `scope`,
        `pro`.`problemHeader` AS `problemHeader`,
        `pro`.`assignedTo` AS `assignedTo`,
        `lookpty`.`lookupDescription` AS `lookupDescription`,
        `looksc`.`lookupDescription` AS `problemScope`,
        `lookst`.`lookupDescription` AS `problemStatus`,
        `lookpr`.`lookupDescription` AS `problemPriority`,
        `looksc`.`lookupValueNum` AS `problemScopeID`,
        `lookpr`.`lookupValueNum` AS `problemPriorityID`,
        `lookst`.`lookupValueNum` AS `problemStatusID`,
        `pro`.`createdBy` AS `createdBy`,
        DATE_FORMAT(`pro`.`createdDate`, '%d %b %Y') AS `createdDate`,
        `usr`.`first_name` AS `first_name`,
        `usr`.`last_name` AS `last_name`,
        `pro`.`problemID` AS `id`,
        `que`.`queueName` AS `queuename`
    FROM
        (((((((`problem` `pro`
        LEFT JOIN `lookup` `lookty` ON (((`pro`.`problemTypeID` = `lookty`.`lookupSubTypeID`)
            AND (`lookty`.`lookupTypeID` = 8))))
        LEFT JOIN `lookup` `lookpty` ON (((`pro`.`problemTypeID` = `lookpty`.`lookupSubTypeID`)
            AND (`lookpty`.`lookupTypeID` = 9))))
        LEFT JOIN `lookup` `looksc` ON (((`pro`.`scope` = `looksc`.`lookupSubTypeID`)
            AND (`looksc`.`lookupTypeID` = 10))))
        LEFT JOIN `lookup` `lookst` ON (((`pro`.`problemStatusID` = `lookst`.`lookupSubTypeID`)
            AND (`lookst`.`lookupTypeID` = 11))))
        LEFT JOIN `lookup` `lookpr` ON (((`pro`.`problemPriorityID` = `lookpr`.`lookupSubTypeID`)
            AND (`lookpr`.`lookupTypeID` = 12))))
        LEFT JOIN `users` `usr` ON ((`pro`.`assignedTo` = `usr`.`id`)))
        LEFT JOIN `queue` `que` ON ((`pro`.`queueID` = `que`.`queueID`)))