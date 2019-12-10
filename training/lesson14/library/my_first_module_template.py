#!/usr/bin/python
# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
'metadata_version': '1.0',
'status': ['preview'],
'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: << INTRODUCE MODULE NAME >>
short_description: This is my first module
version_added: "2.9"
description:
    - "This is my longer description explaining my first module"
options:
    name:
        description:
        - This is the name of the person who can perform an action
        required: true
    << INTRODUCE ACTION OPTION>>
author:
    - << INTRODUCE AUTHOR NAME >>
'''

EXAMPLES = '''
# Pepe action
- name: Test with a message
  my_first_module:
    name: Pepe
    action: run
# Laura action
- name: Test with a message
  my_first_module:
    name: Laura
    action: jump

'''

RETURN = '''
original_params:
    description: The original params that were passed in
    type: str
    returned: always
message:
    description: The output message that the test module generates
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():

    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=True),
        << INTRODUCE ACTION ARGUMENT >>
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        << DEFINE CHANGE STATE >>
        original_message=[],
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    << APPEND TO 'original_message' NAME ARGUMENT >>
    << APPEND TO 'original_message' ACTION ARGUMENT >>
    << DEFINE TEXT 'message' >>

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['name'] == 'Fail':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():

    run_module()

if __name__ == '__main__':

    main()
