# -*- coding: utf-8 -*-



'''
@Author Amit Joshi
'''


docfile = file("file_36.csv", "r")
pos = file("pos", "w")
neg = file("neg", "w")
net = file("net", "w")
# ignr = file("ignr", "w")

for line in docfile:
	line = line.strip()
	# line = "'"+line+"'"+","
	# print line

	
	# ignr.write(line)

	try:
		if int(line[-2:]) == -1:
			line = line.replace("\t-1", "\n")
			neg.write(line)

		elif int(line[-1]) == 1:
			line = line.replace("\t1", "\n")
			pos.write(line)

		elif int(line[-1]) == 0:
			line = line.replace("\t0", "\n")
			net.write(line)
	except:
		pass

docfile.close()
pos.close()
neg.close()
net.close()
# ignr.close()