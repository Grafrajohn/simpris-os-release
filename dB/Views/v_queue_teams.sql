CREATE VIEW `v_queue_teams` AS
    SELECT
        `qt`.`id` AS `id`,
        `qt`.`queueID` AS `queueID`,
        `tm`.`teamID` AS `teamID`,
        `tm`.`teamName` AS `teamName`,
        `tm`.`teamDescription` AS `teamDescription`,
        `qt`.`deletedDate` AS `deletedDate`
    FROM
        (`team` `tm`
        JOIN `queue_team` `qt` ON ((`tm`.`teamID` = `qt`.`queueTeamID`)))