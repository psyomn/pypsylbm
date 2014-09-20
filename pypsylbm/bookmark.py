class Bookmark(object):
    """ Bookmark domain object """ 

    def __init__(self, name, title, volume, chapter, page):
        self._name = name
        self._title = title 
        self._volume = volume
        self._chapter = chapter
        self._page = page

    @property
    def name(self): return self._name

    @property
    def title(self): return self._title

    @property
    def volume(self): return self._volume

    @property 
    def chapter(self): return self._chapter

    @property
    def page(self): return self._page

