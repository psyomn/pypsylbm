import socket 

from pypsylbm.config import Config
from pypsylbm.host import Host

class Insert(object):
    """ Insert a bookmark """
    
    def __init__(self, bookmark):
        self._bookmark = bookmark

    def execute(self):
        bm = self._bookmark
        token = Config.load_key()
        host = Host()
 
        bmdata  = ['ins']
        bmdata += [bm.name, bm.title]
        bmdata += [str(bm.volume), str(bm.chapter), str(bm.page)]
        bmdata += [token]

        message = '|'.join(bmdata)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode(), (host.address, host.port))

        resp = sock.recv(1024).decode()

        print(resp)
