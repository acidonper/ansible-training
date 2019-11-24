# Ansible Inventory

## Goals

Create an Ansible inventory with the following requisites:

* 3 groups (north, south, west and east)
* Each group has to contains a couple of devices (Example: **north** has student01 and student02, **south** has student03 and student04, ...)
* Create a super group **laboratory** with all other groups included
* Define an ansible var **zone** with the group name in each group
* Check inventory file structure is correct and graphs it 

## Useful Links

For more information, please visit:

* https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory
* https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html