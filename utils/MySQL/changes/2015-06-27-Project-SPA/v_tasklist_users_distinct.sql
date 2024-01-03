CREATE 
VIEW `v_tasklist_users_distinct` AS
    SELECT DISTINCT
        `usr`.`id` AS `id`,
        `usr`.`first_name` AS `first_name`,
        `usr`.`last_name` AS `last_name`,
        `pr`.`projectID` AS `projectID`,
        `pr`.`clientID` AS `clientID`
    FROM
        (((`tasklist` `tl`
        JOIN `project` `pr` ON ((`tl`.`projectID` = `pr`.`projectID`)))
        JOIN `userproject` `upr` ON ((`upr`.`projectID` = `pr`.`projectID`)))
        JOIN `users` `usr` ON ((`usr`.`id` = `upr`.`userID`)))