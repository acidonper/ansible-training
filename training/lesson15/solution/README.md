# Ansible Lookups, Callbacks & Tags

## Run tags-playbook.yml with tag debug!

```
$ ansible-playbook -i inventory tags-playbook.yml -t debug -k -K
```

## Run tags-playbook.yml with tag user!

```
$ ansible-playbook -i inventory tags-playbook.yml -t user -k -K
```

## Run tags-playbook.yml with tag apache!

```
$ ansible-playbook -i inventory tags-playbook.yml -t apache -k -K
```

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
-   https://docs.ansible.com/ansible/latest/plugins/plugins.html

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com