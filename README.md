smart_ssh_pipelining
=========

Try to detect ssh pipeling if needed, and the `ansible_ssh_pipelining` fact is set to `True` or `False`.
If the following conditions is set, the role will skip detecting for the hosts:
- set inventory variable: `ansible_ssh_pipelining`;
- `pipelining` in the effective ansible.cfg;
- `ANSIBLE_SSH_PIPELINING` environment is not empty.

Requirements
------------

Python modules:
- ansible >= 2.0
- jinja2 >= 2.6

Role Variables
--------------

N/A

Dependencies
------------

gzm55.local_ansible_config

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: gzm55.smart_ssh_pipelining }

License
-------

BSD
