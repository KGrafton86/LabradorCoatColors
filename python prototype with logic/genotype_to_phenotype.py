# labrador coat colors tool
# Carolyn R Grafton 2021
# this is for practice in python and is not intended to be released

from sys import argv

# function to split input into the separate genes 
# (does not check/sanitize the input)
def split_genes(genotype):
	b_gene = genotype[0:2]
	e_gene = genotype[2:4]
	d_gene = genotype[4:6]
	return (b_gene, e_gene, d_gene)

# check if dog is dilute
def dilute_check(d_gene):
	return d_gene == "dd"
		

# get the dog's standard color from the B and E genes
def puppy_color(b_gene, e_gene, d_gene):
	color = None
	dilute = dilute_check(d_gene)
	if e_gene == "ee":
		standard_color = "yellow"
		if dilute == True:
			standard_color = "dilute " + standard_color
			color = "champagne"
		elif dilute != True:
			color = "yellow"
		else: 
			print("wtf is this how did you get here? error GtP2")
		# if b_gene == "bb":	# 'dudley' is an incorrectly-used slang term, 'liver pigment' is correct
			# # standard_color += " (liver pigment)" 
			# color += " (liver pigment)"
	elif b_gene == "bb":
		standard_color = "chocolate"
		if dilute == True:
			standard_color = "dilute " + standard_color
			color = "silver"
	elif b_gene == "Bb" or b_gene == "BB":
		standard_color = "black"
		if dilute == True:
			standard_color = "dilute " + standard_color
			color = "charcoal"
	else: 
		print("wtf is this how did you get here? error GtP1")
	if color is None:
		color = standard_color
	return (standard_color, color, dilute)


# MAIN CODE BODY
def genotype_to_phenotype(genotype):
	# split into individual genes
	b_gene, e_gene, d_gene = split_genes(genotype)
	
	# find the dog's color
	standard_color, color, dilute = puppy_color(b_gene, e_gene, d_gene)
	return (standard_color, color, dilute)

		
# run main code
# genotype_to_phenotype()