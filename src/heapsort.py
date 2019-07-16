#!/bin/env python3
import sys
import parsevcf
import random
import vcfobject
from vcfobject import * 



#################
###HEAPSORT######
#################

#Permet de trier la liste des insertions en O(nlog(n)) en temps et O(1) en espace
#en comparant CHROM POS ID (avec la surcharge des opérateur)

count=0
sys.setrecursionlimit(100000)
def heapSort(liste):
	global count
	longueur=len(liste)
	for i in range(longueur, -1, -1):
		count+=1
		switch(liste, longueur, i)
	for i in range((longueur-1),-1,-1):
		count+=1
		tmp=liste[i]
		liste[i]=liste[0]
		liste[0]=tmp
		switch(liste,i,0)
def switch(liste,longueur, i):
	global count
	noeud=i
	enfantdroit=i*2+2
	enfantgauche=i*2+1
	if enfantgauche < longueur and liste[i] < liste[enfantgauche]: 
		noeud = enfantgauche
	if enfantdroit < longueur and liste[noeud] < liste[enfantdroit] :
		noeud = enfantdroit
	if noeud != i:
		tmp=liste[i]
		liste[i]=liste[noeud]
		liste[noeud]=tmp
		switch(liste,longueur,noeud)
		count+=1
