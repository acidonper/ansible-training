Red Hat Ansible Trainging
---------------------------

Introduction 
--------------

Red Hat Ansible Training tries to give a general overview about Red Hat Ansible Engine and Red Hat Ansible Tower solutions, covering the most important concepts and elements inside these automation tools.

To support this objective, a set of practical laboratories have been included in this training in order to explore each point deeply and assist the student learning process to internalizing best practices and key concepts.

Folder Structure 
-----------------

A folder structure is provided in this repository in order to split laboratory content and improve the clarity of the training. The following folders have been included with a specific objective:

* aws -> Includes environment set up automatisms in order to deply and destry laboratory environments.
* example -> Includes son Ansible playbooks and roles which could be usefull in a future steps.
* training -> Lessons structure which include specific execercises with the appropiate solutions.

Laboratory Environment
------------------------

Amazon Web Services (AWS) is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.

As you might know, Red Hat Ansible community supports several AWS modules which allow final customers to define and deploy multiples computing resources in this provider. In that way, this training makes use of these modules to deploy and destroy the enviroment dynamically based on number of users and resources the training needs.

* Deploy Red Hat Ansible Training Environment
```
$ ansible-playbook aws-iac.yaml
```

* Destroy Red Hat Ansible Training Environment
```
$ ansible-playbook aws-iac-destroy.yaml 
```

Lessons 
---------

Training folder includes The following list includes a lessons summary:

* **Lesson 1** - Install Ansible
* **Lesson 2** - Configure Ansible
* **Lesson 3** - Ansible AdHoc Commands
* **Lesson 4** - Ansible Inventory
* **Lesson 5** - Ansible Playbooks
* **Lesson 6** - Ansible Variable
* **Lesson 7** - Ansible Facts
* **Lesson 8** - Ansible Vault
* **Lesson 9** - Ansible Conditionals, loops and delegation
* **Lesson 10** - Ansible Handlers
* **Lesson 11** - Install Ansible
* **Lesson 12** - Install Ansible
* **Lesson 13** - Install Ansible
* **Lesson 14** - Install Ansible
* **Lesson 15** - Install Ansible
* **Lesson 16** - Install Ansible
* **Lesson 17** - Install Ansible


License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
   
