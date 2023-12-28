class FileType:
    def __init__(self, name, extension):
        self.__name = name
        self.__extension = extension
    
    # Mutators
    def set_name(self, name):
        self.__name = name

    def set_extension(self, extension):
        self.__extension = extension

    # Accessors
    def get_name(self):
        return self.__name

    def get_extension(self):
        return self.__extension
    

class Photo(FileType):
    def __init__(self, name, extension, date):
        FileType.__init__(self,name,extension)
        self.__date = date

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date


class Music(FileType):
    def __init__(self, name, extension, year, albumartist, album):
        FileType.__init__(self,name,extension)
        self.__year = year
        self.__albumartist = albumartist
        self.__album = album

    # Mutators
    def set_year(self, year):
        self.__year = year

    def set_albumartist(self, albumartist):
        self.__albumartist = albumartist

    def set_album(self, album):
        self.__album = album

    # Accessors
    def get_year(self):
        return self.__year  
      
    def get_albumartist(self):
        return self.__albumartist
    
    def get_album(self):
        return self.__album    
