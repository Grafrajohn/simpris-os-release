INSERT INTO `simpricity`.`auth_group`
(`id`,
`name`)
select id,
name
from groups;

INSERT INTO `simpricity`.`auth_user_groups`
(`id`,
`user_id`,
`group_id`)
select id,
user_id,
group_id from users_groups ug
where ug.user_id in (select id from auth_user)
