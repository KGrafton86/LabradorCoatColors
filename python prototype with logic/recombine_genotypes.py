# labrador coat colors tool
# Carolyn R Grafton 2021
# this is for practice in python and is not intended to be released

from itertools import product

def split_genes(genotype):
	genotype = (genotype[0:2], genotype[2:4], genotype[4:6])
	return (genotype)

# sire = 'BbeeDd'
# dam = 'bbEEdd'

# splits and recombines an individual gene into all possible combinations
def recombine_gene(sire, dam):
	genes = list(product(sire, dam))
	genelist = []
	for i in genes:
		genelist.append(''.join(sorted(i)))
	return(genelist)

# splits and recombines a genotype into all possible combinations
def recombine_genotype(sire, dam):
	sire = split_genes(sire)
	dam = split_genes(dam)
	B = recombine_gene(sire[0], dam[0])
	E = recombine_gene(sire[1], dam[1])
	D = recombine_gene(sire[2], dam[2])
	genes = list(product(B, E, D))
	genelist = []
	for i in genes:
		genelist.append(''.join(i))
	return(sorted(genelist))

# offspring = recombine_genotype(sire, dam)
# print(offspring)