
class Host(object):
    """ Class used to configure which host we want (default or from file) """
    
    def __init__(self, mode=None):
        if mode == None:
            self._address = 'localhost'
            self._port    = 8080
        else:
            # TODO
            self._address = "from file"
            self._port = 0

    @property
    def address(self): return self._address

    @property
    def port(self): return self._port
        
