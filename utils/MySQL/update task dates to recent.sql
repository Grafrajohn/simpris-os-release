SET SQL_SAFE_UPDATES = 0;
update task
set taskstartdate = now() - interval 30 day
where taskstartdate < now() - interval 30 day
and createdby = 4
and deleteddate is null;
SET SQL_SAFE_UPDATES = 1;

SET SQL_SAFE_UPDATES = 0;
update task
set taskstartdate = now() - interval 45 day
where taskstartdate is null
    and createdby = 4
and deleteddate is null;
SET SQL_SAFE_UPDATES = 1;

SET SQL_SAFE_UPDATES = 0;
update task 
set tasktimeestimate = MOD(taskID, 10) + 2
where tasktimeestimate is null
and createdby = 4;
SET SQL_SAFE_UPDATES = 1;