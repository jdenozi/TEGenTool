#!/bin/bash
for F in *.vcf 
do 
	vcf-sort $F | bgzip -c > ${F}.gz;
	tabix -p vcf ${F}.gz; 
	
done
vcf-merge `ls *.gz` > out.vcf;
