# This script takes a baseline output and compares line by line with the generated output
# SPRING 2013

import subprocess
import difflib
import sys

NUM_ITERATIONS = 2

RUN_ALL = 1
RUN_FCFS = 0
RUN_SRTF = 0
RUN_PBS = 0
RUN_MLFQ = 0

INPUT_PATH = "./p1_test/TestOutputs/"

def test_scheduler(fileName):
	d = difflib.Differ()
	fp1 = open(INPUT_PATH + fileName)
	correct_lines = fp1.readlines()
	fp1.close()
	print("")
	print("Testing" + " " + fileName[13:17] + " " + fileName[5:12])

	for i in range(0,NUM_ITERATIONS):
		with open("generated_output.txt", 'w') as f:
    			subprocess.check_call(["./RunScheduler","0","input_1"], stdout=f)
		fp2 = open("generated_output.txt")	
		test_lines = fp2.readlines()
		fp2.close()
		matcher = difflib.SequenceMatcher(None,correct_lines,test_lines)

		if matcher.ratio() == 1.0:
			print "Iteration" + " " + str(i+1) + ":" + "All is Well"
		else:
			print "Iteration" + " " + str(i+1) + ":" + "Problem"
			result = d.compare(correct_lines,test_lines)
			fp3 = open("error.log","a")
			fp3.write("Error: " + fileName + "\n")
			fp3.writelines(result)
			fp3.close()

def runme(args=None):
	if RUN_ALL or RUN_FCFS:
		# FCFS - INPUT 1
		test_scheduler("base_input_1_fcfs_output")
		# FCFS - INPUT 2
		test_scheduler("base_input_2_fcfs_output")
		# FCFS - INPUT 3
		test_scheduler("base_input_3_fcfs_output")

	if RUN_ALL or RUN_SRTF:
		#SRTF - INPUT 1
		test_scheduler("base_input_1_srtf_output")
		#SRTF - INPUT 2
		test_scheduler("base_input_2_srtf_output")
		#SRTF - INPUT 3
		test_scheduler("base_input_3_srtf_output")
	
	if RUN_ALL or RUN_PBS:
		# PBS - INPUT 1
		test_scheduler("base_input_1_pbs_output")
		# PBS - INPUT 2
		test_scheduler("base_input_2_pbs_output")
		# PBS - INPUT 3
		test_scheduler("base_input_3_pbs_output")

	if RUN_ALL or RUN_MLFQ:
		# MLFQ - INPUT 1
		test_scheduler("base_input_1_mlfq_output")
		# MLFQ - INPUT 2
		test_scheduler("base_input_2_mlfq_output")
		# MLFQ - INPUT 3
		test_scheduler("base_input_3_mlfq_output")

if __name__ == "__main__":
	runme()

#if RUN_ALL == 1 or RUN_SRTF == 1:
#
#	# SRTF - INPUT 1
#
#	fileName = "base_input_1_srtf_output"
#
#	fp1 = open("./p1_test/TestOutputs/"+fileName)
#	correct_lines = fp1.readlines()
#	print("")
#	print("Testing" + " " + fileName[13:17] + " " + fileName[5:12])

#	for i in range(0,NUM_ITERATIONS):
#		with open("generated_output.txt", 'w') as f:
#    			subprocess.check_call(["./RunScheduler","1","input_1"], stdout=f)
#		fp2 = open("generated_output.txt")	
#		test_lines = fp2.readlines()
#		matcher = difflib.SequenceMatcher(None,correct_lines,test_lines)
#
#		if matcher.ratio() == 1.0:
#			print "Iteration" + " " + str(i+1) + ":" + "All is Well"
#		else:
#			print "Iteration" + " " + str(i+1) + ":" + "Problem"
#			result = d.compare(correct_lines,test_lines)
#			fp3 = open("error.log","a")
#			fp3.write("Error: " + fileName + "\n")
#			fp3.writelines(result)
#			fp3.close()
#
#
#	# SRTF - INPUT 2
#
#	fileName = "base_input_2_srtf_output"
#
#	fp1 = open("./p1_test/TestOutputs/"+fileName)
#	correct_lines = fp1.readlines()
#	print("")
#	print("Testing" + " " + fileName[13:17] + " " + fileName[5:12])
#
#	for i in range(0,NUM_ITERATIONS):
#		with open("generated_output.txt", 'w') as f:
#    			subprocess.check_call(["./RunScheduler","1","input_2"], stdout=f)
#		fp2 = open("generated_output.txt")	
#		test_lines = fp2.readlines()
#		matcher = difflib.SequenceMatcher(None,correct_lines,test_lines)
#
#		if matcher.ratio() == 1.0:
#			print "Iteration" + " " + str(i+1) + ":" + "All is Well"
#		else:
#			print "Iteration" + " " + str(i+1) + ":" + "Problem"
#			result = d.compare(correct_lines,test_lines)
#			fp3 = open("error.log","a")
#			fp3.write("Error: " + fileName + "\n")
#			fp3.writelines(result)
#			fp3.close()
#
#
#	# SRTF - INPUT 3
#
#	fileName = "base_input_3_srtf_output"
#
#	fp1 = open("./p1_test/TestOutputs/"+fileName)
#	correct_lines = fp1.readlines()
#	print("")
#	print("Testing" + " " + fileName[13:17] + " " + fileName[5:12])
#
#	for i in range(0,NUM_ITERATIONS):
#		with open("generated_output.txt", 'w') as f:
#    			subprocess.check_call(["./RunScheduler","1","input_3"], stdout=f)
#		fp2 = open("generated_output.txt")	
#		test_lines = fp2.readlines()
#		matcher = difflib.SequenceMatcher(None,correct_lines,test_lines)
#
#		if matcher.ratio() == 1.0:
#			print "Iteration" + " " + str(i+1) + ":" + "All is Well"
#		else:
#			print "Iteration" + " " + str(i+1) + ":" + "Problem"
#			result = d.compare(correct_lines,test_lines)
#			fp3 = open("error.log","a")
#			fp3.write("Error: " + fileName + "\n")
#			fp3.writelines(result)
#			fp3.close()
#
#
#if RUN_ALL == 1 or RUN_PBS == 1:
#
#	# PBS - INPUT 1
#
#	fileName = "base_input_1_pbs_output"
#
#	fp1 = open("./p1_test/TestOutputs/"+fileName)
#	correct_lines = fp1.readlines()
#	print("")
#	print("Testing" + " " + fileName[13:16] + " " + fileName[5:12])
#
#	for i in range(0,NUM_ITERATIONS):
#		with open("generated_output.txt", 'w') as f:
#    			subprocess.check_call(["./RunScheduler","2","input_1"], stdout=f)
#		fp2 = open("generated_output.txt")	
#		test_lines = fp2.readlines()
#		matcher = difflib.SequenceMatcher(None,correct_lines,test_lines)
#
#		if matcher.ratio() == 1.0:
#			print "Iteration" + " " + str(i+1) + ":" + "All is Well"
#		else:
#			print "Iteration" + " " + str(i+1) + ":" + "Problem"
#			result = d.compare(correct_lines,test_lines)
#			fp3 = open("error.log","a")
#			fp3.write("Error: " + fileName + "\n")
#			fp3.writelines(result)
#			fp3.close()
#
#
#	# PBS - INPUT 2
#
#	fileName = "base_input_2_pbs_output"
#
#	fp1 = open("./p1_test/TestOutputs/"+fileName)
#	correct_lines = fp1.readlines()
#	print("")
#	print("Testing" + " " + fileName[13:16] + " " + fileName[5:12])
#
#	for i in range(0,NUM_ITERATIONS):
#		with open("generated_output.txt", 'w') as f:
#    			subprocess.check_call(["./RunScheduler","2","input_2"], stdout=f)
#		fp2 = open("generated_output.txt")	
#		test_lines = fp2.readlines()
#		matcher = difflib.SequenceMatcher(None,correct_lines,test_lines)
#
#		if matcher.ratio() == 1.0:
#			print "Iteration" + " " + str(i+1) + ":" + "All is Well"
#		else:
#			print "Iteration" + " " + str(i+1) + ":" + "Problem"
#			result = d.compare(correct_lines,test_lines)
#			fp3 = open("error.log","a")
#			fp3.write("Error: " + fileName + "\n")
#			fp3.writelines(result)
#			fp3.close()
#
#
#	# PBS - INPUT 3
#
#	fileName = "base_input_3_pbs_output"
#
#	fp1 = open("./p1_test/TestOutputs/"+fileName)
#	correct_lines = fp1.readlines()
#	print("")
#	print("Testing" + " " + fileName[13:16] + " " + fileName[5:12])
#
#	for i in range(0,NUM_ITERATIONS):
#		with open("generated_output.txt", 'w') as f:
#    			subprocess.check_call(["./RunScheduler","2","input_3"], stdout=f)
#		fp2 = open("generated_output.txt")	
#		test_lines = fp2.readlines()
#		matcher = difflib.SequenceMatcher(None,correct_lines,test_lines)
#	
#		if matcher.ratio() == 1.0:
#			print "Iteration" + " " + str(i+1) + ":" + "All is Well"
#		else:
#			print "Iteration" + " " + str(i+1) + ":" + "Problem"
#			result = d.compare(correct_lines,test_lines)
#			fp3 = open("error.log","a")
#			fp3.write("Error: " + fileName + "\n")
#			fp3.writelines(result)
#			fp3.close()
#
#if RUN_ALL == 1 or RUN_MLFQ == 1:
#
#	# MLFQ - INPUT 1
#
#	fileName = "base_input_1_mlfq_output"
#
#	fp1 = open("./p1_test/TestOutputs/"+fileName)
#	correct_lines = fp1.readlines()
#	print("")
#	print("Testing" + " " + fileName[13:17] + " " + fileName[5:12])
#
#	for i in range(0,NUM_ITERATIONS):
#		with open("generated_output.txt", 'w') as f:
#    			subprocess.check_call(["./RunScheduler","3","input_1"], stdout=f)
#		fp2 = open("generated_output.txt")	
#		test_lines = fp2.readlines()
#		matcher = difflib.SequenceMatcher(None,correct_lines,test_lines)
#
#		if matcher.ratio() == 1.0:
#			print "Iteration" + " " + str(i+1) + ":" + "All is Well"
#		else:
#			print "Iteration" + " " + str(i+1) + ":" + "Problem"
#			result = d.compare(correct_lines,test_lines)
#			fp3 = open("error.log","a")
#			fp3.write("Error: " + fileName + "\n")
#			fp3.writelines(result)
#			fp3.close()
#
#	# MLFQ - INPUT 2
#
#	fileName = "base_input_2_mlfq_output"
#
#	fp1 = open("./p1_test/TestOutputs/"+fileName)
#	correct_lines = fp1.readlines()
#	print("")
#	print("Testing" + " " + fileName[13:17] + " " + fileName[5:12])
#
#	for i in range(0,NUM_ITERATIONS):
#		with open("generated_output.txt", 'w') as f:
#    			subprocess.check_call(["./RunScheduler","3","input_2"], stdout=f)
#		fp2 = open("generated_output.txt")	
#		test_lines = fp2.readlines()
#		matcher = difflib.SequenceMatcher(None,correct_lines,test_lines)
#
#		if matcher.ratio() == 1.0:
#			print "Iteration" + " " + str(i+1) + ":" + "All is Well"
#		else:
#			print "Iteration" + " " + str(i+1) + ":" + "Problem"
#			result = d.compare(correct_lines,test_lines)
#			fp3 = open("error.log","a")
#			fp3.write("Error: " + fileName + "\n")
#			fp3.writelines(result)
#			fp3.close()
#
#
#	# MLFQ - INPUT 3
#
#	fileName = "base_input_3_mlfq_output"
#
#	fp1 = open("./p1_test/TestOutputs/"+fileName)
#	correct_lines = fp1.readlines()
#	print("")
#	print("Testing" + " " + fileName[13:17] + " " + fileName[5:12])
#
#	for i in range(0,NUM_ITERATIONS):
#		with open("generated_output.txt", 'w') as f:
#    			subprocess.check_call(["./RunScheduler","3","input_3"], stdout=f)
#		fp2 = open("generated_output.txt")	
#		test_lines = fp2.readlines()
#		matcher = difflib.SequenceMatcher(None,correct_lines,test_lines)
#	
#		if matcher.ratio() == 1.0:
#			print "Iteration" + " " + str(i+1) + ":" + "All is Well"
#		else:
#			print "Iteration" + " " + str(i+1) + ":" + "Problem"
#			result = d.compare(correct_lines,test_lines)
#			fp3 = open("error.log","a")
#			fp3.write("Error: " + fileName + "\n")
#			fp3.writelines(result)
#			fp3.close()
