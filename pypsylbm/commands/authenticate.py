
class Authenticate(object):
    def __init__(self, user): 
        """ Pass a user in with proper credentials, and authenticate """
        self._user = user

    def execute(self):
        print("sending authentication request")

