from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):

    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        ctx = self._play_context

        # connection common
        result['connection'] = ctx.connection
        result['port'] = ctx.port
        if ctx.remote_user is not None:
          result['remote_user'] = ctx.remote_user

        result['check_mode'] = bool(ctx.check_mode)
        result['diff'] = bool(ctx.diff)

        # become
        result['become'] = bool(ctx.become)
        result['become_method'] = ctx.become_method
        result['become_user'] = ctx.become_user
        result['become_exe'] = ctx.become_exe or getattr(ctx, '%s_exe' % ctx.become_method, ctx.become_method)

        # become flags may be modified in PlayContext.make_become_cmd
        become_flags = ctx.become_flags or getattr(ctx, '%s_flags' % ctx.become_method, '')
        if ctx.become_method == 'sudo' or ctx.become_method == 'dzdo':
          if ctx.become_pass:
            become_flags = become_flags.replace('-n', '')
        elif ctx.become_method == 'doas':
          if not ctx.become_pass:
            become_flags += ' -n '
          if ctx.become_user:
            become_flags += ' -u %s ' % ctx.become_user
        result['become_flags'] = become_flags

        result['changed'] = False
        return result
