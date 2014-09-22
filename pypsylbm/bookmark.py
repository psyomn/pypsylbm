class Bookmark(object):
    """ Bookmark domain object """ 

    def __init__(self, session, name, title, volume, chapter, page):
        self._session = session
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
    def identification(self): return self._id

    @identification.setter
    def identification(self, value): self._id = value

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

    sql_select = sql_all + " where id = ?"

    sql_update = "update " + sql_table_name + " set " \
        "id = ?, name = ?, title = ?, volume = ?, chapter = ?, page = ? "\
        "WHERE id = ?"

    def insert(self):
        self._session.db.execute(Bookmark.sql_insert, 
            (self.identification, self.name, self.title,
            self.volume, self.chapter, self.page))
        self._session.db.commit()

    def delete(self):
        self._session.db.execute(Bookmark.sql_delete, (self.identification))

    def update(self):
        self._session.db.execute(Bookmark.sql_update, (self.identification, self.name, self.title,
            self.volume, self.chapter, self.page, self.identification))

    def select(self, idnum):
        row = self._session.db.execute(Bookmark.sql_select, (idnum))[0]

        bookmark = Bookmark(
          self._session, 
          row[1], # name 
          row[2], # title
          row[3], # volume
          row[4], # chapter
          row[5]) # page

        bookmark.identification = row[0]

        return bookmark
        

    def all(self):
        rows = self._session.db.execute(Bookmark.sql_all)

    def create_table(db):
        db.execute(Bookmark.sql_create)
        db.commit()

