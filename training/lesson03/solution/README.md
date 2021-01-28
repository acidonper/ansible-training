
# Ansible AdHoc Commands

## Print "It is working" message on localhost

```
$ ansible localhost -c local -m debug -a 'msg="It is working"'
```

## Print instance settings on localhost

```
$ ansible localhost -c local -m setup
```

## Create a new user "yourname" on localhost using become (root)

```
$ ansible localhost -c local -m user -a "name=yourname" -b -K
```

## Include the new user "yourname" on **wheel** group on localhost using become (root)

```
$ ansible localhost -c local -m user -a "name=yourname groups=wheel" -b -K
```

## Copy file **/etc/passwd** on localhost using user "yourname" and setting permissions 440 and owner root in **/tmp/newfile**

```
$ ansible localhost -c local -m copy -a "src=/etc/passwd dest=/tmp/newfile owner=root mode=0440" -b --become-user=yourname -K
```
When setting permissions using octal notation in Ansible modules take the following into account:

> For those used to /usr/bin/chmod remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like 0644 or 01777) or quote it (like '644' or '1777') so Ansible receives a string and can do its own conversion from string into number. Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results

For more information please visit:

- https://docs.ansible.com/ansible/latest/modules/copy_module.html

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
