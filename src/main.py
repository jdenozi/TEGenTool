#!/bin/env python3
#import vcfobject
import parsevcf
import vcfobject
import time
import sys 
ObjectVcf=vcfobject.ObjectVcf
ParseVcf=parsevcf.ParseVcf
bob=ObjectVcf("0","essais.vcf")
bob.dataConvert()
