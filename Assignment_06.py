###  Assignment No 6 ###
#Name : Kiran Sanjay Lungade
#Batch : B2
#Roll No : 38
#Assignment Title : Implement and visualize Dependency Parsing of Textual Input using Standford CoreNLP and Spacy library


import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = """
Earth is the third planet from the Sun in our solar system and the only known celestial body to support life. 
With a diverse range of ecosystems, it is home to a vast array of plant and animal species, including humans. 
Earth's atmosphere, composed mainly of nitrogen and oxygen, sustains life by providing the necessary conditions for biological processes to thrive.
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")


'''
******************    OUTPUT      *************************

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'Earth'
token.dep_ = 'dep'

TOKEN: Earth
=====
token.tag_ = 'NNP'
token.head.text = 'is'
token.dep_ = 'nsubj'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'is'
token.dep_ = 'ROOT'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'planet'
token.dep_ = 'det'

TOKEN: third
=====
token.tag_ = 'JJ'
token.head.text = 'planet'
token.dep_ = 'amod'

TOKEN: planet
=====
token.tag_ = 'NN'
token.head.text = 'is'
token.dep_ = 'attr'

TOKEN: from
=====
token.tag_ = 'IN'
token.head.text = 'planet'
token.dep_ = 'prep'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'Sun'
token.dep_ = 'det'

TOKEN: Sun
=====
token.tag_ = 'NNP'
token.head.text = 'from'
token.dep_ = 'pobj'

TOKEN: in
=====
token.tag_ = 'IN'
token.head.text = 'planet'
token.dep_ = 'prep'

TOKEN: our
=====
token.tag_ = 'PRP$'
token.head.text = 'system'
token.dep_ = 'poss'

TOKEN: solar
=====
token.tag_ = 'JJ'
token.head.text = 'system'
token.dep_ = 'amod'

TOKEN: system
=====
token.tag_ = 'NN'
token.head.text = 'in'
token.dep_ = 'pobj'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'planet'
token.dep_ = 'cc'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'body'
token.dep_ = 'det'

TOKEN: only
=====
token.tag_ = 'JJ'
token.head.text = 'body'
token.dep_ = 'amod'

TOKEN: known
=====
token.tag_ = 'VBN'
token.head.text = 'body'
token.dep_ = 'amod'

TOKEN: celestial
=====
token.tag_ = 'JJ'
token.head.text = 'body'
token.dep_ = 'amod'

TOKEN: body
=====
token.tag_ = 'NN'
token.head.text = 'planet'
token.dep_ = 'conj'

TOKEN: to
=====
token.tag_ = 'TO'
token.head.text = 'support'
token.dep_ = 'aux'

TOKEN: support
=====
token.tag_ = 'VB'
token.head.text = 'is'
token.dep_ = 'advcl'

TOKEN: life
=====
token.tag_ = 'NN'
token.head.text = 'support'
token.dep_ = 'dobj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'is'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

TOKEN: With
=====
token.tag_ = 'IN'
token.head.text = 'is'
token.dep_ = 'prep'

TOKEN: a
=====
token.tag_ = 'DT'
token.head.text = 'range'
token.dep_ = 'det'

TOKEN: diverse
=====
token.tag_ = 'JJ'
token.head.text = 'range'
token.dep_ = 'amod'

TOKEN: range
=====
token.tag_ = 'NN'
token.head.text = 'With'
token.dep_ = 'pobj'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'range'
token.dep_ = 'prep'

TOKEN: ecosystems
=====
token.tag_ = 'NNS'
token.head.text = 'of'
token.dep_ = 'pobj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'is'
token.dep_ = 'punct'

TOKEN: it
=====
token.tag_ = 'PRP'
token.head.text = 'is'
token.dep_ = 'nsubj'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'is'
token.dep_ = 'ROOT'

TOKEN: home
=====
token.tag_ = 'RB'
token.head.text = 'is'
token.dep_ = 'advmod'

TOKEN: to
=====
token.tag_ = 'IN'
token.head.text = 'home'
token.dep_ = 'prep'

TOKEN: a
=====
token.tag_ = 'DT'
token.head.text = 'array'
token.dep_ = 'det'

TOKEN: vast
=====
token.tag_ = 'JJ'
token.head.text = 'array'
token.dep_ = 'amod'

TOKEN: array
=====
token.tag_ = 'NN'
token.head.text = 'to'
token.dep_ = 'pobj'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'array'
token.dep_ = 'prep'

TOKEN: plant
=====
token.tag_ = 'NN'
token.head.text = 'species'
token.dep_ = 'nmod'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'plant'
token.dep_ = 'cc'

TOKEN: animal
=====
token.tag_ = 'NN'
token.head.text = 'plant'
token.dep_ = 'conj'

TOKEN: species
=====
token.tag_ = 'NNS'
token.head.text = 'of'
token.dep_ = 'pobj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'species'
token.dep_ = 'punct'

TOKEN: including
=====
token.tag_ = 'VBG'
token.head.text = 'species'
token.dep_ = 'prep'

TOKEN: humans
=====
token.tag_ = 'NNS'
token.head.text = 'including'
token.dep_ = 'pobj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'is'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

TOKEN: Earth
=====
token.tag_ = 'NNP'
token.head.text = 'atmosphere'
token.dep_ = 'poss'

TOKEN: 's
=====
token.tag_ = 'POS'
token.head.text = 'Earth'
token.dep_ = 'case'

TOKEN: atmosphere
=====
token.tag_ = 'NN'
token.head.text = 'sustains'
token.dep_ = 'nsubj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'atmosphere'
token.dep_ = 'punct'

TOKEN: composed
=====
token.tag_ = 'VBN'
token.head.text = 'atmosphere'
token.dep_ = 'acl'

TOKEN: mainly
=====
token.tag_ = 'RB'
token.head.text = 'of'
token.dep_ = 'advmod'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'composed'
token.dep_ = 'prep'

TOKEN: nitrogen
=====
token.tag_ = 'NN'
token.head.text = 'of'
token.dep_ = 'pobj'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'nitrogen'
token.dep_ = 'cc'

TOKEN: oxygen
=====
token.tag_ = 'NN'
token.head.text = 'nitrogen'
token.dep_ = 'conj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'atmosphere'
token.dep_ = 'punct'

TOKEN: sustains
=====
token.tag_ = 'VBZ'
token.head.text = 'sustains'
token.dep_ = 'ROOT'

TOKEN: life
=====
token.tag_ = 'NN'
token.head.text = 'sustains'
token.dep_ = 'dobj'

TOKEN: by
=====
token.tag_ = 'IN'
token.head.text = 'sustains'
token.dep_ = 'prep'

TOKEN: providing
=====
token.tag_ = 'VBG'
token.head.text = 'by'
token.dep_ = 'pcomp'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'conditions'
token.dep_ = 'det'

TOKEN: necessary
=====
token.tag_ = 'JJ'
token.head.text = 'conditions'
token.dep_ = 'amod'

TOKEN: conditions
=====
token.tag_ = 'NNS'
token.head.text = 'providing'
token.dep_ = 'dobj'

TOKEN: for
=====
token.tag_ = 'IN'
token.head.text = 'conditions'
token.dep_ = 'prep'

TOKEN: biological
=====
token.tag_ = 'JJ'
token.head.text = 'processes'
token.dep_ = 'amod'

TOKEN: processes
=====
token.tag_ = 'NNS'
token.head.text = 'for'
token.dep_ = 'pobj'

TOKEN: to
=====
token.tag_ = 'TO'
token.head.text = 'thrive'
token.dep_ = 'aux'

TOKEN: thrive
=====
token.tag_ = 'VB'
token.head.text = 'conditions'
token.dep_ = 'relcl'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'sustains'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

'''