# Ansible Roles

## Search and Install Nginx official role located on Ansible Galaxy

```
$ ansible-galaxy install nginxinc.nginx
```

## Install rhel-system-roles


```
$ subscription-manager repos --enable ansible-2-for-rhel-8-x86_64-rpms
$ dnf install rhel-system-roles ansible

```

## Create a custom role named "mariadb" which has to implement the following tasks


```
$ ansible-galaxy init roles/mariadb
```

##   Test Database


```
$ sudo -i
$ mysql -u root -p
MariaDB [(none)]> $ show databases;
MariaDB [(none)]> $ show grants for 'test01'@'xxx';
MariaDB [(none)]> $ show grants for 'test02'@'xxx';
MariaDB [(none)]> $ show grants for 'test03'@'xxx';
```

##   Test NGINX


```
$ curl http://localhost
```

##   Test NTP


```
$ chronyc tracking

Reference ID    : D8EF230C (time4.google.com)
Stratum         : 2
Ref time (UTC)  : Fri Dec 06 12:37:05 2019
System time     : 0.000407905 seconds fast of NTP time
Last offset     : -0.000026877 seconds
RMS offset      : 0.000945020 seconds
Frequency       : 0.180 ppm slow
Residual freq   : +1.061 ppm
Skew            : 0.196 ppm
Root delay      : 0.111675613 seconds
Root dispersion : 0.001107449 seconds
Update interval : 65.4 seconds
Leap status     : Normal

```

## Useful Links

For more information, please visit:

-   https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
-   https://docs.ansible.com/ansible/latest/modules/modules_by_category.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
-   https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html
-   https://docs.ansible.com/ansible/latest/modules/import_tasks_module.html
-   https://galaxy.ansible.com/linux-system-roles/timesync
-   https://galaxy.ansible.com/nginxinc

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com