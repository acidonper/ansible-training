# Ansible Conditionals, loops and delegate

## Goals

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Create a playbook named "tools-playbook.yml". The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Define the following variables:
        -   User name variable named "mysql_name" with "testuser01"
        -   User pass variable named "mysql_pass" with "testuser01"
        -   User pass variable named "mysql_db" with "testdb01"
        -   Client IP variable named "mysql_client_ip" with <ip_classroom_instance>
        -   List or Array of packages named "mysql_packages" with "mysql-server" and "python3-PyMySQL" included
    -   Install the list of packages
    -   Start mysqld service if installation packages has changed 
    -   Restart mysqld service if installation packages has not changed
    -   Create a new mysql database using "mysql_db" variable
    -   Create a new user using "mysql_name" and "mysql_pass" variables with read/write rights to "mysql_db" database from host "mysql_client_ip"
    -   Import "usertable.mysql" table into "mysql_db" database delegating to mysql_client_ip instance the operation
-   Before running your playbook, run the ansible-playbook --syntax-check site.yml command to verify that its syntax is correct
-   Run the playbook!
-   Test the database

## Useful Links

For more information, please visit:

-   https://stackoverflow.com/questions/29179856/create-mysql-tables-with-ansible
