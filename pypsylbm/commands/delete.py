import socket

from pypsylbm.config import Config
from pypsylbm.host import Host

class Delete(object):
    
    def __init__(self, book):
        self._book = book
        
    def execute(self):
        message = '|'.join(['del', str(book.id), Config.load_key()])
        host = Host()

        socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket.sendto(message.encode(), (host.address(), host.port()))
        response = socket.recv(1024).decode()
        self.__handle_resp(response)

    def __handle_resp(self, response):
        isok = response.split("|")[1]
        if isok == 'ok':
            print("bookmark deleted")
        else:
            print("problem deleting bookmark")

