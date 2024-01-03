CREATE
VIEW `v_my_users` AS
    SELECT DISTINCT
        `usr`.`id` AS `user_id`,
        `usr`.`first_name` AS `first_name`,
        `usr`.`last_name` AS `last_name`,
        `org`.`organisationID` AS `organisationID`,
        `org`.`organisationName` AS `organisationName`,
        `org`.`clientID` AS `clientID`,
        `usr`.`is_active` AS `active`,
        CONCAT(`usr`.`first_name`,
                ' ',
                `usr`.`last_name`) AS `name`,
        `uo`.`userID` AS `userID`,
        IF((`usr`.`is_active` = 1), 'Yes', 'No') AS `activeDesc`,
        `usr`.`id` AS `id`
    FROM
        (((`organisation` `org`
        JOIN `userorganisation` `uo` ON ((`org`.`organisationID` = `uo`.`organisationID`)))
        JOIN `users` ON ((`org`.`organisationID` = `users`.`company`)))
        JOIN `auth_user` `usr` ON ((`users`.`id` = `usr`.`id`)))
    UNION SELECT DISTINCT
        `usr`.`id` AS `user_id`,
        `usr`.`first_name` AS `first_name`,
        `usr`.`last_name` AS `last_name`,
        `org`.`organisationID` AS `organisationID`,
        `org`.`organisationName` AS `organisationName`,
        `org`.`clientID` AS `clientID`,
        `usr`.`is_active` AS `active`,
        CONCAT(`usr`.`first_name`,
                ' ',
                `usr`.`last_name`) AS `name`,
        `usr`.`id` AS `userID`,
        IF((`usr`.`is_active` = 1), 'Yes', 'No') AS `activeDesc`,
        `usr`.`id` AS `id`
    FROM
        ((`organisation` `org`
        JOIN `users` ON ((`org`.`organisationID` = `users`.`company`)))
        JOIN `auth_user` `usr` ON ((`users`.`id` = `usr`.`id`)))