
Convert an input file, containing one word per line, to a file containing several columns
per page.

A page is filled is this way: the first column is filled first, then the second column
is filled, then the third, etc.

If there are not enough words on the last page, the last column might be shorter than
other columns.

Example of the output:

```
word-1 word-5 word-9 word-13
word-2 word-6 word-10
word-3 word-7 word-11
word-4 word-8 word-12
```
