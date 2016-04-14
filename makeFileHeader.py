# This script creates a file with a default template header
# Siddharth Advani
# 02/25/2016
###########################################################

import sys
import time
from datetime import date

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'Usage: python makeFileHeader.py filename.extention'
		print 'Example: python makeFileHeader.py test.py'
		print 'Supported extentions are m, v cpp, cc, c and py'
	else:
		try:
			fp = open(sys.argv[1], 'w')
		except IOError:
			print 'cannot open ' + sys.argv[1]

		fcmp = (sys.argv[1]).split('.')		

		if fcmp[1] == 'm':
			comment_symbol = '%'
		elif fcmp[1] == 'v':
			comment_symbol = '//'
		elif fcmp[1] == 'py':
			comment_symbol = '#'
		elif fcmp[1] == 'cpp' or fcmp[1] == 'cc' or fcmp[2] == 'c':
			comment_symbol = '//'
		else:
			raise NameError('File extention')	

		fp.write(50*comment_symbol)		
		fp.write('\n')
		fp.write(comment_symbol + '\tProject Name:')
		fp.write('\n')
		fp.write(comment_symbol + '\tModule Name: ' + sys.argv[1])
		fp.write('\n')
		fp.write(comment_symbol + '\tAuthor:')
		fp.write('\n')
		fp.write(comment_symbol + '\tDate: ' + str(date.today()))
		fp.write('\n')
		fp.write(comment_symbol + '\tComments:')
		fp.write('\n')
		fp.write(50*comment_symbol)		
		
		fp.close()

