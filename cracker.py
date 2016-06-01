#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zipfile
import argparse

def extract_file(zipFile, password):
    try:
        zipFile.extractall(pwd=password)
        return password
    except:
        return None

def main():
    parser = argparse.ArgumentParser(description='Zip Paassword Cracker')
    parser.add_argument('-f', '--zipFile', dest='zipFile', help='specify zip file')

    parser.add_argument('-d', '--dictionaryFile', dest='dictionaryFile', help='specify dictionary file')

    args = parser.parse_args()
    if (args.zipFile is None) and (args.dictionaryFile is None):
        parser.print_help()
        exit(0)
    else:
        zname = args.zipFile
        dname = args.dictionaryFile
    zipFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extract_file(zipFile, password)
        if guess:
            print('Found password: ' + password)
            exit(0)



if __name__ == '__main__':
    main()