# Ansible Filter

Filters in Ansible are from Jinja2, and are used for transforming data inside a template expression. Take into account that templating happens on the Ansible controller, not on the task’s target host, so Filters also execute on the controller as they manipulate local data.
In addition the ones provided by Jinja2, Ansible ships with its own and allows users to add their own custom filters.

In order to understand this lesson properly, a set of steps have been designed to be implemented in the following section.

**ENJOY !!!**

## Resources

In order to assist this laboratory implementation, a set of resources have been added:

-   dictionary.json (JSON file with an example)

## Steps

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Create a playbook named "roles-playbook.yml" using "myinstance" as a hosts parameter and `<studentxx>` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Read "dictionary.json" file and register the content in a new variable
    -   Parse the new variable content to an ansible dictionary
    -   Search cluster names and print the result
    -   Search servers names and print the result
    -   Search libraries names and print the result
    -   Set a new fact with an IPs arrays with the following content:
        -   192.168.1.1
        -   192.16.2,2
        -   192.168.23.32
    -   Test each array IP item in order to validate the IP address. If one of them is not valid, this tasks has to throw an error. 
    -   Extract *path*, *port* and *hostname* from the following url:
        -   http://user:password@www.acme.com:9000/dir/index.html?query=term#fragment
-     Before running your playbook, run the ansible-playbook --syntax-check site.yml command to verify that its syntax is correct
-     Run the playbook!

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html


License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com


