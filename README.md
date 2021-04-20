# LoginSistemWithMySQL
This is a Login and Registering system project using MySQL database and docker for a local server.
  # Requirements
  - Docker
  - MySQL
  - PyQt5
  - A email for using the code sender
  
  # How to run
  First, you will have to create a SQL Database.<br>
  You can use any DB manager like MySQL workbench or DBeaver and Docker.
  
  - <b>How to create the DB (with Docker):</b><br>
    There is a dir named "Create_MySQL_Usuarios_DB",<br>
    when you open, there will be the docker-compose file and<br>
    "users_login_table.sql".<br>
    If you are running your docker in a linux system, open the docker-compose file<br>
    and change the "\" for "/":
      > volumes:<br> 
      >   -- .\MySQL_Docker\Container:/var/lib/mysql
      
    Then Open your terminal inside the paste and run this command:
      > docker-compose up
      
    Now you have created your SQL container in docker with the database "users".
  
  - <b>How to create the table:</b><br>
    You can open the script "users_login_table.sql" with your<br>
    DB manager and run it or you can copy the code, open a new script<br>
    in the manager, paste the code and run it, then it will generate<br>
    the table with all the constraints.
    
    ...
    
    
