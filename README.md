# This is python web applicatio using uWSGI interface


### Create .env file at settings.py level and enter these variables.

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
