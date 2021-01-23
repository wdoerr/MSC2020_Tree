# MSC2020_Tree
Directory Tree based on the Mathematical Sciences Classiﬁcation System

The main usage is to download the .zip file and unzip it.
It contains an empty directory structure following MSC2020.

This repository contains the code to generate it in folder '../Code'.
That code generates a folder '../Code/Tree' which is also located in the .zip file.

The code does the following alteration compared to the original MSC2020:
- brackets with their content (the comments) removed 
- space converted to '_'
- ';' converted to '_and_'
- ''' converted to ''
- '*' converted to 'star'
- '_and_etc._' converted to '-'
- '_and_etc.\r' removed (at end of line)
- '_and_e.g.' removed
- '_.' removed
- ':' removed
- '>' converted to 'greater'
- 'p.i.' converted to 'p_i_'
- '(Co)' converted to 'Co'
- some more convertions (not tracked)
- long lines got shortened, found with notepad++ regular expression: ^.{80,1000}\r) 
- class names are truncated to 40 characters

