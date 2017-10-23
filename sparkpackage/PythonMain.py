from sparkpackage.ReadNameFile import ReadNameFile
from sparkpackage.FetchEmail import FetchEmail
from sparkpackage.ReadFile import ReadFile

readFile = ReadFile("/home/dharshekthvel/ac/bin/fr/baykara.html")
fetchMail = FetchEmail(readFile.readFile())

print fetchMail.fetchEmailFromFileContent()



read_name_file = ReadNameFile('/home/dharshekthvel/ac/code/ResumeParser-master/GATEFiles/plugins/ANNIE/resources/gazetteer/person_first.lst')
french_names = read_name_file.readFrenchName('/home/dharshekthvel/ac/code/ResumeParser-master/GATEFiles/plugins/ANNIE/resources/gazetteer/person_first.lst')
print ReadNameFile.finalArray