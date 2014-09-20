import socket 

from pypsylbm.host import Host
from pypsylbm.config import Config

class Authenticate(object):
    def __init__(self, user): 
        self._user = user

    def execute(self):
        host = Host()

        message = '|'.join(["auth", self._user.name, self._user.password])
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode(), (host.address, host.port))
        
        # Response 
        print("authentication ... ", end='', flush=True)
        resp = sock.recv(1024).decode()
        token = resp.split('|')[1] 

        if token == "fail":
            print("fail")
        
        else:
            print("success")
            Config.store_key(token)



