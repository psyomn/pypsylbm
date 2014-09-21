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

        resp = sock.recv(1024).decode()
        
        if resp == "regok":
            print("registration success")

        elif resp == "username-taken":
            print("username taken; try something else")

        elif resp == "bad-username":
            print("bad username format")

        else:
            print("malformed response")



