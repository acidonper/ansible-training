# Ansible Templates

Ansible Templates are a powerful tool which allows custom files can be generated based on variables. This lesson implements some examples about their implementation.

In order to understand this lesson properly, a set of steps have been designed to be implemented in the following section.

**ENJOY !!!**

## Resources

In order to assist this laboratory implementation, a set of resources have been added:

-   httpd.conf (Default Apache configuration file in Red Hat Enterprise Linux 8)
-   index.html (Basic HTML document structure)

## Steps 

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Create a playbook named "templates-playbook.yml" using "myinstance" as a hosts parameter and ``<studentxx>`` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Define an array variable named "http_ports" which contains the following sequence of ports (80, 81, 8008, 8009 and 9000)
    -   Create a template from "httpd.conf" configuration file in order to listen ports defined in "http_ports variable" and create a virtualhost per each <port> using as root directory
    -   Create a template from "index.html" file in order to include port number as body content corresponding to the virtual host port
    -   Install "httpd" package
    -   Create new folders based on port number (Example: "ansible-service-``<port>``") in "/var/www/html"
    -   Copy HTML template page named "index.html.j2" in each "/var/www/html/ansible-service-``<port>``"
    -   Copy apache configuration template named "httpd.conf.j2" to "/etc/httpd/conf/httpd.conf"
    -   NOTE: It is important to bear in mind that it is necessary restart httpd service when a new package or package version is installed or configuration file modified
-   Before running your playbook, run the ansible-playbook --syntax-check  command to verify that its syntax is correct
-   Run the playbook!
-   Test the apache server

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
-   https://docs.ansible.com/ansible/latest/modules/template_module.html
-   https://jinja.palletsprojects.com/en/2.10.x/
  
License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
 