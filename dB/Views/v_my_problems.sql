CREATE
VIEW `v_my_problems` AS
    SELECT
        `pro`.`problemID` AS `problemID`,
        `pro`.`organisationID` AS `organisationID`,
        `lookty`.`lookupValueChar` AS `problemType`,
        `pro`.`problemHeader` AS `problemHeader`,
        `pro`.`assignedTo` AS `assignedTo`,
        `looksc`.`lookupValueChar` AS `problemScope`,
        `lookstat`.`lookupValueChar` AS `problemStatus`,
        `lookpr`.`lookupValueChar` AS `problemPriority`,
        `looksc`.`lookupValueNum` AS `problemScopeID`,
        `pro`.`createdBy` AS `createdBy`,
        `pro`.`problemID` AS `id`,
        COALESCE(`usr`.`first_name`, ' ') AS `first_name`,
        COALESCE(`usr`.`last_name`, ' ') AS `last_name`,
        `pro`.`clientID` AS `clientID`,
        pro.queueid as queueid
    FROM
        (((((`problem` `pro`
        LEFT JOIN `lookup` `lookty` ON ((`pro`.`problemTypeID` = `lookty`.`lookupSubTypeID`)))
        LEFT JOIN `lookup` `looksc` ON ((`pro`.`scope` = `looksc`.`lookupSubTypeID`)))
        LEFT JOIN `lookup` `lookstat` ON ((`pro`.`problemStatusID` = `lookstat`.`lookupSubTypeID`)))
        LEFT JOIN `lookup` `lookpr` ON ((`pro`.`problemPriorityID` = `lookpr`.`lookupSubTypeID`)))
        LEFT JOIN `users` `usr` ON ((`usr`.`id` = `pro`.`assignedTo`)))
    WHERE
        ((`lookty`.`lookupTypeID` = 8)
            AND (`looksc`.`lookupTypeID` = 10)
            AND (`lookstat`.`lookupTypeID` = 11)
            AND (`lookpr`.`lookupTypeID` = 12)
            AND ISNULL(`pro`.`deletedBy`))