# Ansible AdHoc Commands

## Goals

* Debug "It is working" message on localhost
* Print instance settings on localhost
* Create a new user "yourname" on localhost using become (root)
* Include the new user "yourname" on **wheel** group on localhost using become (root)
* Copy sudo file **/etc/passwd** on localhost using become "yourname" and setting permissions 440 and owner root in **/tmp/newfile**

## Useful Links

For more information, please visit:

* https://docs.ansible.com/ansible/latest/cli/ansible.html
* https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
