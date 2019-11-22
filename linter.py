from SublimeLinter import lint


class SaltLint(lint.Linter):
    name = 'salt-lint'
    cmd = ('salt-lint', '--nocolour', '--severity', '${args}')
    regex = (r'\[(?P<code>\d+)\] '
             r'\[(?:(?P<error>HIGH)|(?P<warning>\w+):?)\] '
             r'(?P<message>.+)\s+'
             r'.+:(?P<line>\d+)\s+'
             r'(?P<near>.+)')
    multiline = True
    default_type = lint.WARNING
    defaults = {
        'selector': 'source.sls'
    }
