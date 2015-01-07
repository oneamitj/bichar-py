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

# def train():

args = sys.argv


# print args[1], args[2]

if len(args) != 3:
	print "Usage python train.py <file> <tag>"
	print "valid tag 'p' and 'n'"
	exit(0)

try:
	tag_file = file(args[1], "r")
	tag = args[2]
except:
	print "No such file", args[1]
	exit(0)

for text in tag_file:
	text = text.strip().replace("'", "")
	text = txt_to_list(text)
	for word in text:
		sqlSel = "SELECT * FROM `classified` WHERE word = '%s' AND tag = '%s'" % (word, tag)
		# print sqlSel
		cursor.execute(sqlSel)
		data = cursor.fetchone()

		if data:
			sqlIns = "UPDATE classified SET count = '%s' WHERE word = '%s' AND tag = '%s'" % (int(data[2]) + 1, word, tag)
		else:
			sqlIns = "INSERT INTO classified(word, tag, count) VALUES('%s', '%s', '%s')" % (word, tag, 1)

		cursor.execute(sqlIns)
		db.commit()