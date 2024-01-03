CREATE 
VIEW `v_project_tasks` AS
    SELECT DISTINCT
        `pr`.`projectID` AS `projectID`,
        `pr`.`projectName` AS `projectName`,
        `pr`.`projectDescription` AS `projectDescription`,
        `tl`.`taskListID` AS `taskListID`,
        `tl`.`taskListName` AS `taskListName`,
        `tl`.`taskListDescription` AS `taskListDescription`,
        `tk`.`taskID` AS `taskID`,
        `tk`.`taskDescription` AS `taskDescription`,
        CONCAT(LEFT(`tk`.`taskDescription`, 80), '...') AS `taskDescriptionShort`,
        `tk`.`taskTypeID` AS `taskTypeID`,
        `tk`.`taskStatusID` AS `taskStatusID`,
        `tk`.`taskPriorityID` AS `taskPriorityID`,
        `tk`.`assignedTo` AS `assignedTo`,
        `lkst`.`lookupValueChar` AS `taskStatus`,
        `lkpr`.`lookupValueChar` AS `taskPriority`,
        `tk`.`taskID` AS `id`
    FROM
        ((((`project` `pr`
        JOIN `tasklist` `tl` ON ((`pr`.`projectID` = `tl`.`projectID`)))
        LEFT JOIN `task` `tk` ON ((`tl`.`taskListID` = `tk`.`taskListID`)))
        LEFT JOIN `lookup` `lkst` ON (((`tk`.`taskStatusID` = `lkst`.`lookupValueNum`)
            AND (`lkst`.`lookupTypeID` = 21))))
        LEFT JOIN `lookup` `lkpr` ON (((`tk`.`taskPriorityID` = `lkpr`.`lookupValueNum`)
            AND (`lkpr`.`lookupTypeID` = 4))))