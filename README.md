# A comparison between the Byzantine Textform and the KJV Textus Receptus

## Source Files

* [Textus Receptus source](https://github.com/Center-for-New-Testament-Restoration/KJTR/blob/main/KJTR.txt)  
* [Byzantine text source](https://github.com/byztxt/byzantine-majority-text/tree/master/csv-unicode/accents/no-variants)

## Cleaning up the files

The files need to be normalized so that we can compare *just* the Greek text itself. We need to do the following:
* Strip all Greek polytonic accents and breathing marks
* Remove the header information from the files
* Remove all book/chapter/verse numbers
* Remove all punctuation

## Usage
Just run `python normalize.py <input_filename> <output_filename>` to clean up a file.

After running `normalize.py` on each of the original files, we have 2 clean files that can be directly compared as a diff.   

`git diff KJTR.txt BYZ.txt > compared.diff`  

The contents of `compared.diff` file can be copy/pasted into the [*diff2htmlui* template](https://github.com/rtfpessoa/diff2html#diff2htmlui-examples). This gives you a standalone, stacic HTML file that can be hosted anywhere. 

Or you can use SSI to include the diff file into the template instead of copy/pasting: `<!--#include virtual="comp.diff" -->`

## Viewing
**https://cmp.mrgreekgeek.com/**

Now you can view the file in your favorite web browser! It's pretty big, so it takes a lot of resources. 
