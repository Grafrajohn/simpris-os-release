CREATE 
VIEW `v_my_tasktypes` AS
    SELECT 
        `lookup`.`clientID` AS `clientID`,
        `lookup`.`lookupDescription` AS `lookupDescription`,
        `lookup`.`lookupValueNum` AS `lookupValueNum`,
        `lookup`.`lookupValueChar` AS `lookupValueChar`,
        `lookup`.`lookupSubTypeID` AS `id`
    FROM
        `lookup`
    WHERE
        (`lookup`.`lookupTypeID` = 5)