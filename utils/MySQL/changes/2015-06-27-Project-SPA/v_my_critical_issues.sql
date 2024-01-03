CREATE 
VIEW `v_my_critical_issues` AS
    SELECT DISTINCT
        `pr`.`projectName` AS `projectName`,
        `pr`.`projectID` AS `projectID`,
        `tk`.`taskDescription` AS `taskDescription`,
        `tk`.`taskID` AS `taskID`,
        `tk`.`assignedTo` AS `assignedTo`,
        `pr`.`organisationID` AS `organisationID`,
        `tk`.`deletedDate` AS `deletedDate`,
        `upr`.`userID` AS `userID`
    FROM
        (((`project` `pr`
        JOIN `tasklist` `tl` ON ((`pr`.`projectID` = `tl`.`projectID`)))
        JOIN `task` `tk` ON ((`tl`.`taskListID` = `tk`.`taskListID`)))
        JOIN `userproject` `upr` ON ((`upr`.`projectID` = `pr`.`projectID`)))
    WHERE
        (`tk`.`taskPriorityID` = 1) 
    UNION SELECT DISTINCT
        `prb`.`problemHeader` AS `problemHeader`,
        `prb`.`problemID` AS `problemID`,
        NULL AS `NULL`,
        NULL AS `NULL`,
        `prb`.`assignedTo` AS `assignedTo`,
        `prb`.`organisationID` AS `organisationID`,
        `prb`.`deletedDate` AS `deletedDate`,
        NULL AS `NULL`
    FROM
        `problem` `prb`
    WHERE
        (`prb`.`problemPriorityID` = 1)