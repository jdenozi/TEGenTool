#!/bin/env python3
import re
import pandas as pd
import parsevcf

ParseVcf=parsevcf.ParseVcf

############
###IMPORT###
############
class ObjectVcf:
	
	def __init__(self, generation, path,filename):
		self.generation=generation
		self.filename=filename
		self.header=""
		self.chromosome=[]
		self.readFile(path)
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

	def readFile(self,path):
		try : 
			with open(path+self.filename,"r") as file:
				chrom=""
				for line in  file.readlines():
					info=[]
					first_char=line[0]	
					if first_char=="#":
						self.header+=line
					else:
						try : 
							parseline=ParseVcf(line)
							row=[]
							[row.append(attribute)for attribute in parseline.iterAttribute()]	
							self.chromosome.append(row)
						except:
							pass
		except FileNotFoundError:
			print("File not found")
		except ValueError :
			print("Could not convert int to string")
			

	def dataConvert(self):
		self.dataframe=pd.DataFrame.from_records(self.chromosome, columns=["Chrom", "Pos", "Id", "Ref", "Alt", "Qual", "Filter", "Info", "PosEnd"])
		self.dataframe.Pos=pd.to_numeric(self.dataframe.Pos)		
		self.dataframe.PosEnd=pd.to_numeric(self.dataframe.PosEnd)


def removeNestedTE(listeobj,value=0):
	for objvcf in listeobj:
		objvcf.dataConvert()
		print(objvcf.dataframe)
		for index in range(1, len(objvcf.dataframe),1):
			print(index)
			
			current_row=objvcf.dataframe.loc[index]
			previous_row=objvcf.dataframe.loc[index-1]
				
			if current_row.Pos<=previous_row.PosEnd:
				if (previous_row.PosEnd-current_row.Pos)<=value:
					pass
				else:
					objvcf.dataframe.drop(index, inplace=True)
					
			else:
				pass
			
			
		
