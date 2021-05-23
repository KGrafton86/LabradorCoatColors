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

# function to iterate through all possible mating pairs	
def main():
	f = open("test_all_mating_pairs_results.txt", "w+")
	
	for s in genotypes:
		for d in genotypes:
			test_count.increment()
			sire_color, dam_color, genotype_percents, phenotype_percents = test(s, d)
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
			
	f.close()
	print("test_all_mating_pairs task complete")

main()