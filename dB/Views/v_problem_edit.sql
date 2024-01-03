CREATE
VIEW `v_problem_edit` AS
    SELECT
        `pro`.`clientID` AS `clientID`,
        `pro`.`problemID` AS `problemID`,
        `pro`.`organisationID` AS `organisationID`,
        `org`.`organisationName` AS `organisationName`,
        `pro`.`problemDescription` AS `problemDescription`,
        `pro`.`noOfPeopleAffected` AS `noOfPeopleAffected`,
        `pro`.`scope` AS `problemScopeID`,
        `pro`.`problemSubTypeID` AS `problemSubTypeID`,
        `pro`.`problemTypeID` AS `problemTypeID`,
        `pro`.`problemStatusID` AS `problemStatusID`,
        `pro`.`problemPriorityID` AS `problemPriorityID`,
        `pro`.`problemHeader` AS `problemHeader`,
        `pro`.`assignedTo` AS `assignedTo`,
        `pro`.`createdBy` AS `createdBy`,
        `pro`.`problemID` AS `id`,
        pro.queueID as queueID
    FROM
        (`problem` `pro`
        JOIN `organisation` `org` ON ((`pro`.`organisationID` = `org`.`organisationID`)))