#!/usr/bin/python

#mssql connections string 
odbcConString = 'DRIVER={FreeTDS}; SERVER=db.com; DATABASE=dbName; UID=username; PWD=password'

#mysql connections info
MYSQL_host="domain.com"
MYSQL_user="username"
MYSQL_passwd="password"
MYSQL_db="dbtoselect"

#tables to retrieve and recreate
list_of_tables = [['original_name', 'new_name_or_same']]
