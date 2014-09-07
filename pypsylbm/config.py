import os

class Config(object):
    def config_dir_path():
        """ 
        Depending on what system you run, you have a different 'config' path.
        On linux, and variants, we have ~/.config, on Windows there's APPDATA.
        """
        name = os.name
        if (name == 'nt'):
            # TODO not to sure about this
            return "%APPDATA%"
        else:
            return os.environ["HOME"] + "/.config/"
                   
    def data_dir_path():
        """
        The data directory inside the config dir
        """
        return Config.config_dir_path() + 'pypsylbm' + "/"
