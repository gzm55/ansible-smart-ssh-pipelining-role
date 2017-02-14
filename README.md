smart_ssh_pipelining
=========

Try to detect ssh pipeling if needed, and the `ansible_ssh_pipelining` fact is set to `True` or `False`.

Requirements
------------

ansible >= 2.0
jinja2 >= 2.7

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
