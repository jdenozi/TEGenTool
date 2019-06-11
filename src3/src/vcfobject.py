#!/bin/env python3
import re
import parsevcf
import os
import webbrowser
import time
import sys
import pandas as pd
from dataframeMethods import NumberTeType
from dataframeMethods import ETDynamicOverGenerations
from dataframeMethods import insertionOverGenerations
from operator import itemgetter
from heapsort import heapSort
from nestedte import removeNestedTE
from progressbar import ProgressBar
import warnings
warnings.filterwarnings("ignore")
#from heapsort import permute
ParseVcf=parsevcf.ParseVcf
sys.setrecursionlimit(1000)
def extensionCheck(filename):
		if re.search("(.vcf)$",filename)!=None:
			return True
		else:
			return False

##################
#CLASSE OBJECTVCF#
##################	

class ObjectVcf:
	
	def __init__(self,path, value=0):
		self.path=path
		self.gen=""
		self.header=""
		self.readFile(path, value)
		self.dataframe=""

	##########
	##GETTER##
	##########
	def getGeneration(self):
		return self.generation
	
	def getFilename(self):
		return self.filename

	def getHeader(self):
		return self.getHeader
	##########
	##SETTER##
	##########

	def setGeneration(self, new_generation):
		self.generation=new_generation
	
	def setFilename(self, new_filename):
		self.filename=new_filename
	
	def setHeader(self, new_header):
		self.header=new_header

	#################
	##CLASS METHODS##
	#################	
				
	##########
	#READFILE#
	##########
	#Read all VCF files
	#Parse each vcf column with parsevcf class 
	#Concat each Vcf line in one list
	def readFile(self,path,value):
		liste=[]
		columns=["Chrom", "Pos", "Id", "Ref", "Alt", "Qual", "Filter", "MQ","DP", "PosEnd", "Génération"]
		counter=0
		for dir, subdir,files in os.walk(path):
			barre=ProgressBar(len(files),title="Reading files ...")
			for i in range(0,len(files),1):
				barre.update()
				file=files[i]
				try : 
					if extensionCheck(file) is True:
						with open(path+file,"r") as file:
							chrom=""
							for line in  file.readlines():
								first_char=line[0]	
								if first_char=="#":
									self.header+=line
								else:
									#try : 
									parseline=ParseVcf(line,i)
									liste.append(parseline)
					else:				
						break
						print("One or several files have the wrong extension.Please remove this files.")
				except FileNotFoundError:
					print("File not found")
				except ValueError :
					print("Could not convert int to string")
		print("\nReading files done")
		listecopy=[]	
		print("\nNombre d'insertion avant nettoyages des éléments imbriqués",len(liste))
		liste=removeNestedTE(liste, value)
		debut=time.time()
		heapSort(liste)
		fin=time.time()
		print(fin-debut)
		
		print("Nombre d'insertion après nettoyages des éléments imbriqués",len(liste))

		tmp=liste[0]
		for i in range(0,len(liste),1):
			if listecopy:
				if tmp.chrom==liste[i].chrom and tmp.pos==liste[i].pos:
					tmp.gen.append(liste[i].gen[0])
					heapSort(tmp.gen)
				else:
					info=[]
					[info.append(j)for j in liste[i].iterAttribute()]
					listecopy.append(info)
					tmp=liste[i]
			else:
				info=[]
				[info.append(j)for j in liste[i].iterAttribute()]
				listecopy.append(info)
				tmp=liste[0]	
		print(len(listecopy[0]))
		dataframe=pd.DataFrame(listecopy, columns=columns)
		print("ok")
		#print(dataframe.head(10))
		print("Compression: gain de ", len(liste)-len(listecopy))
		#NumberTeType(dataframe)
		ETDynamicOverGenerations(dataframe)
		insertionOverGenerations(dataframe)
		#webbrowser.open(os.getcwd()+"/webpage/home.html")	
	
