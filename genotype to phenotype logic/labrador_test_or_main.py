# labrador coat colors tool
# asks the user whether they want to run test or main
# to run this, need to comment out the lines in test_all_genotypes and lab_coat_colors that call the main function

from test_all_genotypes import test_all_genotypes
from genotype_to_phenotype import genotype_to_phenotype

def test_or_main():
	print("Run test or main? ")
	choice = input()
	if choice.lower() == "test" or choice.lower() == "t":
		test_all_genotypes()
	elif choice.lower() == "main" or choice.lower() == "m":
		genotype_to_phenotype()
	else:
		print("\nNot a valid choice")
		test_or_main()

test_or_main()		
