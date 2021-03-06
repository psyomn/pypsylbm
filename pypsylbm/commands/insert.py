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
        self._handle_response(resp)

    def _handle_response(self, response):
        status = response.split("|")[1]

        if status == "ok":
            bm_id = int(response.split("|")[2])
            self._bookmark.identification = bm_id 

            if self._bookmark.select(bm_id) == None:
                self._bookmark.insert()
                print("stored bookmark")

            else:
                self._bookmark.update()
                print("updated bookmark")


        elif status == "fail":
            print("Problem inserting bookmark")

        else:
            print("Malformed reply")


