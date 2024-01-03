CREATE VIEW `v_user_context_full` AS
    SELECT 
        `usr`.`id` AS `id`,
        `org`.`clientID` AS `clientID`,
        `ausr`.`username` AS `username`,
        `usr`.`first_name` AS `first_name`,
        `usr`.`last_name` AS `last_name`,
        `org`.`organisationID` AS `organisationID`,
        `org`.`organisationName` AS `organisationName`,
        `ausr`.`is_superuser` AS `isSuperUser`,
        `ausr`.`is_staff` AS `isStaff`,
        `cli`.`clientName` AS `clientName`,
        `tea`.`teamName` AS `teamName`
    FROM
        (((((`users` `usr`
        JOIN `auth_user` `ausr` ON ((`usr`.`id` = `ausr`.`id`)))
        JOIN `organisation` `org` ON ((`org`.`organisationID` = `usr`.`company`)))
        JOIN `client` `cli` ON ((`org`.`clientID` = `cli`.`clientID`)))
        LEFT JOIN `team_user` `tu` ON ((`usr`.`id` = `tu`.`userID`)))
        LEFT JOIN `team` `tea` ON ((`tu`.`teamID` = `tea`.`teamID`)))