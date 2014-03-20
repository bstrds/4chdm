#!/usr/bin/env python2

from os import path
import sys
import wordcloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, '4chdata/all.dat')).read()
# Separate into a list of (word, frequency).
words = wordcloud.process_text(text, max_features=1000)
# Compute the position of the words.
elements = wordcloud.fit_words(words, width=1000, height=1000)
# Draw the positioned words to a PNG file.
wordcloud.draw(elements, path.join(d, 'mu4.png'), width=1000, height=1000,
        scale=2)
