# Ansible Lookups, Callbacks & Tags

Lookup plugins allow Ansible to access data from outside sources. This can include reading the lesystem in addition to contacting external datastores and services. Like all templating, these plugins are evaluated on the Ansible control machine, not on the target/remote.

Callback plugins enable adding new behaviors to Ansible when responding to events. By default, callback plugins control most of the output you see when running the command line programs, but can also be used to add additional output, integrate with other tools and marshall the events to a storage backend.

Finally, Tags allow Ansible users to execute specific parts of code. Tags can be defined at playbook, role and task level.

In order to understand this lesson properly, a set of steps have been designed to be implemented in the following section.

**ENJOY !!!**

## Resources

In order to assist this laboratory implementation, a set of resources have been added:

-   dictionary.json
-   tags-playbook-template.yml

## Steps

### lookup

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Create a playbook named "lookup-playbook.yml" using "myinstance" as a hosts parameter and `<studentxx>` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Create a variable named "test_dict" with dictionaryyyy.json file content (if file does not exist display a warning)
    -   Create a variable named "dict_content" with dictionary.json file content and parse to an Ansible dictionary (if file does not exist display a warning)
    -   Display "test_dict" variable
    -   Display "dict_content" variable
-   Before running your playbook, run the ansible-playbook --syntax-check site.yml command to verify that its syntax is correct
-   Run lookup-playbook.yml!

## tags

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Copy playbook named "tags-playbook-template.yml" into "tags-playbook.yml" using "myinstance" as a hosts parameter and `<studentxx>` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Tag tasks 1 and 2 as "debug" 
    -   Tag task 3 as "user"
    -   Tag tasks 4 and 5 as "apache"
-   Before running your playbook, run the ansible-playbook --syntax-check site.yml command to verify that its syntax is correct
-   Run tags-playbook.yml with tag debug!
-   Run tags-playbook.yml with tag user!
-   Run tags-playbook.yml with tag apache!

### callbacks

-   Define "dense" callback in ansible.cfg
-   Run lookup-playbook.yml!
-   Run tags-playbook.yml!

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
-   https://docs.ansible.com/ansible/latest/plugins/plugins.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_tags.html

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com