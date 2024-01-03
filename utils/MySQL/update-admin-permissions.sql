SET SQL_SAFE_UPDATES = 0;

UPDATE auth_user a
JOIN users_groups b ON a.id = b.user_id
SET a.is_superuser = 1
WHERE a.is_superuser = 0
AND b.group_id = 1;

UPDATE auth_user a
JOIN users_groups b ON a.id = b.user_id
SET a.is_staff = 1
WHERE a.is_staff = 0
AND b.group_id = 2;

SET SQL_SAFE_UPDATES = 1;
