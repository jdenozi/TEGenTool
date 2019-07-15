nbfichier=1
nbinsertion=10
nom="name"

for i in range(0,nbfichier,1):
	with open(nom+str(i)+".vcf", "w") as fichier:
		count=0
		for  j in range(0,nbinsertion,1):
			count=count+45
			fichier.write("0\t"+ str(count)+"\t" + ".	A	G	129.03	.	AC=2;AF=1.00;AN=2;DP=4;ExcessHet=3.0103;FS=0.000;MLEAC=2;MLEAF=1.00;MQ=35.36;QD=32.26;SOR=1.609	GT:AD:DP:GQ:PL	1/1:0,4:4:12:157,12,0 \n")
