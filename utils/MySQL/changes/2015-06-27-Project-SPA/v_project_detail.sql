CREATE 
VIEW `v_project_detail` AS
    SELECT DISTINCT
        `project`.`projectID` AS `projectID`,
        `project`.`organisationID` AS `organisationID`,
        `project`.`programmeID` AS `programmeID`,
        `project`.`clientID` AS `clientID`,
        `project`.`projectName` AS `projectName`,
        `project`.`projectDescription` AS `projectDescription`,
        `project`.`stakeholderID` AS `stakeholderID`,
        `project`.`projectManagerID` AS `projectManagerID`,
        `project`.`deliverables` AS `deliverables`,
        `project`.`budget` AS `budget`,
        `project`.`importance` AS `importance`,
        `project`.`createdDate` AS `createdDate`,
        `project`.`createdBy` AS `createdBy`,
        `project`.`updatedDate` AS `updatedDate`,
        `project`.`updatedBy` AS `updatedBy`,
        `project`.`deletedDate` AS `deletedDate`,
        `project`.`deletedBy` AS `deletedBy`,
        `org`.`organisationName` AS `organisationName`,
        `usr`.`first_name` AS `shFirstName`,
        `usr`.`last_name` AS `shLastName`,
        `lk`.`lookupValueChar` AS `importanceDescription`,
        `usr2`.`first_name` AS `pmFirstName`,
        `usr2`.`last_name` AS `pmLastName`,
        `usr3`.`id` AS `userID`,
        `project`.`projectID` AS `id`
    FROM
        ((((((`project`
        JOIN `userproject` `upr` ON ((`project`.`projectID` = `upr`.`projectID`)))
        JOIN `users` `usr3` ON ((`upr`.`userID` = `usr3`.`id`)))
        LEFT JOIN `organisation` `org` ON ((`project`.`organisationID` = `org`.`organisationID`)))
        LEFT JOIN `users` `usr` ON ((`project`.`stakeholderID` = `usr`.`id`)))
        LEFT JOIN `lookup` `lk` ON (((`project`.`importance` = `lk`.`lookupSubTypeID`)
            AND (`lk`.`lookupTypeID` = 19))))
        LEFT JOIN `users` `usr2` ON ((`project`.`projectManagerID` = `usr2`.`id`)))
    WHERE
        ISNULL(`project`.`deletedDate`)