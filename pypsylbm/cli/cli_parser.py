class CLIParser(object):
    """
    Command line interface to the application.
    """

    def __init__(self, params):
        """ Params are argument values passed in """
        self.__values = params

    def setup():
        """ If this is a first time run, we send creds, and get a key """
        print('Executing setup')

    def print_help():
        print("usage:")
        print("    pypsylbm <command> [data]")
        print()
        print("commands:")
        print("    pypsylbm set server <host> <port>")
        print("    pypsylbm register <username> <password>")
        print("    pypsylbm login <username> <password>")
        print("    pypsylbm (i|insert) <booktitle> <volume> <chapter> <page>")
        print("    pypsylbm (ls|list)")
        print() 

    def execute(args):
        """ Main entry point """

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
        print("register")

    def login(args):
        print('login')

    def insert(args):
        print('insert')

    def list(args):
        print('list')

