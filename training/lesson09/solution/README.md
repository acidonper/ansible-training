# Ansible Conditionals, loops and delegate

## Notes

You can pass a list directly to a parameter for some plugins. Most of the packaging modules, like yum and apt have this capability. When available, passing the list to a parameter is better than looping over the task. For example:

```
- name: optimal yum
  yum:
    name: "{{  list_of_packages  }}"
    state: present

- name: non-optimal yum, slower and may cause issues with interdependencies
  yum:
    name: "{{  item  }}"
    state: present
  loop: "{{  list_of_packages  }}"
```

## Useful Links

For more information, please visit:

-   https://stackoverflow.com/questions/29179856/create-mysql-tables-with-ansible
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html#iterating-over-a-simple-list

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
 