select usr.id as 'user id',usr.username,grp.id as 'group id',grp.name as 'group name',
grpu.id as 'auth_user_groups',grpp.id as 'auth_group_permissions',
perm.name,perm.codename
from auth_user usr
left join auth_user_groups grpu on usr.id = grpu.user_id
left join auth_group grp on grpu.group_id = grp.id
left join auth_group_permissions grpp on grp.id = grpp.group_id
left join auth_permission perm on grpp.permission_id = perm.id
order by usr.id;

select app_label, model, name, codename
from django_content_type cont
inner join auth_permission perm on cont.id = perm.content_type_id