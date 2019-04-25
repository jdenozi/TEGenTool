#!/bin/env python3
import re
def endInfo(info):
	return re.search("(END)=(\d+)",info)[2]
		

class ParseVcf:
	
	def __init__(self,line):
		self.chrom=""
		self.pos=""
		self.id=""
		self.ref=""
		self.alt=""
		self.qual=""
		self.filter=""	
		self.info=""
		self.posend=""
		self.parse(line)
	def parse(self,line):
		try:
			parseline=line.split("	")
			self.chrom=parseline[0]
			self.pos=parseline[1]
			self.id=parseline[2]
			self.ref=parseline[3]
			self.alt=parseline[4]
			self.qual=parseline[5]
			self.filter=parseline[6]
			self.info=parseline[7]
			try:
				self.posend=endInfo(self.info)
			except:
				self.posend("None")
			
		except:
			print("Data corrupted")

	def iterAttribute(self):
		return iter(self.__dict__.values())

		

