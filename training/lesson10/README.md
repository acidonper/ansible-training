# Ansible Handlers

## Goals

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Create a playbook named "tools-playbook.yml". The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Install httpd and php package (*Please use loop)
    -   Create a new folder "php" in "/var/www/html"
    -   Create a new file "index.php" in "/var/www/html/php" with a PHP hello world content
    -   Create a new apache configuration file in order to implement a new VirtualHost which listen in port 81 and has "/var/www/html/php" as root directory 
    -   Restart httpd service if the configuration file change
-   Before running your playbook, run the ansible-playbook --syntax-check site.yml command to verify that its syntax is correct
-   Run the playbook!
-   Test the apache server
-   Modify the content of the configuration file to listen in port 82
-   Run the playbook!
-   Test the apache server

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
-   https://docs.ansible.com/ansible/latest/modules/copy_module.html



