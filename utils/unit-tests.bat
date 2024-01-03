cd C:\source\simpris
rem c:\python\python.exe manage.py makemigrations simpris
c:\python\python.exe manage.py test simpris.tests-unit.test_app --settings=simpris.settings_test
c:\python\python.exe manage.py test simpris.tests-unit.test_organisation --settings=simpris.settings_test --verbosity=2 
pause