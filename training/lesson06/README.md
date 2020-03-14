# Ansible Variables

Ansible Variables are an important element as they are in other programming languages. This lesson tries to implement the most common scenarios implemented in a day to day Ansible procedures.

In order to understand this lesson properly, a set of steps have been designed to be implemented in the following section.

**ENJOY !!!**

## Steps 

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Create a group variables file named "myinstance.yml" in a new folder named "group_vars" with the folowwing variables:
    -   String variable called "test_string" with random content
    -   Array variable called "test_array" with a number sequence from 0 to 5
    -   Dictionary varible called "test_dic" with 2 employees definition (name, id and age)
-   Crate a variables file named "vars.yml" in a new folder named "vars" with the folowwing variables:
    -   String variable called "test_string" with random content (*Important: It has to be different from test_string in myinstance.yml)
-   Create a playbook named "playbook-variables.yml" using "myinstance" as a hosts parameter and ``<studentxx>`` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Print test_string variable (*Identify which one is printed)
    -   Print test_array variable
    -   Print test_dic variable
    -   Print the list of sources used as inventory
    -   Print the connection plugin actually used for the task on the target host
    -   Print Ansible facts
-   Before running your playbook, run the ansible-playbook --syntax-check  command to verify that its syntax is correct
-   Run the playbook!
-   Import "vars.yml" file into the playbook
-   Before running your playbook, run the ansible-playbook --syntax-check  command to verify that its syntax is correct
-   Run the playbook!

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
