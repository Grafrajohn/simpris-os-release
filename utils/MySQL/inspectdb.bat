rem make sure the db/id in settings.py is set correctly for the db - server host of 127.0.0.1 seems to work
rem this script refreshes the models from the dB so run it after changes to the MySQL dB 

cd C:\source\simpris
c:\python\python.exe manage.py inspectdb > simpris\models.py
pause