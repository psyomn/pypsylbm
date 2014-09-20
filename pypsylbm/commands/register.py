import socket
from pypsylbm.host import Host 

class Register(object):
    def __init__(self, user):
        self._user = user

    def execute(self):
        host = Host()
        message = '|'.join(["reg", self._user.name, self._user.password])
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode(), (host.address, host.port))


