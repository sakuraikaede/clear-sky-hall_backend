# The Backend of Clear Sky Hall Website
Related repo:[sakuraikaede/clear-sky-hall](https://github.com/sakuraikaede/clear-sky-hall)  
The backend for Clear Sky Hall Website (in plan)

## Requirements
+ Python3  
+ A MySQL server  
+ Python Packages:flask,PyMySQL  

## Setting
You have to import "csh.sql" in MySQL.  
You need to modify the "settings.json". This is the meaning of the keys in this JSON file.  

|  Key   | Meaning                                                    |
|  ----  | ---------------------------------------------------------- |
| ip     | The hostname of the MySQL server                           |
| port   | The port of the MySQL server                               |
| dbname | The database name for backend, default is "clear_sky_hall" |
| user   | The username of the MySQL server                           |
| passwd | The password of the MySQL server                           |
| table  | The table for backend                                      |  
  
## Run

Then, let's run!  
`python myApp.py`  
If you need to run it in a production environment, maybe you need to use a WSGI container.
