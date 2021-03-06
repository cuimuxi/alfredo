Alfredo - Born to serve!
************************


Alfredo is a simple, extensible gtalk bot. It's capable of doing any kind of tasks, implemented as separated commands.

Here is a typical session: ::

    you: inv some text
    alfredo: called inv some text -> txet emos
    

Implementing a new command
**************************

Commands are implemented as Plugins (more at plugnplay <https://github.com/daltonmatos/plugnplay>). Just create a new class:

    from alfredo import Plugin, ICommand

    class SomeCommand(Plugin):
      implements = [ICommand]

      def help(self):
        return ('short help', 'long help')

      def name(self):
        return 'mycommand'

      def match_name(self, command):
        return 'mycommand' == command

      def run(self, user, *args)
        # process some logic
        return result


In this case we create a new command named 'mycommand'. If we send this message to alfredo:

   mycommand p1 p2 p3


the ``run()`` method would be called like this: ``run('user@domain.com', 'p1', 'p2', 'p3')``. This method must return a string, that will be sent back to the original user.


How to use it
*************

To start talking to a running instance of alfredo just add ``alfredo@daltonmatos.com`` to your gtalk conacts list and you are done!

Or try out your own commands from the example code.


Dependencies
************

Alfredo's core components only needs:

* plugnplay - https://github.com/daltonmatos/plugnplay
* xmpppy - http://xmpppy.sourceforge.net/

The included commands needs:

* BeautifulSoup - http://www.crummy.com/software/BeautifulSoup/
* requests - https://github.com/kennethreitz/requests
* simplejson - http://code.google.com/p/simplejson/

You can even run the requirements file to get up your environment::

    pip install -r requirements.txt

--

Dalton barreto

daltonmatos@gmail.com


