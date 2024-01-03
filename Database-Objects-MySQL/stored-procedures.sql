DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `selectProjectDetail`(IN `parm_projectID` INT)
BEGIN







select *



from project 



where projectID = parm_projectID;







END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `selectProjectsMy`(IN parm_userID INT)
BEGIN







select *



from project pr inner join userProject up



on pr.projectID = up.projectID



where up.userID = parm_userID;







END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_check_recent_activity`()
BEGIN

(select 'account', accountName, createdDate, createdBy
from account)
union
(select 'client', clientName, createdDate, createdBy
from client)
union
(select 'project', projectName, createdDate, createdBy
from project)
union
(select 'task', taskDescription, createdDate, createdBy
from task)
order by 3 desc,1 desc
limit 100;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_gantt_project`(IN `parm_projectID` INT)
BEGIN







select '[' as jsonRow



union



select CONCAT('{ "name": "', tsk.taskDescription, '","desc": "', tsk.taskDescription, '", 



"values": [{"from": "/Date(',tsk.createdDate,')/", "to": "/Date(',tsk.createdDate,')/", "desc": "<b>',



tsk.taskDescription,'</b><br><b>Data</b>: [',tsk.createdDate,' - ',tsk.createdDate,'] ", "customClass": "ganttRed", "label": "',



tsk.taskDescription,'"}]},') 



from project pro inner join tasklist tkl on pro.projectID = tkl.projectID



inner join task tsk on tsk.taskListID = tkl.taskListID



where pro.projectID = parm_projectID



union



select ']';







END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_generic_chart`(in parm_table char(50), in parm_group_field char(50), in parm_lookup_id int)
BEGIN
    SET @s = CONCAT('SELECT count(*) as count,', parm_group_field, ' as group_field, lookup.lookupValueChar as lookup FROM ', parm_table, ' join lookup on lookup.lookupValueNum = ', parm_table, '.', parm_group_field, ' where lookup.lookupTypeID = ', parm_lookup_id, ' group by ', parm_group_field);
    PREPARE stmt FROM @s;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_get_project_potential_users`(IN `parm_projectID` INT(11))
BEGIN
declare var_orgID int;
	select fn_get_project_organisation(parm_projectID) into var_orgID;

    select distinct
        `us`.`first_name` AS `first_name`,
        `us`.`last_name` AS `last_name`,
        `us`.`id` AS `userID`
    from
        `users` `us`
	where (us.id in (select userID from userorganisation where organisationID = var_orgID)
	or us.company = var_orgID)
	and us.id not in (select userID from userproject where projectID = parm_projectID and deletedDate is null)
    and us.active = 1;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_get_project_users`(IN `parm_projectID` INT(11))
    READS SQL DATA
BEGIN

    select 
        `us`.`first_name` AS `first_name`,
        `us`.`last_name` AS `last_name`,
        `us`.`id` AS `userID`
    from
        `users` `us`
        join `userproject` `usp` ON `us`.`id` = `usp`.`userID`
		where usp.projectID = parm_projectID
        and usp.deletedDate is null
        and us.active = 1;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_insert_invoice_line`(IN `parm_invoiceID` INT, IN `parm_timeID` INT, IN `parm_lineNo` INT, IN parm_userID int)
BEGIN

declare var_taskID INT;
declare var_hours float;
declare var_description varchar(150);
declare var_hourlyrate decimal(10,2);
declare var_taxrate1 decimal(10,2);
declare var_taxrate2 decimal(10,2);
declare var_taxrate3 decimal(10,2);
declare var_tax1 decimal(10,2);
declare var_tax2 decimal(10,2);
declare var_tax3 decimal(10,2);
declare var_grossTotal decimal(10,2);
declare var_netTotal decimal(10,2);

select tk.taskID, IFNULL(tm.hours,0), tk.taskDescription into var_taskID, var_hours, var_description 
from time tm join task tk on tm.taskID = tk.taskID 
where timeID = parm_timeID;

select IFNULL(defaultRate,0) into var_hourlyrate
from user_payrate
where userID = parm_userID;

if var_hourlyRate IS NULL then set var_hourlyRate = 0;
end if;

select ifnull(defaultRate,0) into var_taxrate1
from user_taxrate
where userID = parm_userID;

if var_taxrate1 is null then set var_taxrate1 = 0;
end if;

set var_taxrate2 = 0;
set var_taxrate3 = 0;

set var_grossTotal = var_hourlyRate * var_hours;

set var_tax1 = var_grossTotal * var_taxrate1;
set var_tax2 = var_grossTotal * var_taxrate2;
set var_tax3 = var_grossTotal * var_taxrate3;

set var_netTotal = var_grossTotal - (var_tax1 + var_tax2 + var_tax3);

INSERT INTO `simpricity`.`invoiceline`

(invoiceID,

`lineNo`,

`taskID`,

`timeID`,

`itemDescription`,

`tax1Rate`,

`tax2Rate`,

`tax3Rate`,

`hourlyRate`,

`noHours`,

`agreedRate`,

`tax1`,

`tax2`,

`tax3`,

`grossTotal`,

`netTotal`)

VALUES

(

parm_invoiceID,

parm_lineNo,

var_TaskID,

parm_timeID,

var_description,

var_taxrate1,

var_taxrate2,

var_taxrate3,

var_hourlyrate,

var_hours,

var_hourlyrate,

var_tax1,

var_tax2,

var_tax3,

var_grossTotal,

var_netTotal

);

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_metric_client_revenue`(IN parm_userID INT)
BEGIN

declare varTotal decimal(12,2);

select sum(invl.netTotal) into varTotal
from userorganisation uorg
inner join organisation org on uorg.organisationID = org.organisationID
inner join project prj on org.organisationID = prj.organisationID
inner join tasklist tkl on prj.projectID = tkl.projectID
inner join task tsk on tkl.taskListID = tsk.taskListID
inner join invoiceline invl on tsk.taskID = invl.taskID
where uorg.userID = parm_userID;

select concat(org.organisationName, ' : ', sum(invl.netTotal)) as col1,sum(invl.netTotal*100)/varTotal as col2
from userorganisation uorg
inner join organisation org on uorg.organisationID = org.organisationID
inner join project prj on org.organisationID = prj.organisationID
inner join tasklist tkl on prj.projectID = tkl.projectID
inner join task tsk on tkl.taskListID = tsk.taskListID
inner join invoiceline invl on tsk.taskID = invl.taskID
where uorg.userID = parm_userID
group by org.organisationID,org.organisationName;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_metric_my_client_revenue`(IN parm_userID INT)
BEGIN

declare varTotal decimal(12,2);

select sum(invl.netTotal) into varTotal
from organisation org
inner join project prj on org.organisationID = prj.organisationID
inner join tasklist tkl on prj.projectID = tkl.projectID
inner join task tsk on tkl.taskListID = tsk.taskListID
inner join invoiceline invl on tsk.taskID = invl.taskID
where tsk.assignedTo = parm_userID;

select concat(org.organisationName, ' : ', sum(invl.netTotal)) as col1,sum(invl.netTotal*100)/varTotal as col2
from organisation org
inner join project prj on org.organisationID = prj.organisationID
inner join tasklist tkl on prj.projectID = tkl.projectID
inner join task tsk on tkl.taskListID = tsk.taskListID
inner join invoiceline invl on tsk.taskID = invl.taskID
where tsk.assignedTo = parm_userID
group by org.organisationID,org.organisationName;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_metric_my_problems_project`(IN parm_userID INT)
BEGIN

declare varTotal int;
set varTotal = 0;

select count(prb.problemID) into varTotal
from project prj
inner join problemlink plk on prj.projectID = plk.problemLinkID and plk.problemLinkType = 1
inner join problem prb on prb.problemID = plk.problemLinkID and prb.completedDate is null and prb.deletedDate is null
where prb.assignedTo = parm_userID;

if varTotal > 0 then
select concat(prj.projectName,' : ',count(prb.problemID)) as col1,count(prb.problemID*100)/varTotal as col2
from project prj
inner join problemlink plk on prj.projectID = plk.problemLinkID and plk.problemLinkType = 1
inner join problem prb on prb.problemID = plk.problemLinkID and prb.completedDate is null and prb.deletedDate is null
where prb.assignedTo = parm_userID;
end if;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_metric_problem_proj`(IN parm_userID INT)
BEGIN

select org.organisationID as col1,org.organisationName as col2,sum(invl.netTotal) as col3
from userorganisation uorg
inner join organisation org on uorg.organisationID = org.organisationID
inner join project prj on org.organisationID = prj.organisationID
inner join tasklist tkl on prj.projectID = tkl.projectID
inner join task tsk on tkl.taskListID = tsk.taskListID
inner join invoiceline invl on tsk.taskID = invl.taskID
where uorg.userID = parm_userID
group by org.organisationID,org.organisationName;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_metric_problems_project`(IN parm_userID INT)
BEGIN

declare varTotal int;

select count(prb.problemID) into varTotal
from userorganisation uorg
inner join organisation org on uorg.organisationID = org.organisationID
inner join project prj on org.organisationID = prj.organisationID
inner join problemlink plk on prj.projectID = plk.problemLinkID and plk.problemLinkType = 1
inner join problem prb on prb.problemID = plk.problemLinkID and prb.completedDate is null and prb.deletedDate is null
where uorg.userID = parm_userID;

select concat(prj.projectName,' : ',count(prb.problemID)) as col1,count(prb.problemID*100)/varTotal as col2
from userorganisation uorg
inner join organisation org on uorg.organisationID = org.organisationID
inner join project prj on org.organisationID = prj.organisationID
inner join problemlink plk on prj.projectID = plk.problemLinkID and plk.problemLinkType = 1
inner join problem prb on prb.problemID = plk.problemLinkID and prb.completedDate is null and prb.deletedDate is null
where uorg.userID = parm_userID
group by prb.problemID;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_my_overdue_projects`(IN `parm_userID` INT)
BEGIN

select prj.projectID as col1,prj.projectName as col2,prj.projectDescription as col3,
DATE_FORMAT(max(tsk.taskStartDate),'%d-%b-%Y') as col4,
CAST(tsk.taskTimeEstimate as CHAR) as col5
from project prj
join tasklist tkl on tkl.projectID = prj.projectID
join task tsk on tsk.tasklistID = tkl.tasklistID and tsk.taskStatusID not in (7,8,9)
and date_add(tsk.taskStartDate, INTERVAL tsk.taskTimeEstimate DAY) < current_timestamp
where prj.stakeholderID = parm_userID
or prj.projectManagerID = parm_userID
or prj.createdBy = parm_userID
or prj.updatedBy = parm_userID
or tkl.createdBy = parm_userID
or tkl.updatedBy = parm_userID
or tsk.assignedTo = parm_userID
or tsk.createdBy = parm_userID
or tsk.updatedBy = parm_userID
group by prj.projectID;


END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_my_overdue_tasks_proj`(parm_userID int)
BEGIN

select tsk.taskID as col1,tsk.taskDescription as col2,prj.projectName as col3,
DATE_FORMAT(date_add(tsk.taskStartDate,interval tsk.taskTimeEstimate day),'%d %b %Y') as col4
from project prj
join tasklist tkl on tkl.projectID = prj.projectID
join task tsk on tsk.tasklistID = tkl.tasklistID and tsk.taskStatusID not in (7,8,9)
and date_add(tsk.taskStartDate, INTERVAL tsk.taskTimeEstimate DAY) < current_timestamp
where prj.stakeholderID = parm_userID
or prj.projectManagerID = parm_userID
or prj.createdBy = parm_userID
or prj.updatedBy = parm_userID
or tkl.createdBy = parm_userID
or tkl.updatedBy = parm_userID
or tsk.assignedTo = parm_userID
or tsk.createdBy = parm_userID
or tsk.updatedBy = parm_userID;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_my_tasks_complete`(IN parm_userID INT)
BEGIN

select tsk.taskID as col1,tsk.taskDescription as col2,prj.projectName as col3,date_add(tsk.taskStartDate,interval tsk.taskTimeEstimate day) as col4
from project prj
join userproject upr on prj.projectID = upr.projectID
join tasklist tkl on tkl.projectID = prj.projectID
join task tsk on tsk.tasklistID = tkl.tasklistID and tsk.taskStatusID not in (7,8,9)
join users usr on usr.ID = upr.userID and usr.ID = parm_userID
where tsk.assignedTo = parm_userID
and (tsk.taskPercentComplete = 100
or tsk.taskStatusID = 7);

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_overdue_projects`(IN parm_userID INT)
BEGIN

select prj.projectID as col1,prj.projectName as col2,prj.projectDescription as col3,
DATE_FORMAT(max(tsk.taskStartDate),'%d %b %Y') as col4,CAST(tsk.taskTimeEstimate as CHAR) as col5
from project prj
join userproject upr on prj.projectID = upr.projectID
join tasklist tkl on tkl.projectID = prj.projectID
join task tsk on tsk.tasklistID = tkl.tasklistID and tsk.taskStatusID not in (7,8,9)
and date_add(tsk.taskStartDate, INTERVAL tsk.taskTimeEstimate DAY) < current_timestamp
join users usr on usr.ID = upr.userID and usr.ID = parm_userID
group by prj.projectID;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_overdue_tasks_proj`(IN parm_userID INT)
BEGIN

select tsk.taskID as col1,tsk.taskDescription as col2,prj.projectName as col3,
DATE_FORMAT(date_add(tsk.taskStartDate,interval tsk.taskTimeEstimate day),'%d %b %Y') as col4
from project prj
join userproject upr on prj.projectID = upr.projectID
join tasklist tkl on tkl.projectID = prj.projectID
join task tsk on tsk.tasklistID = tkl.tasklistID and tsk.taskStatusID not in (7,8,9)
and date_add(tsk.taskStartDate, INTERVAL tsk.taskTimeEstimate DAY) < current_timestamp
join users usr on usr.ID = upr.userID and usr.ID = parm_userID;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_project_time`(IN `parm_userID` INT)
BEGIN

select 	prj.projectID,
		prj.projectName,
        sum(tim.hours)
        from project prj
        inner join tasklist tkl on prj.projectID = tkl.projectID
        inner join task tsk on tsk.taskListID = tsk.taskListID
        inner join time tim on tim.taskID = tsk.taskID
        where prj.deletedDate is null
        group by prj.projectID;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_report_vip`(IN parm_userID INT)
BEGIN

select prj.projectID as col1,usr.username as col2,prj.projectname as col3,lk.lookupvaluechar as col4
from users usr join userproject upr on usr.ID = upr.userID
join project prj on prj.projectID = upr.projectID 
join opinion opn on opn.userID = usr.id and opn.itemID = prj.projectID 
join lookup lk on lk.lookupsubtypeid = opn.opiniontype where lk.lookuptypeid = 20;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_select_problem_assignees`(IN parm_userID INT)
BEGIN
    select distinct
        `us`.`first_name` AS `first_name`,
        `us`.`last_name` AS `last_name`,
        `uo`.`userID` AS `userid`,
        `pr`.`problemID` AS `problemID`
    from
        ((`userorganisation` `uo`
        join `users` `us` ON ((`us`.`id` = `uo`.`userID`)))
        join `problem` `pr` ON ((`pr`.`organisationID` = `uo`.`organisationID`)));
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_select_project_index_sidebar`(IN `parm_userID` INT)
BEGIN

select 'New projects' as projectName,'' as column2,'' as id, 0 as column4
union
SELECT distinct proj.projectName, proj.createdDate,proj.projectID,3
from project proj join userproject upr on proj.projectID = upr.projectID
where proj.createdDate > fn_past_date(-10)
and upr.userID = parm_userID
union
select 'Changed projects','' as column2,'' as id, 5
union
SELECT proj.projectName, proj.updatedDate,proj.projectID, 7
from project proj join userproject upr on proj.projectID = upr.projectID
where proj.updatedDate > fn_past_date(-10)
and upr.userID = parm_userID
union
select 'New users','' as column2,'' as id, 9
union
SELECT proj.projectName, usr.username,proj.projectID, 11
from project proj left join userproject upr on proj.projectID = upr.projectID
join users usr on upr.userID = usr.id
where usr.created_on > fn_past_date(-10)
and usr.id = parm_userID
and proj.projectID in (select projectID from userproject where userid = parm_userID)
union
select 'New tasklists','' as column2,'' as id, 13
union
SELECT proj.projectName,tsk.taskListName,proj.projectID, 15
from project proj join userproject upr on proj.projectID = upr.projectID
join tasklist tsk on tsk.projectID = proj.projectID
where tsk.createdDate > fn_past_date(-10)
and upr.userID = parm_userID
order by 4,1,2
limit 40;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_select_task_links`(in parm_taskID int, in parm_taskListID int)
BEGIN

    select distinct
        `tk`.`taskID` AS `taskID`,
        concat(left(`tk`.`taskDescription`, 30), '...') AS `taskDescription`
    from
        `task` `tk`
        join `tasklist` `tkl` ON `tk`.`taskListID` = `tkl`.`taskListID`
        join `project` `pr` ON `tkl`.`projectID` = `pr`.`projectID`
    where
        isnull(`pr`.`deletedDate`)
            and isnull(`tkl`.`deletedDate`)
            and isnull(`tk`.`deletedDate`)
			and pr.projectID in 
        (select pri.projectID 
		from `task` `tki`
        join `tasklist` `tkli` ON `tki`.`taskListID` = `tkli`.`taskListID`
        join `project` `pri` ON `tkli`.`projectID` = `pri`.`projectID`
		where tki.taskID = parm_taskID or tki.taskListID = parm_taskListID)
	order by tk.taskID;

END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sr_selectGanttData`(IN `parm_projectID` INT)
BEGIN



select pro.projectID, pro.projectName, tsk.taskDescription as 'name', tsk.taskDescription as 'desc', tsk.createdDate + 0 as 'from', 

tsk.createdDate + 1000000 as 'to'

from project pro left join tasklist tkl on pro.projectID = tkl.projectID

right join task tsk on tsk.taskListID = tkl.taskListID

where pro.projectID = parm_projectID;



END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `temp_update_users`()
BEGIN


DECLARE CclientID int;
declare CorganisationID int;
declare Cid mediumint;
DECLARE no_more_rows BOOLEAN;

DECLARE mycursor CURSOR FOR
select id, org.clientID, organisationID
from organisation org
join users usr on usr.company = org.organisationID;

DECLARE CONTINUE HANDLER FOR NOT FOUND
	SET no_more_rows = TRUE;

open mycursor;

the_loop: LOOP

	fetch mycursor into Cid, CclientID, CorganisationID;

	IF no_more_rows THEN
	CLOSE mycursor;
	LEAVE the_loop;
    END IF;

	update users
	set clientID = CclientID
	where id = Cid;

END LOOP the_loop;


END$$
DELIMITER ;
