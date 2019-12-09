# Ansible Roles

Ansible Roles lesson is one of the most important lesson in this training. It is important take the time required in order to understand how system roles work and how ansible galaxy repository helps users to accelerate ansible procedures implementation.

In order to understand this lesson properly, a set of steps have been designed to be implemented in the following section.

**ENJOY !!!**

## Steps 

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Search and Install Nginx official role located on Ansible Galaxy
-   Install rhel-system-roles
-   Create a folder named "roles" to locate custom roles
-   Create a custom role named "mariadb" which has to implement the following tasks:
    -   Install mariadb-server package
    -   Start and Enable mysqld service
    -   Create databases defined in "mysql_datases" (*At least "testroles01" by default)
    -   Include a tasks file named "create_mariadb_user.yml" located in tasks folder. It is necessary import this file as often as the number of users defined in an array variable named "mysql_users" (*At least "test01" by default). Regarding this tasks file, it has to perform the following tasks:
        -   Create a database named "``<user_name``"
        -   Create user with user name and password using ``<user_name>``, rights to "testroles01" and ``<user_name>`` databases from `<myinstance_ip>`
-   Create a playbook named "roles-playbook.yml" using "myinstance" as a hosts parameter and `<studentxx>` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Execute custom role named "mariadb" with an array var named "mysql_users" which locates the following users: test01, test02, test03
    -   Execute nginx galaxy role 
    -   Execute timesync rhel-system-role in order to configure "time.google.com" as NTP server 
-     Before running your playbook, run the ansible-playbook --syntax-check  command to verify that its syntax is correct
-     Run the playbook!
-     Test

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html
-   https://docs.ansible.com/ansible/latest/modules/import_tasks_module.html
-   https://galaxy.ansible.com

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com