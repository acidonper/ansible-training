# Ansible Facts

## Goals

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Create a playbook named "facts-playbook.yml" using "myinstance" as a hosts parameter and ``<studentxx>`` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    - Create a folder /named "etc/ansible/facts.d"
    - Create a custom facts "/etc/ansible/facts.d/custom.fact" file with a variable named "haproxy_ip" which includes instance ip
    - Debug local facts "haproxy_ip"
    - Create a new variable named "life_variable" with date content
    - Debug variable "life_variable"
-   Before running your playbook, run the ansible-playbook --syntax-check site.yml command to verify that its syntax is correct
-   Run the playbook!

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
-   https://docs.ansible.com/ansible/latest/modules/set_fact_module.html
-   https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html