class User(object): 
    """ User of the specific account """

    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._api_token = None

    @property
    def api_token(self): return self._api_token
      
    @property
    def name(self): return self._name

    @property
    def password(self): return self._password
