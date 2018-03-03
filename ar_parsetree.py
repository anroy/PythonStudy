#! python
from nltk.corpus import treebank
# import sys

t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()