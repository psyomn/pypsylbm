import os, errno

class Config(object):

    key_filename = 'key'
    db_name = 'pypsylbm.sqlite3'

    def config_dir_path():
        """ 
        Depending on what system you run, you have a different 'config' path.
        On linux, and variants, we have ~/.config, on Windows there's APPDATA.
        """
        name = os.name
        if (name == 'nt'):
            # TODO not to sure about this (windows)
            return "%APPDATA%"
        else:
            return os.environ["HOME"] + "/.config/"
                   
    def data_dir_path():
        """ The data directory inside the config dir """
        # TODO cross platform sep might have an issue? 
        return Config.config_dir_path() + 'pypsylbm' + "/"

    def db_path():
        """ The sqlite3 database file """
        return ''.join([Config.data_dir_path(), Config.db_name])

    def bootstrap():
        """ Make init stuff, each time the program runs """
        os.makedirs(name=Config.data_dir_path(), exist_ok=True)

    def token_path():
        """ One text file, containing one line, which is API key """
        return ''.join([Config.data_dir_path(), Config.key_filename])

    def store_key(token):
        """ Store token in separate file for later loading """
        f = open(Config.token_path(), 'w')
        f.write(token)
        f.close()
        
    def load_key():
        """ Load token from standard file """
        f = open(Config.token_path(), 'r')
        token = f.readline()
        f.close()
        return token

    def is_first_setup():
        """ checks ~/.config and sees if pypsylbm/ exists. True if not """
        path = Config.data_dir_path()
        return not os.path.isdir(path)

