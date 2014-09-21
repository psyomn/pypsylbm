import sqlite3
import os.path

from pypsylbm.config import Config
from pypsylbm.bookmark import Bookmark

class Session(object):
    """ Session data here (db, etc). If things need to be tested or emulated we
        can perform the required edits in this class instead """

    def __init__(self):
        self.__check_setup()

    @property
    def db(self): return self._db

    def __check_setup(self):
        """ Auxiliary stuff that needs to be checked per run. Is there a
            database? Are the config files there? """ 

        if not Config.is_first_setup(): 
            self._db = sqlite3.connect(Config.db_path())
            return

        Config.bootstrap()
        self._db = sqlite3.connect(Config.db_path())

        Bookmark.create_table(self.db)
           

