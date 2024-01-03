SELECT table_name as obj_name, table_type as obj_type, engine as db_engine, table_rows as no_rows, create_time as created, update_time as updated FROM INFORMATION_SCHEMA.TABLES
where table_schema = 'simpricity'
union
SELECT routine_name, routine_type,null,null,created,last_altered FROM INFORMATION_SCHEMA.ROUTINES
order by updated desc,created desc
