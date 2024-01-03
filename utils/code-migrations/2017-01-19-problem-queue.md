Summary
=======
Add queue to problem

==============================================================================================
Functionality to test
---------------------
Problems can be added to queues
Problem queue can be edited
Problen queue can be viewed

==============================================================================================
>>DJANGO<<
----------

SERIALIZERS

API
problem\*.*

APPS
problem\*.*
project\views.py

MODELS
v_problems
v_problem_edit

TEMPLATES
problem\*.*
project\*.*

FILES
-----
urls.py

PERMISSIONS

=============================================================================================
>>MYSQL<<
--------- 
problem table - add queueID
problem_archive - add queueid
v_problems  - add queueID
v_problem_edit

=============================================================================================
>>STATIC<<
----------

Javascript
----------
problem.js

HTML
----


============================================================================================
Notes
-----
xxxxxx

Checklist
---------
1. Changes to urls.py?
2. Changes to archive tables?
3. Changes to models.py?