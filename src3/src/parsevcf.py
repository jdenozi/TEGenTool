#!/bin/env python3
import re
def endInfo(info):
	return re.search("(END)=(\d+)",info)[2]
def mqInfo(info):
	return re.search("(MQ)=(\d+)",info)[2]

def dpInfo(info):
	return re.search("(DP)=(\d+)",info)[2]
		
##############
###PARSEVCF###
##############
#Class which parse every line by vcf column
#
#
#
class ParseVcf:
	
	def __init__(self,line,gen):
		self.chrom=""
		self.pos=0
		self.id=""
		self.ref=""
		self.alt=""
		self.qual=""
		self.filter=""	
		self.mq=""
		self.dp=""
		self.posend=""
		self.gen=[]
		self.gen.append(gen)
		self.parse(line)
	####################
	#OPERATOR SURCHARGE#						
	####################
	#Which allow to compare two ParseVcf Object
	#using chromosome and position attribute
####################################	
	def __lt__(self,vcfobject):
		for i,j in zip(self.chrom,vcfobject.chrom):
			if i>j:
				return False
		if self.pos < vcfobject.pos:
			return True
		else:
			return False

####################################
	def __get__(self,vcfobject):
		for i,j in zip(self.chrom,vcfobject.chrom):
			if i<j:
				return True
		if self.pos > vcfobject.pos:
			return True
		else:
			return False


###################################
	def __eq__(self,vcfobject):
		for i,j in zip(self.chrom, vcfobject.chrom):
			if i!=j:
				return False
		if self.pos == vcfobject.pos:
			return True
		else:
			return False


##################################
##################################

	#######
	#PARSE#
	#######
	#function used to parse every single vcf line
	#calling in ParseVCf constructor
	#which provide check list 
	def parse(self,line):
		try:
			parseline=line.split("	")
			self.chrom=parseline[0]
			self.pos+=int(parseline[1])
			self.id=parseline[2]
			self.ref=parseline[3]
			self.alt=parseline[4]
			self.qual=parseline[5]
			self.filter=parseline[6]
			try:
				self.mq=mqInfo(parseline[7])
			except: 
				self.mq="None"
			try : 
				self.dp=dpInfo(parseline[7])
			except:
				self.dp="None"
				
			try:
				self.posend=endInfo(parseline[7])
			except:
				self.posend="None"
			
		except:
			print("Data corrupted")

	def iterAttribute(self):
		return iter(self.__dict__.values())

