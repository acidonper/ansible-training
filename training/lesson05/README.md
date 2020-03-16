# Ansible Playbooks

Ansible Playbook is the Ansible way to execute multiples tasks in a simple execution. This lesson explores Ansible Playbooks and their main aspects.

In order to understand this lesson properly, a set of steps have been designed to be implemented in the following section.

**ENJOY !!!**

## Steps 

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Create a playbook named playbook.yml, using "myinstance" as a hosts parameter and ``<studentxx>`` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Print "It is working" message on group "myinstance"
    -   Print instance settings on group "myinstance"
    -   Create a new user "testplay01" on group "myinstance" using become (root)
    -   Install package "httpd" on group "myinstance" using become (root)
    -   Enable and up "httpd" service on group "myinstance" using become (root)
-   Before running your playbook, run the ansible-playbook --syntax-check  command to verify that its syntax is correct
-   Run the playbook and verify results via curl http://localhost

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/modules/modules_by_category.html

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
 