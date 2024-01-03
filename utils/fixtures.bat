cd C:\source\simpris
rem c:\python\python.exe manage.py dumpdata auth.User --format=json > simpris/fixtures/User.json
rem c:\python\python.exe manage.py dumpdata simpris.VUserContextFull --format=json > simpris/fixtures/vusercontextfull.json
rem c:\python\python.exe manage.py dumpdata --format=json > simpris/fixtures/initial_data.json
c:\python\python.exe manage.py dumpdata simpris.VSearch > c:\source\simpris\simpris\fixtures\vsearch.json
pause