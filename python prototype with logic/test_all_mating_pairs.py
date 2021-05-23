# labrador coat colors tool
# Carolyn R Grafton 2021
# this is for practice in python and is not intended to be released

from labrador_coat_colors import test

# list of all genotypes
genotypes = ["BBEEDD", "BBEEDd", "BbEEDD", "BbEEDd", "BBEeDD", "BBEeDd", "BbEeDD", "BbEeDd", # black
			 "BBeeDD", "BBeeDd", "BbeeDD", "BbeeDd", "bbeeDD", "bbeeDd", # yellow
			 "bbEEDD", "bbEEDd", "bbEeDD", "bbEeDd", # chocolate
			 "BBEEdd", "BbEEdd", "BBEedd", "BbEedd", # charcoal
			 "BBeedd", "Bbeedd", "bbeedd", # champagne
			 "bbEEdd", "bbEedd"] # silver

class Counter():
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1

    def reset(self):
        self.counter = 0

    def get_value(self):
        return self.counter
			 
pairings = len(genotypes) ** 2
test_count = Counter()

# trim list to remove any with a count of 0
def trim_list(list):
	trimmed_list = []
	for l in list: 
		if l[1] > 0:
			trimmed_list.append(l)
	return(trimmed_list)
	
# sum percentages from the list to find which ones don't add up to 100%
def percent_sum(list):
	sum = 0
	for l in list:
		sum = sum + l[2]
	return(sum)
	
# extract individual counts and percentages
# needs to be done before list is trimmed
def phenotype_counts_and_percents(list):
	black_count = list[0][1]
	black_percent = list[0][2]
	yellow_count = list[1][1]
	yellow_percent = list[1][2]
	chocolate_count = list[2][1]
	chocolate_percent = list[2][2]
	charcoal_count = list[3][1]
	charcoal_percent = list[3][2]
	champagne_count = list[4][1]
	champagne_percent = list[4][2]
	silver_count = list[5][1]
	silver_percent = list[5][2]
	return(black_count, black_percent, yellow_count, yellow_percent, chocolate_count, chocolate_percent, charcoal_count, charcoal_percent, champagne_count, champagne_percent, silver_count, silver_percent)

# function to iterate through all possible mating pairs	
def main():
	f = open("test_all_mating_pairs_results.txt", "w+")
	f2 = open("test_all_mating_pairs_results.csv", "w+")
	f2.write("test number, sire genotype, sire color, dam genotype, dam color, genotype percent sum, phenotype percent sum, black count, black percent, yellow count, yellow percent, chocolate count, chocolate percent, charcoal count, charcoal percent, champagne count, champagne percent, silver count, silver percent\n")
	
	for s in genotypes:
		for d in genotypes:
			test_count.increment()
			sire_color, dam_color, genotype_percents, phenotype_percents = test(s, d)
			black_count, black_percent, yellow_count, yellow_percent, chocolate_count, chocolate_percent, charcoal_count, charcoal_percent, champagne_count, champagne_percent, silver_count, silver_percent = phenotype_counts_and_percents(phenotype_percents)
			genotype_percents = trim_list(genotype_percents)
			phenotype_percents = trim_list(phenotype_percents)
			f.write("-------------------------\n")
			f.write(f"Test {test_count.get_value()} of {pairings}\n")
			f.write("\n")
			f.write(f"SIRE: - {s} - {sire_color}\n")
			f.write(f"DAM: - {d} - {dam_color}\n")
			f.write("\n")
			f.write("POTENTIAL OFFSPRING GENOTYPES: \n")
			f.write(str(genotype_percents))
			f.write("\n")
			f.write("\nPOTENTIAL OFFSPRING PHENOTYPES: \n")
			f.write(str(phenotype_percents))
			f.write("\n-------------------------\n")
			f.write("\n")
			
			genotype_percent_sum = percent_sum(genotype_percents)
			phenotype_percent_sum = percent_sum(phenotype_percents)
			f2.write(f"{test_count.get_value()}, {s}, {sire_color}, {d}, {dam_color}, {genotype_percent_sum}, {phenotype_percent_sum}, {black_count}, {black_percent}, {yellow_count}, {yellow_percent}, {chocolate_count}, {chocolate_percent}, {charcoal_count}, {charcoal_percent}, {champagne_count}, {champagne_percent}, {silver_count}, {silver_percent}\n")
			
	f.close()
	f2.close()
	print("test_all_mating_pairs task complete")

main()