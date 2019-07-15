#!/bin/env python3
def removeNestedTE(listobj,value):
	listcleaned=[]
	tmp=listobj[0]
	listcleaned.append(tmp)	
	print("value",value)	

	for i in range(1,len(listobj),1):
		if tmp.gen[0]==listobj[i].gen[0]:
			if tmp.posend is None :
				print("value",tmp.posend)	

				if tmp.chrom==listobj[i].chrom and listobj[i].pos - int(tmp.posend)>value:
					tmp=listobj[i]
					listcleaned.append(tmp)
				
				
			if tmp.chrom==listobj[i].chrom and listobj[i].pos - tmp.pos>value:
				tmp=listobj[i]
				listcleaned.append(tmp)
		else:
			tmp=listobj[i]
			listcleaned.append(tmp)

	return listcleaned 	
			

