# Ansible Playbooks

## Goals

* Create an inventory file with a group named "myinstance" and your internal instance IP assigned included
* Debug "It is working" message on group "myinstance" with ec2-user
* Print instance settings on group "myinstance" 
* Create a new user "testplay01" on group "myinstance" using become (root)
* Install package "httpd" on group "myinstance" using become (root)
* Enable and up "httpd" service on group "myinstance" using become (root)

## Useful Links

For more information, please visit:

* https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
* https://docs.ansible.com/ansible/latest/modules/modules_by_category.html