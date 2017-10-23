class ReadFile:

    def __init__(self, _name_of_file_):
        self.name_of_file = _name_of_file_


    def readFile(self):
        resumeTikaFile = open(self.name_of_file, "r")
        return resumeTikaFile.read(99999)


