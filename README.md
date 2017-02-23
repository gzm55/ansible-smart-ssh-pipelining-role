smart_ssh_pipelining
====================

Try to detect and enable ssh pipeling if needed, and the `ansible_ssh_pipelining` fact.
If the following conditions are matched, the role will skip detecting for the hosts:
- set inventory variable: `ansible_ssh_pipelining`;
- set `pipelining` in the effective ansible.cfg;
- `ANSIBLE_SSH_PIPELINING` environment is not empty.

Each time you changing the become method or the become flag or change the requiretty in sudoers config,
this role can be re-inclued to reflect the correct pipelining status.

When become method is 'su', ansible will ignore ansible_ssh_pipelining, so only detect for 'sudo',
and enable ssh pipelining for all other meghods. Having a remote host without 'sudo' command,
we also enable pipelining, cause a become-task will always fail in this scenario.

This role does not require remote machines having a python executable,
and can be safely used before seeding the machines.

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

- `gzm55.local_ansible_config`
- `gzm55.require_local_command`

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: gzm55.smart_ssh_pipelining }

License
-------

BSD
