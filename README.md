# Simpris Open Source

Released for Simpris under the GNU license.

## Python Django MySQL Project Management System

Simpris is a general purpose project management system which is designed to be used to manage many different types of projects. Over the years Simpris has groen into a multifaceted project with the following technologies:

## How to set up Simpris

This readme assumes you have advanced Django knowledge, an understanding of MySQL databases and knowledge of a Python/Django operating system. If you don't you will find it ectremely difficult to deploy and run Django.

GoodlyCode can set up Django for you but this would be a busniess proposition.

### 1. Create database

- Create a MySQL database called simpris or similar
- Either:
    - Run Django migrations against the database objects
- Or:
  - From the scripts in the Database-Objects-MySQL folder
    - Build the tables 
    - Build the views
    - Build the stored procedures
    - Build the functions

### 2. Populate the lookup tables

Use MySQL Workbench or similar to import data from files in the DataLoad folder:
- lookup-type.csv
- lookup.csv
 
### 3. Create Django superuser

If not already done create the Django superuser in the normal way

### 4. Set up the Simpris dependencies in the Django configuration files

- Configure SendGrid email provider
- Configure MySQL database connection
- Configure Google Recaptcha

### 5. Deploy the Django code

Deploy Django in the usual way.

### 6. Start managing your projects!

## Simpris Technical Information

*Updated by Graham 29/11/2023*

### Technologies

#### Front End / GUI

Bootstrap v3 and v5
Javascript
CSS
SASS
Webpack
JQuery
React
VueJS
JQuery DataTables
Python Dhango Templates

#### Back End / Business Logic

Python Django v4
Python v3
Python Django Rest Framework API

#### Data / Database

Python Django Models
MySQL Database

There is an early stage branch for use with PostGres.

#### Infrastructure

Simpris will run on any OS which supports Django

Thre is also a Docker version included

#### IDEs

This project has been run by:

Visual Studio Code - works fine 6/05/2023 - make sure you open the workspace 'simpris-code-workspace'
Eclipse PyDev - works fine 5/12/2021
Visual Studio - bindings included for VS
PyCharm - developed with this and bindings still remain

##### Eclipse Setup

Install Java version of Eclipse
Install PyDev from Eclipse Marketplace

#### Source Control

GitHub URL: https://github.com/user-name/simpris

#### 3rd party dependencies

Sendgrid account required for email, unless you want to change the email logic
Google captcha required to authenticate logins

### Django Setup and Configuration

Python 3.11
Run "pip install -r requirements.txt" in Simpris root directory to get all the required components

Make sure that settings\__init__.py is set correctly for the platform e.g. linux, mac, pc etc
Something like:

\>>>

\# this file controls settings for various environments

\# always import from common
from .common import *

\# choose as per platform:
\#from .live_linux import *
\#from .dev_mac import *
from .dev_pc import *
\#from .docker import * 

SECRET_KEY = 'your-secret-key'

\##### OTHER SECRETS
EMAIL_HOST_PASSWORD = 'sendgrid-password'

WSGI_APPLICATION = 'simpris.wsgi.application'

<<<

Either install MySQL locally or point to your remote MySQL dB

### Theme

As of 5/12/2021 the theme is the bootstrap5 theme in theme\theme-bootstrap-5
In order to change the styles go into the above folder and run npm insdtall if you have not already. Then npm run builds builds the theme from the scss. After building copy the styles.css to static\css\theme\styles.
Debugging 'inspect' in Google Chrome will show you the scss where the problem lies so you can go in and change the scss file thenm rebuild. 

### Docker Tips

to find a file on server use command docker locate [file name] e.g. docker locate docker-compose.yml

#### Docker local

Inside the simpris proj folder run:

'docker-compose up' from within project folder builds and runs the app
'docker-compose up --build' builds the containers first

This will allow you to override what is in docker-compose.yml with what is in the file after -f:

docker-compose -f docker-compose-dev.yml up --build

.dockerignore same function as git ignore

Make sure that the settings __init.py__ command points to docker.py or the app will not be able to access the static files.

For dev docker the docker-compose.yml env_file points at docker-dev.env

#### Docker staging

First build the image with the docker-compose-staging env pointing at docker-staging.env

Make sure settings __init.py__ points at docker.docker images

#### Pushing to Docker Hub

Make sure image has been built first. From inside app/docker folder:

docker build .

When a new image is made make sure it is tagged using the command:

docker tag [image id] [docker registry name]

To get the image id run: docker images 
The above command list all images in a docker repository including your local one