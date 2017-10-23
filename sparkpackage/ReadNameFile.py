class ReadNameFile:

    dataholder = []
    finalArray = []

    def __init__(self, _fileName_):
        self.fileName = _fileName_

    def readFrenchName(self, _fileName_):
        # with open(self.fileName, "r") as filePointer:
        #     lines = filePointer.readlines().splitlines()
        #     lines = [x.strip() for x in lines]

        with open(_fileName_, "r") as f:
            for line in f:
                ReadNameFile.dataholder.append(line)

        ReadNameFile.finalArray = [s.rstrip('\n') for s in ReadNameFile.dataholder if s != '\n']

        return



