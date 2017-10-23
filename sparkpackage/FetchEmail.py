
import re

class FetchEmail:


    def __init__(self, filecontent):
        self.filecontent = filecontent

    def fetchEmailFromFileContent(self):
        matches = re.findall(r'[\w\.-]+@[\w\.-]+', self.filecontent)
        return matches


