class Bookmark(object):
    """ Bookmark domain object """ 

    def __init__(self, title, volume, chapter, page):
        self._title = title 
        self._volume = volume
        self._chapter = chapter
        self._page = page


    @property
    def title(): return self._title

    @property
    def volume(): return self._volume

    @property 
    def chapter(): return self._chapter

    @property
    def page(): return self._page
