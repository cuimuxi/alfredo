#encoding: utf-8

import os
import sys
from PyGtalkRobot import GtalkRobot

import plugnplay

__all__ = ['ICommand',  'Plugin']

Plugin = plugnplay.Plugin


_CONFIG_DIR = os.path.abspath(os.path.join(os.environ.get('HOME', '/tmp'), '.config/alfredo'))
_CUSTOM_COMMANDS_DIR = os.path.join(_CONFIG_DIR, 'commands')
if not os.path.exists(_CONFIG_DIR):
    os.makedirs(_CONFIG_DIR)
    os.makedirs(_CUSTOM_COMMANDS_DIR)


plugnplay.set_plugin_dirs(_CUSTOM_COMMANDS_DIR)


class ICommand(plugnplay.Interface):

  '''
   Returns tha command name
  '''
  def name(self):
    pass

  '''
   Returns a tuple (short-help, long-help)
   about the command
  '''
  def help(self):
    pass

  '''
   Returns true if the command name passed as a paramater
   matches the command implemented by this interface
  '''
  def match_name(self, command):
    pass

  '''
   Run the specific command. Returns a string.
   Receives the username of the sender and any parameters
   passed on the message, eg:

    sender: process arg0 arg1 arg2

   would be translated to: run(sender, 'process', arg0, arg1, arg2)
  '''
  def run(self, user, command, *args):
    pass

commands_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))
plugnplay.set_plugin_dirs(commands_dir)
plugnplay.load_plugins()
