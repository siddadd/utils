# This python script creates a BRAM initialization for the histogram core
# Format is as per Xilinx coe
# Siddharth Advani

import os

fw=open('PageTable.coe', 'w')

fw.write('memory_initialization_radix=16;'+'\n')
fw.write('memory_initialization_vector='+'\n')

page_table_size = 2048*2048/64

for i in range(0,page_table_size-1):	
	fw.write(hex(i)[2:len(hex(i))].zfill(8) + ',' + '\n')

fw.write(hex(page_table_size-1)[2:len(hex(page_table_size-1))].zfill(8) + ';' + '\n')	
fw.close()
