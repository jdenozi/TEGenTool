#!/bin/env python3
import pandas as pd
import parsevcf

ParseVcf=parsevcf.ParseVcf

############
###IMPORT###
############
class ObjectVcf:
	
	def __init__(self, generation, filename):
		self.generation=generation
		self.filename=filename
		self.header=""
		self.chromosome=[]
		self.readFile()

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

	def readFile(self):
		try : 
			with open(self.filename,"r") as file:
				chrom=""
				for line in  file.readlines():
					info=[]
					first_char=line[0]	
					if first_char=="#":
						self.header+=line
					else:
						parseline=ParseVcf(line)
						row=[]
						[row.append(attribute)for attribute in parseline.iterAttribute()]	
						self.chromosome.append(row)
		except FileNotFoundError:
			print("File not found")
		except ValueError :
			print("Could not convert int to string")
			

	def dataConvert(self):
		dataframe=pd.DataFrame.from_records(self.chromosome, columns=["Chrom", "Pos", "Id", "Ref", "Alt", "Qual", "Filter", "Info"])
		print(dataframe)
