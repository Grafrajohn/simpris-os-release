CREATE 
VIEW `v_project_documents` AS
    SELECT 
        `document`.`documentID` AS `documentID`,
        `document`.`documentTypeID` AS `documentTypeID`,
        `document`.`documentParentID` AS `documentParentID`,
        `document`.`documentName` AS `documentName`,
        `document`.`documentFileName` AS `documentFileName`,
        `document`.`documentTitle` AS `documentTitle`,
        `document`.`createdDate` AS `createdDate`,
        `document`.`createdBy` AS `createdBy`,
        `document`.`deletedDate` AS `deletedDate`,
        `document`.`deletedBy` AS `deletedBy`,
        `document`.`documentID` AS `id`
    FROM
        `document`
    WHERE
        ((`document`.`documentTypeID` = 2)
            AND ISNULL(`document`.`deletedDate`))