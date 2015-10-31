#! python
import nltk
import sys

sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
tokens = nltk.word_tokenize(sentence)
sys.stdout.write("tokens: %s\n" % (tokens,))

tagged = nltk.pos_tag(tokens)
sys.stdout.write("tagged: %s\n" % (tagged,))

entities = nltk.chunk.ne_chunk(tagged)
sys.stdout.write("entities: %s\n" % (entities,))
