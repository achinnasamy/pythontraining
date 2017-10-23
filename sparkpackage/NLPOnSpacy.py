import spacy
nlp = spacy.load('en')
doc = nlp(u'Thomas is doing good')



train_data = [("Baris", ['FRENCH_NAME']), ("Baykara", ['FRENCH_NAME'])]
nlp.entity.add_label('FRENCH_NAME')