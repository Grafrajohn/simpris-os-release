CREATE 
VIEW `v_projectgantt_jq` AS
    SELECT 
        `prj`.`projectID` AS `projectID`,
        `prj`.`projectName` AS `projectName`,
        `prj`.`projectDescription` AS `projectDescription`,
        `prj`.`updatedDate` AS `updatedDate`,
        `prj`.`updatedBy` AS `updatedBy`,
        `tsl`.`taskListID` AS `taskListID`,
        `tsl`.`taskListName` AS `taskListName`,
        `tsl`.`taskListDescription` AS `taskListDescription`,
        `tsk`.`taskID` AS `taskID`,
        `tsk`.`taskDescription` AS `taskDescription`,
        IFNULL(`tsk`.`taskLinkID`, `tsk`.`taskID`) AS `taskOrderID`,
        `prj`.`deletedDate` AS `deletedDate`,
        IFNULL((UNIX_TIMESTAMP((`tsk2`.`taskStartDate` + INTERVAL `tsk2`.`taskTimeEstimate` DAY)) * 1000),
                IFNULL((UNIX_TIMESTAMP(`tsk`.`taskStartDate`) * 1000),
                        (UNIX_TIMESTAMP(`tsk`.`createdDate`) * 1000))) AS `taskStartDate`,
        `tsk`.`assignedTo` AS `assignedTo`,
        (UNIX_TIMESTAMP((`tsk`.`taskStartDate` + INTERVAL `tsk`.`taskTimeEstimate` DAY)) * 1000) AS `taskEndDate`,
        `tsk`.`taskTimeEstimate` AS `taskTimeEstimate`,
        `tsk`.`taskStartDate` AS `taskStartDate_unformatted`,
        `tsk`.`taskTimeEstimate` AS `time_estimate`
    FROM
        (((`project` `prj`
        JOIN `tasklist` `tsl` ON ((`prj`.`projectID` = `tsl`.`projectID`)))
        JOIN `task` `tsk` ON ((`tsk`.`taskListID` = `tsl`.`taskListID`)))
        LEFT JOIN `task` `tsk2` ON ((`tsk`.`taskID` = `tsk2`.`taskLinkID`)))
    WHERE
        ISNULL(`tsk`.`deletedDate`)
    ORDER BY `prj`.`projectID` , IFNULL(`tsk`.`taskLinkID`, `tsk`.`taskID`) , `tsk`.`taskListID` , `tsk`.`assignedTo` , `tsk`.`taskStartDate`