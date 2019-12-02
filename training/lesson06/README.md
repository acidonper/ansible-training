# Ansible Variables

## Goals

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Create a variables group file named "myinstance.yml" in a new folder named "group_vars" with the folowwing variables:
    -   String variable called "test_string" with random content
    -   Array variable called "test_array" with a number sequence from 0 to 5
    -   Dictionary varible called "test_dic" with 2 employees definition (name, id and age)
-   Crate a variables file named "vars.yml" in a new folder named "vars" with the folowwing variables:
    -   String variable called "test_string" with random content (*Important: It has to be different from test_string in myinstance.yml)
-   Create a playbook named playbook-variables.yml. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Debug test_string variable (*Identify which one is printed)
    -   Debug test_array variable
    -   Debug test_dic variable
    -   Debug the list of sources used as inventory
    -   Debug the connection plugin actually used for the task on the target host
    -   Debug Ansible facts
-   Before running your playbook, run the ansible-playbook --syntax-check site.yml command to verify that its syntax is correct
-   Run the playbook!

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
