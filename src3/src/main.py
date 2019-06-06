#!/bin/env python3
#import vcfobject
import parsevcf
import vcfobject
import time
import sys 
import os
import time
import argparse
ObjectVcf=vcfobject.ObjectVcf
ParseVcf=parsevcf.ParseVcf
###############
###Arguments###
###############*
debut = time.time()
parser = argparse.ArgumentParser(description='TE Gen Tool')
parser.add_argument('-d','--directory',help='Directory')
parser.add_argument('-o','--overlap', type=int, help='Remove nested TE, 20 is hardly recommended' )

args = parser.parse_args()
if args.directory:
	if args.overlap:
		ObjectVcf(args.directory, args.overlap)
	else:
		ObjectVcf(args.directory)
else:
	print("Please path directory must be mentionned")
	"""
	list_objvcf=[]
	for dir,subdir,files in os.walk(args.file):
		[list_objvcf.append(ObjectVcf(0,dir,file)) for file in files]
	if not list_objvcf:
		raise FileNotFoundError("An error occurred with you file path")
	if args.clean:
		vcfobject.removeNestedTE(list_objvcf,args.clean)
	if not args.clean:
		vcfobject.removeNestedTE(list_objvcf)
	[print(vcf.dataframe)for vcf in list_objvcf]
	"""

fin=time.time()
print(fin-debut)
