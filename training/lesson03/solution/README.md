
# Ansible AdHoc Commands

## Debug "It is working" message on localhost

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
$ ansible localhost -c local -m user -a "name=pepe groups=wheel" -b -K
```

## Copy sudo file **/etc/passwd** on localhost using user "yourname" and setting permissions 440 and owner root in **/tmp/newfile**

```
$ ansible localhost -c local -m copy -a "src=/etc/passwd dest=/tmp/newfile owner=root mode=400" -b -K

```
