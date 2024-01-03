DELIMITER $$
CREATE DEFINER=`root`@`localhost` FUNCTION `fn_get_client`(parm_userID int) RETURNS int(11)
BEGIN

declare var_clientID int;

select cli.clientID into var_clientID
from organisation org join client on org.clientID = cli.clientID
join users usr on usr.company = org.organisationID 
where userID = @userID; 

RETURN var_clientID;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` FUNCTION `fn_get_my_users`(parm_userID int) RETURNS int(11)
BEGIN

declare var_count integer;

select count(*) into var_count
from users usr
join userorganisation uorg on usr.id = uorg.userID 
where id = parm_userID; 

RETURN var_count;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` FUNCTION `fn_get_organisation`(parm_userID int) RETURNS int(11)
BEGIN

declare var_organisationID int;

select org.organisationID into var_organisationID
from organisation
join users usr on usr.company = org.organisationID 
where userID = @userID; 

RETURN var_organisationID;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` FUNCTION `fn_get_project_organisation`(`parm_projectID` INT) RETURNS int(11)
BEGIN

DECLARE var_organisation int;

select organisationID into var_organisation from project where projectID = parm_projectID;

RETURN var_organisation;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` FUNCTION `fn_past_date`(`parm_noOfDays` INT) RETURNS date
    DETERMINISTIC
BEGIN



DECLARE var_mydate datetime;



set var_mydate = date_add(curdate(), interval parm_noOfDays day);



return var_mydate;



END$$
DELIMITER ;
