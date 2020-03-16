# Ansible Handlers and Blocks

Ansible Handlers manage specific procedure situations when a tasks have been applied. This lesson implements some examples about this aspect.

Blocks allow for logical grouping of tasks and in play error handling in a way similar to exceptions in most programming languages. Blocks only deal with ‘failed’ status of a task. A bad task definition or an unreachable host are not ‘rescuable’ errors.

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
        -   Install "apache2" package
    -   If any of the previous tasks fail, implement the following tasks:
        -   Install "httpd" package
    -   In any case, the following tasks need to be executed under the block:
        -   Copy httpd configuration file named "httpd.conf" to "/etc/httpd/conf/httpd.conf"
        -   Install "php" package
        -   Create a new folder "php" in "/var/www/html"
        -   Copy php file named "index.php" to "/var/www/html/php"
    -   NOTE: It is important to bear in mind that it is necessary to restart httpd service when a new package or package version is installed or configuration file modified
-   Before running your playbook, run the ansible-playbook --syntax-check  command to verify that its syntax is correct
-   Run the playbook!
-   Test the apache server
-   Modify the content of the configuration file to listen in port 82
-   Run the playbook!
-   Test the apache server

## Notes

Package name differences betwen distributions are usually handled using conditionals and the facts provided by the machine. In this lesson we use blocks instead for demonstrative purposes.

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
-   https://httpd.apache.org/docs/2.4/configuring.html
-   https://docs.ansible.com/ansible/latest/modules/copy_module.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html
  
License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
 