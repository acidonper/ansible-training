# Ansible Playbooks

## Goals

* Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
* Create a playbook named playbook.yml. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
  * Debug "It is working" message on group "myinstance"
  * Print instance settings on group "myinstance"
  * Create a new user "testplay01" on group "myinstance" using become (root)
  * Install package "httpd" on group "myinstance" using become (root)
  * Enable and up "httpd" service on group "myinstance" using become (root)

## Useful Links

For more information, please visit:

* https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
* https://docs.ansible.com/ansible/latest/modules/modules_by_category.html