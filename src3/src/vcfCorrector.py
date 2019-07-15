#!/bin/env python3
import re 
from numpy.polynomial.polynomial import Polynomial
from numpy import *
import numpy as np
from scipy.interpolate import lagrange



def vcfCorrector(dataframe, lenfile):
	for i in dataframe:
		pass
		
	
#Calcul la probabilioté d'erreur d'annotation (30,0) (15,0.1) (5,0.5) (0,1)
dp=array([100, 50, 25, 0])
dpx=array([0, 0.5, 0.75, 1])
p=lagrange(dp,dpx)
print(p(5))
