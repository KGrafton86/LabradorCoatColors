# labrador coat colors tool
# Carolyn R Grafton 2021
# this is for practice in python and is not intended to be released

# # lists for testing
# offspring_genotypes = ['BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEeDd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'BbEedd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEeDd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd', 'bbEedd']

# offspring_colors = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'charcoal', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'chocolate', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver']

# calculate genotype percentages
def calculate_genotype_percents(offspring):
	# list of all genotypes
	genotypes = ["BBEEDD", "BBEEDd", "BbEEDD", "BbEEDd", "BBEeDD", "BBEeDd", "BbEeDD", "BbEeDd", # black
				 "BBeeDD", "BBeeDd", "BbeeDD", "BbeeDd", "bbeeDD", "bbeeDd", # yellow
				 "bbEEDD", "bbEEDd", "bbEeDD", "bbEeDd", # chocolate
				 "BBEEdd", "BbEEdd", "BBEedd", "BbEedd", # charcoal
				 "BBeedd", "Bbeedd", "bbeedd", # champagne
				 "bbEEdd", "bbEedd"] # silver
	offspring_len = len(offspring)
	genotype_percents = []
	for g in genotypes:
		count = sum(1 for o in offspring if o == g)
		percent = count / offspring_len * 100
		genotype_percents.append((g, count, percent))
	return(genotype_percents)

# genotype_percents = calculate_genotype_percents(offspring_genotypes)
# print(genotype_percents)		

# calculate phenotype percentages
def calculate_phenotype_percents(offspring):
	# list of all phenotypes
	phenotypes = ["black", "yellow", "chocolate", "charcoal", "champagne", "silver"]
	offspring_len = len(offspring)
	phenotype_percents =  []
	for p in phenotypes:
		count = sum(1 for o in offspring if o == p)
		percent = count / offspring_len * 100
		phenotype_percents.append((p, count, percent))
	return(phenotype_percents)

# phenotype_percents = calculate_phenotype_percents(offspring_colors)
# print()
# print(phenotype_percents)