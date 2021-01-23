# MSC2020 Tree

# generates a directory tree based on MSC2020, the Mathematical Sciences Classiﬁcation System in the revision 2020

import os
import re  # regular expressions
from typing import Any, Union


def main(filename):
    name_limit = 40 # limit of maximum name length (rest gets truncated)
    f = open(filename, "r", encoding='utf-8')
    level1 = re.compile(r"\d+")
    level2 = re.compile(r"([a-zA-Z-])+")

    for x in f:  # read line by line
        path = os.path.dirname(os.path.abspath(__file__))
      #  path = 'c:\\temp'
        path = os.path.join(path, 'tree') # start folder tree from dedicated folder
        print(x)

        line_split = x.split('_', 1)  # - separates class token from class name
        token = line_split[0]
        name = line_split[1]
        name = name.replace("\n", "")
        name = name[0:name_limit]

        l1 = level1.match(token)
        l1_token = l1.group(0)
        token_rest = token[l1.end(0):]
        l1_int = int(l1_token)

        if l1_int <=3:
            area = '00-03-Foundation'
        elif l1_int <=22:
            area = '05-22-Algebra'
        elif l1_int <= 49:\
            area = '26-49-Analysis'
        elif l1_int <= 58:\
            area = '51-58-Geometry'
        elif l1_int <= 62:\
            area = '60-62-Statistics'
        elif l1_int <= 68:\
            area = '65-68-Computer_Science'
        elif l1_int <= 94:
            area = '70-94-Applications'
        elif l1_int <= 97:
            area = '97-97-Education'
        else:
            area = '99-Others'
        path = os.path.join(path, area)

        if len(token_rest) == 0:
            path = os.path.join(path, l1_token + '_' + name) # single level case
        else:
            dirs = os.listdir(path)
            found = False # init flag
            for dir_name in os.listdir(path):
                if dir_name.startswith(l1_token):
                    path = os.path.join(path, dir_name)
                    found = True
                    break
            if not found:
                print('Token not recognized (l1 dir not found: ',token)
                continue  # with next line of file
            l2 = level2.match(token_rest)
            if l2 is None:
                print('Token not recognized (l2 is None): ',token)
                continue # with next line of file
            l2_token = l2.group(0)
            token_rest = token_rest[l2.end(0):]
            l3_token = token_rest
            if len(token_rest) == 0:
                path = os.path.join(path, l1_token + l2_token + '_' + name)  # single level case
            else:
                if l2_token == '-':  # do not add a hierarchy level for levels with '-'
                   # l2_token = ''
                   path = os.path.join(path, '-')
                else:
                    dirs = os.listdir(path)
                    found = False  # init flag
                    for dir_name in os.listdir(path):
                        if dir_name.startswith(l1_token + l2_token):
                            path = os.path.join(path, dir_name)
                            found = True
                            break
                    if not found:
                        print('Token not recognized (l2 dir not found): ', token)
                        continue  # with next line of file

                if l3_token != '':
                    path = os.path.join(path, l1_token + l2_token + l3_token + '_' + name)

        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except:
                print("Creation of the directory %s failed" % path)

    f.close()

# run the main function
if __name__ == '__main__':
    main("msc2020.txt")
