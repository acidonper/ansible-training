# Ansible Handlers

Ansible Handlers manage specific procedure situations when a tasks have been applied. This lesson implements some examples about this aspect.

In order to understand this lesson properly, a set of steps have been designed to be implemented in the following section.

**ENJOY !!!**

## Resources

In order to assist this laboratory implementation, a set of resources have been added:

-   httpd.conf (Default Apache configuration file in Red Hat Enterprise Linux 8)

## Steps 

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Modify apache configuration file named "httpd.conf" in order to enable php index and listen in port 80 and 81
-   Create a file named "index.php" with phpinfo() function included
-   Create a playbook named "handlers-playbook.yml" using "myinstance" as a hosts parameter and ``<studentxx>`` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Implement a block with the following tasks:
        -   Install "apache" and "php" packages (\*Please use loop)
    -   If any of previous tasks fail, implement the the following tasks:
        -   Install "httpd" and "php" packages (\*Please use loop)
    -   Anyway, the following tasks have to be executed:
        -   Create a new folder "php" in "/var/www/html"
        -   Copy apache configuration file named "httpd.conf" to "/etc/httpd/conf/httpd.conf"
        -   Copy php file named "index.php" to "/var/www/html/php"
    -   NOTE: It is important to bear in mind that it is necessary restart httpd service when a new package or package version is installed or configuration file modified# Ansible Handlers
-   Before running your playbook, run the ansible-playbook --syntax-check  command to verify that its syntax is correct
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
-   https://httpd.apache.org/docs/2.4/configuring.html
-   https://docs.ansible.com/ansible/latest/modules/copy_module.html
  
License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
 