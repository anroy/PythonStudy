import nltk
text = "This is Andrew's text, isn't it?"

tok1 = nltk.tokenize.WhitespaceTokenizer()
print (tok1.tokenize(text))

tok2 = nltk.tokenize.TreebankWordTokenizer()
print (tok2.tokenize(text))

tok3 = nltk.tokenize.WordPunctTokenizer()
print (tok3.tokenize(text))