from .state import EOF
from .tokens import TokenEof
from .tokens_base import TOKEN_COMMAND_EXECUTE_COMMAND
from .tokens_base import TokenOfCommand
from Vintageous import ex


@ex.command('sublime', 'sublime')
class TokenExecuteCommand(TokenOfCommand):
    def __init__(self, params, *args, **kwargs):
        super().__init__(params,
                         TOKEN_COMMAND_EXECUTE_COMMAND,
                         'sublime', *args, **kwargs)
        self.target_command = 'ex_execute_command'

    @property
    def command(self):
        return self.params['cmd']

    @property
    def arguments(self):
        return self.params['args']


def scan_command_execute_command(state):
    params = {
        'cmd': None,
        'args': None,
    }

    m = state.expect_match(r'( (?P<cmd>[a-z_]+))( (?P<args>.+))?$')
    params.update(m.groupdict())

    return None, [TokenExecuteCommand(params), TokenEof()]
