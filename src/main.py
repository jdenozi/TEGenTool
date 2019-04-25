#!/bin/env python3
#import vcfobject
import parsevcf
import vcfobject
import time
import sys 
import os
import argparse
ObjectVcf=vcfobject.ObjectVcf
ParseVcf=parsevcf.ParseVcf

###############
###Arguments###
###############*

parser = argparse.ArgumentParser(description='TE Gen Tool')
parser.add_argument('-f','--file',
                   help='File to process')
parser.add_argument('-c','--clean', type=int, help='Remove nested TE, with values of nested' )
parser.add_argument('file')

args = parser.parse_args()
if args.file:
	list_objvcf=[]
	for dir,subdir,files in os.walk(args.file):
		[list_objvcf.append(ObjectVcf(0,dir,file)) for file in files]
	for objvcf in list_objvcf:
		objvcf.dataConvert()
		if args.clean:
			objvcf.removeNestedTE(1,args.clean)
		if not args.clean:
			objvcf.removeNestedTE(1)

