from pypsylbm.config import Config
from pypsylbm.user import User

from pypsylbm.commands.register import Register
from pypsylbm.commands.authenticate import Authenticate

class CLIParser(object):
    """
    Command line interface to the application.
    """

    def setup():
        """ If this is a first time run, we send creds, and get a key """
        Config.bootstrap()

    def print_help():
        print("usage:")
        print("    pypsylbm set server <host> <port>")
        print("    pypsylbm register <username> <password>")
        print("    pypsylbm login <username> <password>")
        print("    pypsylbm (i|insert) <booktitle> <volume> <chapter> <page>")
        print("    pypsylbm (ls|list)")
        print() 

    def execute(args):
        """ Main entry point """
        CLIParser.setup()

        if len(args) == 1:
            CLIParser.print_help()

        else:
            cmd  = args[1]
            rest = args[2:]
            
            if cmd == 'set':      
                CLIParser.cmdset(rest)

            elif cmd == 'register': 
                CLIParser.register(rest)

            elif cmd == 'login':    
                CLIParser.login(rest)

            elif cmd == 'i' or cmd == 'insert':
                CLIParser.insert(rest)

            elif cmd == 'ls' or cmd == 'list': 
                CLIParser.ls(rest)

            elif cmd == 'help' or cmd == 'h':
                CLIParser.print_help()

            else:
                print("Invalid command. Try 'help'")


    def ls(args):
        print("going to list things")

    def cmdset(args):
        print("set")

    def register(args):
        username, password = args[0], args[1]
        user = User(username, password)
        reg = Register(user)
        reg.execute()
        print("register")

    def login(args):
        username, password = args[0], args[1]
        user = User(username, password)
        auth = Authenticate(user)
        auth.execute()
        print('login')

    def insert(args):
        print('insert')

    def list(args):
        print('list')

