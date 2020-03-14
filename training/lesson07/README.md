# Ansible Facts

Ansible Facts contain useful information during playbooks executions in order to take some decision or use them based on this information. On the other hand, it is a powerful tool to collect some extra information about the nodes which are beeing managed by Ansible.

In order to understand this lesson properly, a set of steps have been designed to be implemented in the following section.

**ENJOY !!!**

## Steps 

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Create a playbook named "facts-playbook.yml" using "myinstance" as a hosts parameter and ``<studentxx>`` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    - Create a folder /named "etc/ansible/facts.d"
    - Create a custom facts "/etc/ansible/facts.d/custom.fact" file with a variable named "haproxy_ip" which includes instance ip
    - Print local facts "haproxy_ip"
    - Create a new variable named "life_variable" with date content
    - Print variable "life_variable"
-   Before running your playbook, run the ansible-playbook --syntax-check  command to verify that its syntax is correct
-   Run the playbook!

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
-   https://docs.ansible.com/ansible/latest/modules/set_fact_module.html
-   https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
 