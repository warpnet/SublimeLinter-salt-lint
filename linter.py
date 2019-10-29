from SublimeLinter import lint


class SaltLint(lint.Linter):
    name = 'salt-lint'
    cmd = ('salt-lint', '--nocolor', '${args}', '${file}')
    regex = (r'(?P<code>\d+) (?P<message>.+)\s+'
            r'(.+):(?P<line>\d+)\s+'
            r'(?P<near>.+)')
    multiline = True
    default_type = lint.WARNING
    defaults = {
        'selector': 'source.sls'
    }
