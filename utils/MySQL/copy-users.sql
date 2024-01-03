INSERT INTO `simpricity`.`auth_user`
(`id`,
`password`,
`last_login`,
`is_superuser`,
`username`,
`first_name`,
`last_name`,
`email`,
`is_staff`,
`is_active`,
`date_joined`)
Select id,
password,
from_unixtime(last_login),
0,
username,
first_name,
last_name,
email,
0,
active,
from_unixtime(created_on)
from users
where id not in (select id from auth_user)