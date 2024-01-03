CREATE VIEW `vw_select_user_index_sidebar` AS
select 'New users' AS `userName`,'' AS `column2`,'' AS `id`,0 AS `column4`,'' AS `userID`
union select distinct `usr`.`username` AS `username`,date_format(from_unixtime(`usr`.`date_joined`),'%d %b %Y') AS `created_on`,`usr`.`id` AS `id`,3 AS `3`,`uorg2`.`userID` AS `userID`
from ((`auth_user` `usr` join `userorganisation` `uorg` on((`usr`.`id` = `uorg`.`userID`)))
join `userorganisation` `uorg2` on((`uorg`.`organisationID` = `uorg2`.`organisationID`)))
where (`usr`.`date_joined` > `FN_PAST_DATE`(-(90)))
union select 'Changed users' AS `Changed users`,'' AS `column2`,'' AS `id`,5 AS `5`,'' AS `userID`
order by `column4`,`userName`,`column2`;