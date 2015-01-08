bichar-py
---------

python implementation of sentiment analysis for nepali language using bayesian classification.

Tools required:

+ Python
+ MySQL

Usage:

To train:

	python train.py <doctypefile> <tag>

tag => only 'p' or 'n'

doctypefile => file with sentences in each line of type <tag>

Example:

	python train.py positive.txt p

To Analyze

	python analyze.py

Then enter sentence to analyze

More data you train higher is accuracy.
