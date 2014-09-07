
class User(object): 
    """ User of the specific account """

    def __init__(self, name):
        self.__name = name
        self.__api_token = None

    @property
    def api_token(self):
        return self.__api_token
      
    @property
    def name(self):
        return self.__name

