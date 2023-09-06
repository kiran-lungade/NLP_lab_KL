###  Assignment No 1 ###
#Name : Kiran Sanjay Lungade
#Batch : B2
#Roll No : 38
#Assignment Title : Text pre-processing using NLP operation : perform Tokenization
#Stop word removal, Punctuation removal,using Spacy or NLTK Library 

#import library
import spacy
nlp=spacy.load("en_core_web_sm")
from collections import Counter

print("\n##########   Sentence Detection    ###############\n")
#Sentence Detection

text1=("Detecting Paragraphs is somehow less mainstream."
       "Mostly there is some custom logic like: split after two line-ends, or split before uppercased title."
       "Maybe there is some layout-meta information, or a specific paragraph- and chapter numbering that could help.")

about_doc=nlp(text1)
sentences=list(about_doc.sents)
len(sentences)

for sentence in sentences:
    print(f"{sentence[:5]}...")
print("\n#############       Tokenization         ###############\n")

#tokenization

for token in about_doc:
    print(token,token.idx)
print("\n###############           Stop Words Removal       ###############\n")

#stop words removal

spacy_stopwords=spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
print()
for stop_word in list(spacy_stopwords)[:15]:
    print(stop_word)

print([token for token in about_doc if not token.is_stop])

print("\n###############          Lemmatization            ###############\n")

for token in about_doc:
    if str(token)!= str(token.lemma_):
        print(f"{str(token):>20}:{str(token.lemma_)}")

print("\n###############           Word Frequency       ###############\n")

words=[
    token.text
    for token in about_doc
    if not token.is_stop and not token.is_punct
]
print(Counter(words).most_common(5))

print("\n###############           Part_of_speech Tagging       ###############\n")

for token in about_doc:
    print(
        f"""
        TOKEN:{str(token)}
        =====
        TAG: {str(token.tag_):10} POS: {token.pos_}
        EXPLANATION: {spacy.explain(token.tag_)}"""
    )





'''
**********     OUTPUT     ****************


##########   Sentence Detection    ###############

Detecting Paragraphs is somehow less...
Mostly there is some custom...
Maybe there is some layout...

#############       Tokenization         ###############

Detecting 0
Paragraphs 10
is 21
somehow 24
less 32
mainstream 37
. 47
Mostly 48
there 55
is 61
some 64
custom 69
logic 76
like 82
: 86
split 88
after 94
two 100
line 104
- 108
ends 109
, 113
or 115
split 118
before 124
uppercased 131
title 142
. 147
Maybe 148
there 154
is 160
some 163
layout 168
- 174
meta 175
information 180
, 191
or 193
a 196
specific 198
paragraph- 207
and 218
chapter 222
numbering 230
that 240
could 245
help 251
. 255

###############           Stop Words Removal       ###############


twenty
became
ourselves
always
or
would
everything
seems
although
however
any
nevertheless
‘ll
i
next
[Detecting, Paragraphs, mainstream, ., custom, logic, like, :, split, line, -, ends, ,, split, uppercased, title, ., Maybe, layout, -, meta, information, ,, specific, paragraph-, chapter, numbering, help, .]

###############          Lemmatization            ###############

                  is:be
              Mostly:mostly
                  is:be
                ends:end
               Maybe:maybe
                  is:be

###############           Word Frequency       ###############

[('split', 2), ('Detecting', 1), ('Paragraphs', 1), ('mainstream', 1), ('custom', 1)]

###############           Part_of_speech Tagging       ###############


        TOKEN:Detecting
        =====
        TAG: NNP        POS: PROPN
        EXPLANATION: noun, proper singular

        TOKEN:Paragraphs
        =====
        TAG: NNPS       POS: PROPN
        EXPLANATION: noun, proper plural

        TOKEN:is
        =====
        TAG: VBZ        POS: AUX
        EXPLANATION: verb, 3rd person singular present

        TOKEN:somehow
        =====
        TAG: RB         POS: ADV
        EXPLANATION: adverb

        TOKEN:less
        =====
        TAG: RBR        POS: ADV
        EXPLANATION: adverb, comparative

        TOKEN:mainstream
        =====
        TAG: JJ         POS: ADJ
        EXPLANATION: adjective (English), other noun-modifier (Chinese)

        TOKEN:.
        =====
        TAG: .          POS: PUNCT
        EXPLANATION: punctuation mark, sentence closer

        TOKEN:Mostly
        =====
        TAG: RB         POS: ADV
        EXPLANATION: adverb

        TOKEN:there
        =====
        TAG: EX         POS: PRON
        EXPLANATION: existential there

        TOKEN:is
        =====
        TAG: VBZ        POS: VERB
        EXPLANATION: verb, 3rd person singular present

        TOKEN:some
        =====
        TAG: DT         POS: DET
        EXPLANATION: determiner

        TOKEN:custom
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:logic
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:like
        =====
        TAG: IN         POS: ADP
        EXPLANATION: conjunction, subordinating or preposition

        TOKEN::
        =====
        TAG: :          POS: PUNCT
        EXPLANATION: punctuation mark, colon or ellipsis

        TOKEN:split
        =====
        TAG: VB         POS: VERB
        EXPLANATION: verb, base form

        TOKEN:after
        =====
        TAG: IN         POS: ADP
        EXPLANATION: conjunction, subordinating or preposition

        TOKEN:two
        =====
        TAG: CD         POS: NUM
        EXPLANATION: cardinal number

        TOKEN:line
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:-
        =====
        TAG: HYPH       POS: PUNCT
        EXPLANATION: punctuation mark, hyphen

        TOKEN:ends
        =====
        TAG: NNS        POS: NOUN
        EXPLANATION: noun, plural

        TOKEN:,
        =====
        TAG: ,          POS: PUNCT
        EXPLANATION: punctuation mark, comma

        TOKEN:or
        =====
        TAG: CC         POS: CCONJ
        EXPLANATION: conjunction, coordinating

        TOKEN:split
        =====
        TAG: VBN        POS: VERB
        EXPLANATION: verb, past participle

        TOKEN:before
        =====
        TAG: IN         POS: ADP
        EXPLANATION: conjunction, subordinating or preposition

        TOKEN:uppercased
        =====
        TAG: JJ         POS: ADJ
        EXPLANATION: adjective (English), other noun-modifier (Chinese)

        TOKEN:title
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:.
        =====
        TAG: .          POS: PUNCT
        EXPLANATION: punctuation mark, sentence closer

        TOKEN:Maybe
        =====
        TAG: RB         POS: ADV
        EXPLANATION: adverb

        TOKEN:there
        =====
        TAG: EX         POS: PRON
        EXPLANATION: existential there

        TOKEN:is
        =====
        TAG: VBZ        POS: VERB
        EXPLANATION: verb, 3rd person singular present

        TOKEN:some
        =====
        TAG: DT         POS: DET
        EXPLANATION: determiner

        TOKEN:layout
        =====
        TAG: JJ         POS: ADJ
        EXPLANATION: adjective (English), other noun-modifier (Chinese)

        TOKEN:-
        =====
        TAG: HYPH       POS: PUNCT
        EXPLANATION: punctuation mark, hyphen

        TOKEN:meta
        =====
        TAG: JJ         POS: ADJ
        EXPLANATION: adjective (English), other noun-modifier (Chinese)

        TOKEN:information
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:,
        =====
        TAG: ,          POS: PUNCT
        EXPLANATION: punctuation mark, comma

        TOKEN:or
        =====
        TAG: CC         POS: CCONJ
        EXPLANATION: conjunction, coordinating

        TOKEN:a
        =====
        TAG: DT         POS: DET
        EXPLANATION: determiner

        TOKEN:specific
        =====
        TAG: JJ         POS: ADJ
        EXPLANATION: adjective (English), other noun-modifier (Chinese)

        TOKEN:paragraph-
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:and
        =====
        TAG: CC         POS: CCONJ
        EXPLANATION: conjunction, coordinating

        TOKEN:chapter
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:numbering
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:that
        =====
        TAG: WDT        POS: PRON
        EXPLANATION: wh-determiner

        TOKEN:could
        =====
        TAG: MD         POS: AUX
        EXPLANATION: verb, modal auxiliary

        TOKEN:help
        =====
        TAG: VB         POS: VERB
        EXPLANATION: verb, base form

        TOKEN:.
        =====
        TAG: .          POS: PUNCT
        EXPLANATION: punctuation mark, sentence closer


'''