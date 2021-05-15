# labrador coat colors tool
# Carolyn R Grafton 2020
# this is for practice in python and is not intended to be released
# will change and morph as I know more python

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
	if e_gene == "ee":
		standard_color = "yellow"
		if dilute_check(d_gene) == True:
			standard_color = "dilute " + standard_color
			color = "champagne"
		# if b_gene == "bb":	# 'dudley' is an incorrectly-used slang term, 'liver pigment' is correct
			# standard_color += " (liver pigment)" 
			# color += " (liver pigment)"
	elif b_gene == "bb":
		standard_color = "chocolate"
		if dilute_check(d_gene) == True:
			standard_color = "dilute " + standard_color
			color = "silver"
	elif b_gene == "Bb" or b_gene == "BB":
		standard_color = "black"
		if dilute_check(d_gene) == True:
			standard_color = "dilute " + standard_color
			color = "charcoal"
	else: 
		print("wtf is this how did you get here LLC2")
	if color is None:
		color = standard_color
	return (standard_color, color)


# MAIN CODE BODY
def genotype_to_phenotype():
	# get genotype as input
	print("Enter puppy genotype (order: B,E,D): ")
	genotype = input()
	b_gene, e_gene, d_gene = split_genes(genotype)
	print("genotype: " + genotype)
	print("genes: " + b_gene + ", " + e_gene + ", " + d_gene)
	
	# find the puppy's color
	# color = ""
	standard_color, color = puppy_color(b_gene, e_gene, d_gene)
	print("color: " + color)
	
	# if puppy is dilute, print standard color as well
	if standard_color != color:
		print("standard color: " + standard_color)
	exit()
		
# run main code
genotype_to_phenotype()
