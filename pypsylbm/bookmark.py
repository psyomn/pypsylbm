class Bookmark(object):
    """ Bookmark domain object """ 

    def __init__(self, name, title, volume, chapter, page):
        self._name = name
        self._title = title 
        self._volume = volume
        self._chapter = chapter
        self._page = page
        self._id = None

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

    @property
    def id(self): return self._id

    @id.setter
    def id(self, value): self._id = value

    # Active record stuff

    sql_table_name = "bookmarks" 

    sql_create = "create table " + sql_table_name + "(" \
        "id INTEGER, name TEXT, title TEXT, volume INTEGER, " \
        "chapter INTEGER, page INTEGER);"

    sql_insert = "insert into " + sql_table_name + " (" \
        "id,name,title,volume,chapter,page) values " \
        "(?,?,?,?,?,?);"

    sql_delete = "delete from " + sql_table_name + " where id = ?"
    
    sql_all = "select * from " + sql_table_name

    sql_select = sql_all + " where_id = ?"

    sql_update = "update " + sql_table_name + " set " \
        "id = ?, name = ?, title = ?, volume = ?, chapter = ?, page = ? "\

    def insert(self): pass

    def delete(self): pass

    def update(self): pass

    def select(self): pass

    def all(self): pass

    def create_table(db):
        db.execute(Bookmark.sql_create)
        db.commit()

