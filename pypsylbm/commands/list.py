from pypsylbm.session import Session
from pypsylbm.bookmark import Bookmark

class List(object):

    def __init__(self, session):
        self._session = session

    def execute(self):
        sess = Session()
        for bm in Bookmark.select_all(sess):
            print(bm)


