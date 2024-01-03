create VIEW `v_user_context_full` AS
    SELECT
        `ausr`.`id` AS `id`,
        `org`.`clientID` AS `clientID`,
        `ausr`.`username` AS `username`,
        `ausr`.`first_name` AS `first_name`,
        `ausr`.`last_name` AS `last_name`,
        `org`.`organisationID` AS `organisationID`,
        `org`.`organisationName` AS `organisationName`,
        `ausr`.`is_superuser` AS `isSuperUser`,
        `ausr`.`is_staff` AS `isStaff`
    FROM
        ((`users` `usr`
        JOIN `auth_user` `ausr` ON ((`usr`.`id` = `ausr`.`id`)))
        JOIN `organisation` `org` ON ((`org`.`organisationID` = `usr`.`company`)))