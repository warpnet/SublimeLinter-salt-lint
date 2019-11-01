SublimeLinter-salt-lint
=======================

[![Build Status](https://travis-ci.org/warpnet/SublimeLinter-salt-lint.svg?branch=master)](https://travis-ci.org/warpnet/SublimeLinter-salt-lint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [salt-lint](https://github.com/warpnet/salt-lint), a command-line utility that checks for best practices in SaltStack. It will be used with __Salt State files__ (SLS) files.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `salt-lint` is installed on your system.

In order for `salt-lint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
- Salt-lint settings: https://github.com/warpnet/salt-lint#command-line-options
