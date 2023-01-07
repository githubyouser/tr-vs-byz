# tr-vs-byz
## A comparison between the Byzantine Textform and the KJV Textus Receptus

* [Textus Receptus source](https://github.com/Center-for-New-Testament-Restoration/KJTR/blob/main/KJTR.txt)  
* [Byzantine text source](https://github.com/byztxt/byzantine-majority-text/tree/master/csv-unicode/accents/no-variants)

All the accents and uppercase letters were stripped using `remove_accents.py` (adapted from [djemos/remove_accents.py](https://github.com/djemos/remove_accents.py/blob/master/remove_accents.py))  
Punctuation `[.,'·:;ʼ!]` was also stripped.  

Unfortunately, Github can't compare files this large, so you'll have to view the comparison [somewhere else](https://cmp.mrgreekgeek.com/). 

The comparison was made using [Diff2HtmlUI](https://github.com/rtfpessoa/diff2html#diff2htmlui-examples)  
* Generate a diff file `git diff file1 file2 > compared.diff` 
* Copy/paste the contents of the diff file into the sample found [here](https://github.com/rtfpessoa/diff2html#diff2htmlui-examples) (right after `const diffString =`)
