#! python
import nltk
import sys

# sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
sentence = "Now is the time for all good men to come to the aid of the party."

tokens = nltk.word_tokenize(sentence)
sys.stdout.write("tokens: %s\n" % (tokens,))

tagged = nltk.pos_tag(tokens)
sys.stdout.write("tagged: %s\n" % (tagged,))

entities = nltk.chunk.ne_chunk(tagged)
sys.stdout.write("entities: %s\n" % (entities,))