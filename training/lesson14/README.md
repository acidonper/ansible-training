# Ansible Modules

Ansible Modules are a reusable, standalone scripts that Ansible runs on your behalf, either locally or remotely.

There are some use cases which require new modules because Ansible community does not satisfy their requirements or it is necessary to fork some implemented module in order to extend or modify its features.

In order to understand this lesson properly, a set of steps have been designed to be implemented in the following section.

**ENJOY !!!**

## Resources

In order to assist this laboratory implementation, a set of resources have been added:

-   ansible.cfg 
-   ./library/my_first_module_template.py

## Steps

-   Create an inventory file named "inventory" with a group named "myinstance" and your internal instance IP assigned included
-   Modify "ansible.cfg" configuration to be able to include the libraries included in ./library folder.
-   Copy "./library/my_first_module_template.py" into "./library/my_first_module.py" in order to implement a new module named "my_first_module.py"
-   Replace comments ´´<< XXXXXXXXX >>´´ in "my_first_module.py" in order to add the required content. The following list provides a summary about requisites:
    - Documentation section: 
        -   Define Module Name
        -   Introduce new option named "action"
        -   Introduce author name
    - run_module() function:
        -   Introduce a new argument named "action", not required with "Talk" as default value
        -   Define result as "changed" when this module is executed
        -   Append name and action original parameter to ``result["original_message"]`` array
        -   Define the message *"``<user>`` would like to ``<action>``"* in ``result["message"]`` variable
-   Create a playbook named "modules-playbook.yml" using "myinstance" as a hosts parameter and `<studentxx>` as a user. The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   Execute "my_first_module" module, and register output, with the following parameters:
        -   name: John
        -   action: Run
    -   Display module execution output
    -   Execute "my_first_module" module, and register output, with the following parameters:
        -   name: Peter
    -   Display module execution output
    -   Execute "my_first_module" module, and register output, with the following parameters:
        -   name: Fail
-   Before running your playbook, run the ansible-playbook --syntax-check  command to verify that its syntax is correct
-   Run the playbook!

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
-   https://docs.ansible.com/ansible/latest/dev_guide/index.html

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
 