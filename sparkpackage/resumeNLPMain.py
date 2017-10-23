import nltk

import spacy

from sparkpackage.ReadFile import ReadFile


def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""

    print sentt

    for tree in sentt:
        if hasattr(tree, 'label') and tree.label:
            if tree.label() == 'PERSON': print tree[0][0]
    # for subtree in sentt.subtrees(filter=lambda t: t.label == 'PERSON'):
    #     for leaf in subtree.leaves():
    #         person.append(leaf[0])
    #     if len(person) > 1: #avoid grabbing lone surnames
    #         for part in person:
    #             name += part + ' '
    #         if name[:-1] not in person_list:
    #             person_list.append(name[:-1])
    #         name = ''
    #     person = []
    #
    # return (person_list)
    #




text = """Thomson Huret and Thompson Baykara have responded positively to Bitcoin"""
readFile = ReadFile("/home/dharshekthvel/ac/bin/fr/baykara.html")

names = get_human_names(readFile.readFile())
print "LAST, FIRST"


