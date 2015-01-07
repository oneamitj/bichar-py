#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
@Author Amit Joshi
'''


import MySQLdb
import sys, re
from t2l import txt_to_list

reload(sys)
sys.setdefaultencoding('utf8') 

db = MySQLdb.connect("localhost","root","3", "bayes" )
cursor = db.cursor()
cursor.execute("SET NAMES utf8")

# clean_eng_senti = "SELECT * FROM `clean_eng_senti` WHERE SynsetTerms = '%s'" % (row[0])
# sqlIns = "INSERT INTO clean_nep_senti(POS, ID, PosScore, NegScore, SynsetTerms) VALUES('%s', '%s', '%s', '%s', '%s')" % \
# (search_list[0], search_list[1], float(search_list[2]), float(search_list[3]), row[i])

def prob_4_word(word):
	PROB_RARE_WORD = 0.5

	sqlSel_pos = "SELECT * FROM `classified` WHERE word = '%s' AND tag = '%s'" % (word, 'p')
	cursor.execute(sqlSel_pos)
	data_pos = cursor.fetchone()

	sqlSel_neg = "SELECT * FROM `classified` WHERE word = '%s' AND tag = '%s'" % (word, 'n')
	cursor.execute(sqlSel_neg)
	data_neg = cursor.fetchone()

	# print "POS", sqlSel_pos
	# print "NEG", sqlSel_neg

	if data_pos:
		pos_count = data_pos[2]
	else:
		pos_count = 1
	
	if data_neg:
		neg_count = data_neg[2]
	else:
		neg_count = 1


	if pos_count == 1 and neg_count == 1:
		return PROB_RARE_WORD
	else:
		return float(pos_count)/(float(pos_count) + float(neg_count))


def prob_4_list(prob_list):
	# PROB_LIST = 0

	prob_product         = reduce(lambda x,y: x*y, prob_list)
	prob_inverse_product = reduce(lambda x,y: x*y, map(lambda x: 1-x, prob_list))

	return float(prob_product)/(float(prob_product) + float(prob_inverse_product))


def classify(text):
	pl = []

	text = text.replace("'", "")
	text_list = txt_to_list(text)

	for word in text_list:
		prob = prob_4_word(word)
		pl.append(prob)
		# print word, prob

	result = prob_4_list(pl)

	return result