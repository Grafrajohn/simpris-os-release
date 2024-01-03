CREATE VIEW `v_queue_users` AS
VIEW `v_queue_users` AS
    SELECT
        `qu`.`id` AS `id`,
        `us`.`id` AS `userid`,
        `qu`.`queueID` AS `queueID`,
        `us`.`first_name` AS `first_name`,
        `us`.`last_name` AS `last_name`,
        `qu`.`deletedDate` AS `deletedDate`
    FROM
        (`auth_user` `us`
        JOIN `queue_user` `qu` ON ((`us`.`id` = `qu`.`queueUserID`)))