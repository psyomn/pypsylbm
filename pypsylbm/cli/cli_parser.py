from pypsylbm.config import Config
from pypsylbm.user import User
from pypsylbm.bookmark import Bookmark
from pypsylbm.session import Session

from pypsylbm.commands.register import Register
from pypsylbm.commands.authenticate import Authenticate
from pypsylbm.commands.insert import Insert
from pypsylbm.commands.list import List
from pypsylbm.session import Session

class CLIParser(object):
    """ Command line interface to the application. """

    def print_help():
        print("usage:")
        print("    pypsylbm set server <host> <port>")
        print("    pypsylbm register <username> <password>")
        print("    pypsylbm login <username> <password>")
        print("    pypsylbm (i|insert) <bookmark-label> <booktitle> <volume> <chapter> <page>")
        print("    pypsylbm (d|delete) <bookmark-id>")
        print("    pypsylbm (ls|list)")
        print() 

    def execute(args):
        """ Main entry point """

        sess = Session()

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

            elif cmd in ['i', 'insert']:
                CLIParser.insert(rest)

            elif cmd in ['ls', 'list']:
                CLIParser.ls(rest)

            elif cmd in ['h', 'help']:
                CLIParser.print_help()

            elif cmd in ['d', 'delete']:
                CLIParser.delete(rest)

            else:
                print("Invalid command. Try 'help'")


    def ls(args):
        sess = Session()
        lst = List(sess)
        lst.execute()

    def cmdset(args):
        print("set")

    def register(args):
        if not CLIParser._proper_arr_size(args, 2): return

        username, password = args[0], args[1]
        user = User(username, password)
        reg = Register(user)
        reg.execute()

    def login(args):
        if not CLIParser._proper_arr_size(args, 2): return

        username, password = args[0], args[1]
        user = User(username, password)
        auth = Authenticate(user)
        auth.execute()

    def insert(args):
        if not CLIParser._proper_arr_size(args, 5): return

        session = Session()

        name, title, = args[0], args[1]
        volume, chapter, page = int(args[2]), int(args[3]), int(args[4])
        bm = Bookmark(session, name, title, volume, chapter, page)
        ins = Insert(bm)
        ins.execute()

    def delete(args):
        print("TODO delete stuff")

    def _proper_arr_size(arr, size):
        """ Check if array is of particular size; print error if not """
        if len(arr) != size:
            print(size, " argument(s) required")
            return False
        else:
            return True

