# This python script parses through the training dataset provided for LPIRC to find the number of training instances per class
# Siddharth Advani

from xml.dom import minidom
import csv
import os

annotation_path = './LPIRC/LPIRC2015/Annotations/'

fo=open('mapping.txt', mode='r')
reader = csv.reader(fo)
map_dict = dict(reader)
fo.close()

# This dictionary will hold the number of occurrences
num_map_dict = map_dict.fromkeys(map_dict,0)

print('Checking ' + annotation_path)

files = [f for f in os.listdir(annotation_path) if os.path.isfile(os.path.join(annotation_path,f))]
#print files
count = 0
for file in files:
#	if (count < 10):
		if file.endswith('.xml'):
			count = count + 1
			print(str(count) + ':' + file)
			xmldoc = minidom.parse(os.path.join(annotation_path,file));
			classList = xmldoc.getElementsByTagName('name')
			#print('Number of classes in ' + fileName + ':' + str(len(classList)))
			
			for s in classList:
				className = s.childNodes[0].nodeValue
				if (className in map_dict):
					num_map_dict[className] = num_map_dict[className] + 1
					#print(className + '->' + map_dict[className] + ':' + str(num_map_dict[className]))        

fw=open('lpirc_stats.csv', 'w')
try:
	for key in num_map_dict.keys():
		fw.write(key + ',' + map_dict[key] + ',' + str(num_map_dict[key]) + '\n')
finally:
	fw.close()
