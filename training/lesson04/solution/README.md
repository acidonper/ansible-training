# Ansible Inventory

## Check inventory file structure is correct and graphs it 

```
ansible-inventory -i inventory --list
{
    "_meta": {
        "hostvars": {
            "student01": {
                "zone": "north"
            }, 
            "student02": {
                "zone": "north"
            }, 
            "student03": {
                "zone": "south"
            }, 
            "student04": {
                "zone": "south"
            }, 
            "student05": {
                "zone": "east"
            }, 
            "student06": {
                "zone": "east"
            }, 
            "student07": {
                "zone": "west"
            }, 
            "student08": {
                "zone": "west"
            }
        }
    }, 
    "all": {
        "children": [
            "laboratory", 
            "ungrouped"
        ]
    }, 
    "east": {
        "hosts": [
            "student05", 
            "student06"
        ]
    }, 
    "laboratory": {
        "children": [
            "east", 
            "north", 
            "south", 
            "west"
        ]
    }, 
    "north": {
        "hosts": [
            "student01", 
            "student02"
        ]
    }, 
    "south": {
        "hosts": [
            "student03", 
            "student04"
        ]
    }, 
    "west": {
        "hosts": [
            "student07", 
            "student08"
        ]
    }
}
```

```
$ ansible-inventory -i inventory --graph

@all:
  |--@laboratory:
  |  |--@east:
  |  |  |--student05
  |  |  |--student06
  |  |--@north:
  |  |  |--student01
  |  |  |--student02
  |  |--@south:
  |  |  |--student03
  |  |  |--student04
  |  |--@west:
  |  |  |--student07
  |  |  |--student08
  |--@ungrouped:
```

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
 