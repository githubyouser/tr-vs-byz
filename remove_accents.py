# Original source: https://github.com/djemos/remove_accents.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
python_version = sys.version_info.major
if python_version == 3:
	import importlib
	importlib.reload(sys) 
	import re
	import unicodedata
else:
	reload(sys) 
	sys.setdefaultencoding("utf-8")
	import re
	import unicodedata
	str=unicode

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn').lower()

def help():
	print('usage: python ./remove_accents.py polytonic_file monotonic_file')
	text=str("Ὦ κοινὸν αὐτάδελφον Ἰσμήνης κάρα,")
	print(strip_accents(text))
	sys.exit(1)
        
def main(args):
	if len(sys.argv) >=3:
		f= open(sys.argv[1], 'r', encoding="utf-8")		
		text= str(f.read())
		f.close()

		f= open(sys.argv[2], 'w', encoding="utf-8")
		f.write(strip_accents(text))
		f.close()
	else:
		help()

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
