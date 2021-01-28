# VMWare

This role has been designed in order to perform VMWare administration tasks. Brief overview of these tasks are included in the following list:

-   Create and Delete VMs
-   Create VM snapshots
-   Poweron and poweroff specific VMs

In order to support previous tasks, the following playbooks have been developed:

-   create-snapshot.yml
-   create-vm.yml
-   find-vm.yml
-   manage-vm.yml

Finally, defined actions have been included in the following list:

-   create-snapshot
-   manage-vm
-   find-vm
-   create-vm

## Role Variables

### Inputs

It is important to bear in mind that this role is supported by next variable files:

| Variable         | Comment                   | Type   | Tasks           |
| ---------------- | ------------------------- | ------ | --------------- |
| vm_name          | VM Name                   | String | _ALL_           |
| vmware_srv       | VMWare URL                | String | _ALL_           |
| vmware_user      | VMWare Admin User         | String | _ALL_           |
| vmware_pass      | VMWare Admin User Passwd  | String | _ALL_           |
| vmware_dc        | VMWare Datacenter         | String | _ALL_           |
| vmware_folder    | VMWare Destination Folder | String | _ALL_           |
| snap_description | Snapshot Description      | String | create-snapshot |
| vmware_template  | VMWare Template Name      | String | create-vm       |
| vmware_esxi      | VMWare ESXi server IP     | String | create-vm       |
| vmware_datastore | VMWare Datastore name     | String | create-vm       |
| status           | VM status to be defined   | String | manage-vm       |

### Outputs

The result of this role execution should be one of the following action included in the list. Of course, it depends on the action has been triggered and its status of execution:

-   Success process execution messages
-   vmware_dc and vmware_folder -> Retrieve VM facts (find-vm)

## Dependencies

A number of python libraries have to be installed in Ansible server in order to perform correctly theses tasks. For this reason, the following modules should be installed:

-   pyvmomi

## Example Playbook

    - include_role:
        name: vmware
      vars:
        action: create-vm
        vm_name: prueba01
        vmware_folder: /DC/vm/Administration/Ansible
        vmware_dc: DC
        vmware_esxi: DCvs03.example.com
        vmware_template: VI_RHEL7_Template
        vmware_datastore: DC_vs03

## License

BSD

## Author Information

-   Asier Cidon @RedHat
