CREATE 
VIEW `v_project_opinion_detail` AS
    SELECT 
        `opinion`.`opinionID` AS `opinionID`,
        `project`.`projectID` AS `projectID`,
        `opinion`.`userID` AS `userID`,
        `opinion`.`itemID` AS `itemID`,
        `opinion`.`itemType` AS `itemType`,
        `opinion`.`opinionType` AS `opinionType`,
        `lk`.`lookupValueChar` AS `opinionDescription`,
        CONCAT(`usr`.`first_name`,
                ' ',
                `usr`.`last_name`) AS `userName`,
        `opinion`.`opinionID` AS `id`
    FROM
        (((`project`
        JOIN `opinion` ON ((`project`.`projectID` = `opinion`.`itemID`)))
        JOIN `lookup` `lk` ON (((`lk`.`lookupSubTypeID` = `opinion`.`opinionType`)
            AND (`lk`.`lookupTypeID` = 20))))
        JOIN `users` `usr` ON ((`opinion`.`userID` = `usr`.`id`)))
    WHERE
        ISNULL(`opinion`.`deletedDate`)