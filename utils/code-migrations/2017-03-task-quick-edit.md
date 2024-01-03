Summary
=======
Task quick edit

Functionality to test
---------------------
Task quick edit from task list page task/list.
------------------------------------------------------------
DJANGO
------
urls.py - add new routes to api

SERIALIZERS

API
lookup\*.py

APPS
task\views.py

MODELS

TEMPLATES
task\tasklist.html
task\_task_quick_edit.html
task\edit.html

-------------------------------------------------------------
FILES
-----
xxxxxxxx

PERMISSIONS

------------------------------------------------------------
MYSQL
-----                                                      
Lookup - add id column
Lookup - correct dates in createddate - those set to all 00000s
Lookup - remove existing primary key
Lookup - make id primary key with auto increment
Lookup - create unique IX on client/lookuptype/lookupsubtype
delete 3 indexes
create new primary key index
create new composite unique index not primary
------------------------------------------------------------
STATIC
------

Javascript
----------
task\task_quick_edit.js
HTML
----
_task_edit_quick.html

-------------------------------------------------------------
Notes
-----
xxxxxx

-------------------------------------------------------------
Checklist
---------
1. Changes to urls.py?
2. Changes to archive tables?
3. Changes to models.py?