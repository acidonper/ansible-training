# Ansible Conditionals, loops and delegation

## Goals

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Create a playbook named "tools-playbook.yml" using "myinstance" as a hosts parameter and ``<studentxx>`` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
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
    -   Import "usertable.mysql" table file into "mysql_db" database delegating the operation to <mysql_client_ip> instance 
-   Before running your playbook, run the ansible-playbook --syntax-check site.yml command to verify that its syntax is correct
-   Run the playbook!
-   Test the database

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_delegation.html
