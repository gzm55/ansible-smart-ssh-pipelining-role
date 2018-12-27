from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase
from ansible.config.manager import ConfigManager, Setting, find_ini_config_file

class ActionModule(ActionBase):

    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        pipelining_settting = ConfigManager().data.get_setting('ANSIBLE_PIPELINING')
        result['msg'] = pipelining_settting.origin if pipelining_settting else ''
        result['changed'] = False
        return result
