#!/usr/bin/python
#
# this script generates markdown bullet point links from a vimprobable bookmarks file
# author: ameba23

# usage:  linkmarkdown [keytag] outfile
# Lines will be appended to output file only if there is not already a line with that url already in output file.
# If keytag is specified, only bookmarks containing this keytag will be added.

import sys

def setTask():

    if (len(sys.argv) > 2):
        outfile = open(sys.argv[2], 'a+')
    #print '# unsorted links'
    #print 'This a list of links directly generated from my bookmarks'
    #print
    if (len(sys.argv) > 1):
        findtag = sys.argv[1]
    else:
        findtag = ''
    input = open('/home/carrot/.config/vimprobable/bookmarks','r')
    lines = input.readlines()
    input.close()
    taskNum = len(lines)
    for i in range(taskNum):
       if (lines[i].find(findtag) != -1):
        #splitlines = lines[i].split('|')
        splitlines = lines[i].split()
        markdownline = '* ['
        tags = 'Tags:'
        for ii in range(len(splitlines)-1):
            if (splitlines[ii+1] != '|'):
              if (splitlines[ii+1][0] == '['):
                  if (splitlines[ii+1] != ('[' + findtag + ']')):
                    tags = tags + ' ' + splitlines[ii+1].strip('[]')
              else:
                markdownline = markdownline + splitlines[ii+1] 
                if (ii < (len(splitlines)-3)):
                    markdownline = markdownline + ' '
        # if there is no title, let the title be the url
        if markdownline == '* [': markdownline = markdownline + splitlines[0]
        markdownline = markdownline + '](' + splitlines[0] + ') ' + tags + '\n'
        if (len(sys.argv) < 3):
            print markdownline 
        else:
            exists = 0
            outfile.seek(0, 0)
            for line in outfile:
                if splitlines[0] in line: 
                    exists=1
            if exists == 0: outfile.write(markdownline)
    if (len(sys.argv) > 2):
        outfile.close()


setTask()

