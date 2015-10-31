#! python
import sys
import numpy
import nltk
import pip

sys.stdout.write("Python version: %s\n" % (sys.version,))
sys.stdout.write("numpy version: %s\n" % (numpy.__version__,))
sys.stdout.write("nltk version: %s\n" % (nltk.__version__,))
sys.stdout.write("pip version: %s\n" % (pip.__version__,))
