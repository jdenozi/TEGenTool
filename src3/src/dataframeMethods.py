#!/bin/env python3
import pandas as pd
import numpy as np
from collections import Counter
from  itertools import chain
#####################
##DATAFRAME METHODS##
#####################

def NumberTeType(dataframe):
	liste=dataframe["Id"].value_counts()
	with open("../webpage/jsonFiles/numberTeType.json","w") as file:
		file.write("numberTeType='"+liste.to_json()+"';")

def ETDynamicOverGenerations(dataframe):
	df = pd.Series(Counter(chain(*dataframe["Génération"]))).sort_index().rename_axis('Génération').reset_index(name='values')
	with open("../webpage/jsonFiles/etDynamicOverGenerations.json","w") as file:
		file.write("etDynamicOverGenerations='"+df.to_json()+"';")
def insertionOverGenerations(dataframe):
	for i in dataframe["Génération"]:
		for j in range(1, len(i),1):
			i.pop(j)	 
	df = pd.Series(Counter(chain(*dataframe["Génération"]))).sort_index().rename_axis('Génération').reset_index(name='values')
	with open("../webpage/jsonFiles/insertionOverGenerations.json","w") as file:
		file.write("insertionOverGenerations='"+df.to_json()+"';")

def correctedFile(dataframe):
	print("ok")
