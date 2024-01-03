CREATE 
VIEW `v_project_opinion` AS
    SELECT 
        `opinion`.`opinionID` AS `opinionID`,
        `project`.`projectID` AS `projectID`,
        `opinion`.`userID` AS `userID`,
        `opinion`.`itemID` AS `itemID`,
        `opinion`.`itemType` AS `itemType`,
        `opinion`.`opinionType` AS `opinionType`,
        `opinion`.`opinion` AS `opinion`,
        `opinion`.`opinionID` AS `id`
    FROM
        (`project`
        JOIN `opinion` ON ((`project`.`projectID` = `opinion`.`itemID`)))
    WHERE
        ISNULL(`opinion`.`deletedDate`)