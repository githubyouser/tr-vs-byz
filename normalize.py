import sys
import unicodedata
import re

# Source: https://github.com/nlpaueb/greek-bert#pre-process-text-deaccent---lower
def strip_accents_and_lowercase(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn').lower()          

with open(sys.argv[1], "r", encoding="utf-8") as input:
    with open(sys.argv[2], "x", encoding="utf-8") as output:
        for line in input:
            clean = strip_accents_and_lowercase(line)
            clean = re.sub("\#.*\\n", '', clean)              # remove header info from TR text
            clean = re.sub('[0-9]+,[0-9]+,', '', clean)       # remove chapter/verse numbers from BYZ text
            clean = re.sub('chapter,verse,text\n', '', clean) # remove CSV headers from BYZ text
            clean = re.sub('[0-9]+ ', '', clean)              # remove numbers from TR text
            clean = re.sub("[.,'·:;ʼ!\"]", '', clean)         # strip all punctuation
            output.write(clean)