# This is python web application that uses uWSGI

### Before using
Make sure to check that you have MySQL installed on your machine, if not: ```sudo apt-get install python3-dev``` and
```sudo apt-get install python3-dev libmysqlclient-dev```
### Than, create DB
DB creation http://www.mysqltutorial.org/mysql-create-database/.
And if you want to change user and password of mysql https://www.cyberciti.biz/faq/mysql-change-user-password/.

### Create .env file and enter these variables.

|Variables          |Description                            |Value                                                   |
|-------------------|--------------------------------       |--------------------------------------------------------|
|user               |User of your Mysql DB(on local machine)|'your-user'                                             |
|password           |PW of your Mysql DB(on local machine)  |'your-password'                                         |
|server             |Your server *USE THIS VALUE ->         |127.0.0.1 or 'localhost'                                | 
|database           |Your DB name                           |'your-db-name'                                          |
|sender_email       |Email sender *USE THIS VALUE ->        |'vdconvertermp3@gmail.com'                              |
|receiver_email     |Your email                             |'your-email'                                            |
|password           |Password of email  *USE THIS VALUE ->  |'videoconverter123'                                     |

### Create virtual env file by ```python3 -m venev .venv``` than install all dependecies by ```pip install -r requirements.txt```

### To launch app using uWSGI  ```uwsgi --http :9090 --wsgi-file app.py```
### Than launch celery from same directory on another terminal by ```celery -A tasks worker --loglevel=info```
