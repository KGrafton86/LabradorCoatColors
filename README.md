# LabradorCoatColors
Tool for determining the potential puppy colors from a mating pair of labrador retrievers. Because coat color is determined by 3 different genes, it can be complicated to figure out. There used to be a web tool to do this, but the developer stopped supporting it. I am building a similar web tool, with the addition of percentages. 

Labrador Coat Colors.nb is the prototype in Mathematica. You can download the [Wolfram Notebook Player](https://www.wolfram.com/player/) for free to run it. 

## Screenshots of the UI from the Prototype
Note that the percentages do not indicate the makeup of a litter. The numbers are the likelihood of color (phenotype) and genotype _for each individual pup_.

<img src="/prototype_phenotypes_gui.png" alt="prototype phenotypes interface" width="460"> <img src="/prototype_genotypes_gui.png" alt="prototype genotypes interface">

## Genotype to Phenotype Logic folder
To determine what phenotype a genotype is, the prototype just looks through a list. I worked out the decision logic in Python, and created a test file to test every possible combination of these 3 genes.

To run lab_coat_colors.py, genotype should be entered like this: BbEeDd
To run test_all_genotypes.py, comment out the line in lab_coat_colors.py that runs the main function
To run labrador_test_or_main, comment out the lines in both lab_coat_colors.py and test_all_genotypes.py that run the main functions

## Web Application
My next step is to build the whole thing as a web application, which will be [on my dog training website](http://trainingsuperdogs.com/labrador-coat-colors-tool.html) when it's finished.The UI will also get an update from the prototype.
