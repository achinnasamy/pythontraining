from gensim import corpora

#corpus = corpora.MmCorpus('/home/dharshekthvel/ac/code/ResumeParser-master/GATEFiles/plugins/ANNIE/resources/gazetteer/education.lst')


#dictionary = corpora.Dictionary('/home/dharshekthvel/ac/code/ResumeParser-master/GATEFiles/plugins/ANNIE/resources/gazetteer/education.lst')


inputUniversities = [
    ['Universit Paris1 Panthon Sorbonne, en partenariat'],
    ['Universit Galatasaray Istanbul'],
    ['Universit Paris Ouest Nanterre La Dfense'],
    ['Universit de Strasbourg'],
    ['Universit Paris 1 Panthon Sorbonne'],
    ['Universit Paris1 Panthon'],
    ['PANTHEON-SORBONNE PARIS 1'],
    ['Pantheon Sorbonne University'],
    ['Universit de Paris X-Nanterre']
]

dictionary = corpora.Dictionary(inputUniversities)




print dictionary.token2id