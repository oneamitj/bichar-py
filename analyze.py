#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
@Author Amit Joshi
'''

import sys
from bayes import classify
from t2l import txt_to_list

reload(sys)
sys.setdefaultencoding('utf8')

text = raw_input("Enter Nepali Sentence: ")

result = classify(text)

# if result < 0.35:
# 	print text, "=> Positive"
# elif result > 0.65:
# 	print text, "=> Negative"
# else:
# 	print text, "=> Neutral"

if result < 0.35:
	print "\nPositive\n"
elif result > 0.65:
	print "\nNegative\n"
else:
	print "\nNeutral\n"