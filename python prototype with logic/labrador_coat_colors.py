# labrador coat colors tool
# Carolyn R Grafton 2021
# this is for practice in python and is not intended to be released

from genotype_to_phenotype import genotype_to_phenotype
from recombine_genotypes import recombine_genotype
from calculate_percentages import calculate_genotype_percents, calculate_phenotype_percents

# if dilute, report standard color as well
def dilute_plus_standard_color(standard_color, color, dilute):
	if dilute == True:
		color = color + " [" + standard_color + "]"
	elif dilute == False: 
		color
	else: 
		print("wtf is this how did you get here? error PtO1")
	return(color)

# turn list of genotypes into list of phenotypes
def offspring_phenotypes(genotypes):
	phenotypes = []
	for i in genotypes:
		standard_color, color, dilute = genotype_to_phenotype(i)
		phenotypes.append(color)
	return(phenotypes)

# MAIN CODE BLOCK
def main():
	# get sire genotype & color
	print("Enter sire genotype (order: B,E,D): ")
	sire_genotype = input()
	sire_standard_color, sire_color, sire_dilute = genotype_to_phenotype(sire_genotype)
	sire_color = dilute_plus_standard_color(sire_standard_color, sire_color, sire_dilute)
	print("Sire color: " + sire_color)
	
	# get dam genotype & color
	print("\nEnter dam genotype (order: B,E,D): ")
	dam_genotype = input()
	dam_standard_color, dam_color, dam_dilute = genotype_to_phenotype(dam_genotype)
	dam_color = dilute_plus_standard_color(dam_standard_color, dam_color, dam_dilute)
	print("Dam color: " + dam_color)

	# get offspring genotypes
	offspring_genotypes = recombine_genotype(sire_genotype, dam_genotype)
	offspring_colors = offspring_phenotypes(offspring_genotypes)
	
	# calculate percentages
	genotype_percents = calculate_genotype_percents(offspring_genotypes)
	print("Potential offspring genotypes: ")
	print(genotype_percents)
	phenotype_percents = calculate_phenotype_percents(offspring_colors)
	print("Potential offspring colors: ")
	print(phenotype_percents)

# run main code
# main()

def test(sire_genotype, dam_genotype):
	# get sire genotype & color
	sire_standard_color, sire_color, sire_dilute = genotype_to_phenotype(sire_genotype)
	# sire_color = dilute_plus_standard_color(sire_standard_color, sire_color, sire_dilute)
	# print("SIRE - " + sire_genotype + " - " + sire_color)
	
	# get dam genotype & color
	dam_standard_color, dam_color, dam_dilute = genotype_to_phenotype(dam_genotype)
	# dam_color = dilute_plus_standard_color(dam_standard_color, dam_color, dam_dilute)
	# print("DAM - " + dam_genotype + " - " + dam_color)

	# get offspring genotypes
	offspring_genotypes = recombine_genotype(sire_genotype, dam_genotype)
	offspring_colors = offspring_phenotypes(offspring_genotypes)
	
	# calculate percentages
	genotype_percents = calculate_genotype_percents(offspring_genotypes)
	phenotype_percents = calculate_phenotype_percents(offspring_colors)
	return(sire_color, dam_color, genotype_percents, phenotype_percents)