smart_ssh_pipelining (2.0.0)
================================

Try to detect and enable ssh pipelining if needed, and set the `ansible_pipelining` and
`ansible_ssh_pipelining` fact. If any one of the following conditions are matched, the role will
skip detecting for the hosts:
- set one of inventory variables: `ansible_pipelining` or `ansible_ssh_pipelining`;
- or set `pipelining` in the effective ansible.cfg;
- or `ANSIBLE_PIPELINING` environment is not empty.

Each time you chang the become method/flag or the requiretty in sudoers config,
this role can be re-inclued to reflect the correct pipelining status.

When become method is not 'sudo', ansible will ignore `ansible_ssh_pipelining`. So only detect for
'sudo', and enable ssh pipelining for all other methods. Having a remote host without 'sudo'
command, we also enable pipelining, cause a become-task will always fail in this scenario.

This role _does not_ require remote machines having a python executable, and can be safely used
before seeding the machines.

Requirements
------------

Python modules:
- ansible >= 2.8
- jinja2 >= 2.6

For ansible `[2.5, 2.8)`, use `smart_ssh_pipelining 1.0.2`.
For ansible `[2.2, 2.5)`, use `smart_ssh_pipelining 0.0.1`.

Role Variables
--------------

N/A

Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: gzm55.smart_ssh_pipelining }

License
-------

BSD
