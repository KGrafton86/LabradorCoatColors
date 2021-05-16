# labrador coat colors tool
# to test script using each of the possible genotypes
# to run this need to comment out the line in lab_coat_colors that runs the main function

from genotype_to_phenotype import split_genes, puppy_color
from sys import exc_info

# [genotype, phenotype]
genotypes = [["BBEEDD", "black"],
			 ["BBEEDd", "black"],
			 ["BbEEDD", "black"],
			 ["BbEEDd", "black"],
			 ["BBEeDD", "black"],
			 ["BBEeDd", "black"],
			 ["BbEeDD", "black"],
			 ["BbEeDd", "black"],
			 ["BBeeDD", "yellow"],
			 ["BBeeDd", "yellow"],
			 ["BbeeDD", "yellow"],
			 ["BbeeDd", "yellow"],
			 ["bbeeDD", "yellow"],
			 ["bbeeDd", "yellow"],
			 ["bbEEDD", "chocolate"],
			 ["bbEEDd", "chocolate"],
			 ["bbEeDD", "chocolate"],
			 ["bbEeDd", "chocolate"],
			 ["BBEEdd", "charcoal"],
			 ["BbEEdd", "charcoal"],
			 ["BBEedd", "charcoal"],
			 ["BbEedd", "charcoal"],
			 ["BBeedd", "champagne"],
			 ["Bbeedd", "champagne"],
			 ["bbeedd", "champagne"],
			 ["bbEEdd", "silver"],
			 ["bbEedd", "silver"]]
			 
one_genotype = [["bbEEdd", "silver"]]

def test_all_genotypes():
	for genotype in genotypes:
		phenotype = genotype[1]
		genotype = genotype[0]
		try:
			b_gene, e_gene, d_gene = split_genes(genotype)
			color = ""
			standard_color, color = puppy_color(b_gene, e_gene, d_gene)
			output = color
		except KeyboardInterrupt:
			raise
		except Exception:
			output = str(exc_info()[0]) # gets error type
			result = ""
		else: 
			if color == phenotype:
				result = "match"
			elif color != phenotype: 
				result = "MISMATCH"
			else: 
				result = "wtf is this how did you get here code:TAG1"
		print("genotype: " + genotype + "\tphenotype: " + phenotype + "\toutput: " + output + "\tresult: " + result)	
		
# run main code
test_all_genotypes()
