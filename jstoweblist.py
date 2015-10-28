#! /usr/bin/env python2.7

import os

def main():
    try:
        filename = raw_input("Full path to file you would like html friendly?:")
        print "Converting %s in %s to html code..."% (filename,os.getcwd())
        beconvert = open(filename,"r").readlines()
        output = open("%s-converted"%filename,'w')
        w = ["<li><span><xmp>"+x.replace("\n","")+"</xmp></li></span>\n" for x in beconvert]
        output.write(''.join(w))
        output.close()
    except Exception as e:
        print e

if __name__ == '__main__':
    main()
