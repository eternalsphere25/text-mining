#------------------------------------------------------------------------------
# This program breaks down Japanese language text for word analysis
#
# HOW TO USE:
# 1. Place source file into same folder as textMiner.py
# 2. Run textMiner.py and follow the prompts
#
# Make sure the accompanying definitions file is placed in  the same directory 
#   as this file
#------------------------------------------------------------------------------

import csv
import datetime
import math
import MeCab
import os
from text_miner_JP_definitions import *
from tqdm import tqdm
import pyexcel_ods3


def convert_sec_to_min(total_seconds):
	value = math.floor(total_seconds/60)
	return value

def remove_char_from_string(input_df, input_str, char):
    if input_str.find(char) != -1:
        cleaned_string = input_str.replace(char,"")
        input_df = input_df.replace(input_str, cleaned_string) 

def welcome_message():
    print('\nInitializing program, please standby...')
    print('Program online')
    print('\n' + ("*")*80)
    print(('Japanese Language Text Miner').center(80, " "))
    print("")
    print(('This program extracts Japanese text from Excel files (.xlsx),').center(80, " "))
    print(('parses it, and outputs the results to .csv').center(80, " "))
    print("")
    print(('NOTE: Please make sure the necessary data files are').center(80, " "))
    print(('in the same directory as this program').center(80, " "))
    print("")
    print(('For detailed instructions and/or changelog, refer to source code').center(80, " "))
    print('\n' + ("*")*80)


#-------------------------------------------------------------------------------
# STEP 0: Define global variables
#-------------------------------------------------------------------------------

#Just for fun: calculates how much time the program takes
start = datetime.datetime.now()


#-------------------------------------------------------------------------------
# STEP 1: Define input text
#-------------------------------------------------------------------------------

#Startup messages
welcome_message()

#Import data
input_file = input('\nEnter file name (include file extension): ')

data = pyexcel_ods3.get_data(input_file)
extracted_column_data = dict(data)['Sheet1']


#-------------------------------------------------------------------------------
# STEP 2: Parse text
#-------------------------------------------------------------------------------

#Set up parser
mt = MeCab.Tagger()
components = []

#Parse all input text strings
print('\nBegin text parsing...')
for item in tqdm(range(len(extracted_column_data))):
    parsed = mt.parseToNode(extracted_column_data[item][0])
    while parsed:
        components.append(parsed.surface)
        parsed = parsed.next

#Remove empty entries in list
components = list(filter(None, components))

#Print out results
print('\nText parsed successfully')
print('Total number of extracted words: ' + str(len(components)))


#-------------------------------------------------------------------------------
# STEP 3: Run analysis
#-------------------------------------------------------------------------------

#Make copy of list with removed duplicates for counting analysis
words = list(set(components))

#Count the number of occurrences of each word, minus particles and grammar
word_freq = {}
for item in range(len(words)):
    if words[item] not in particles and words[item] not in grammar:
        word_freq[str(words[item])] = str(components.count(words[item]))
    else:
        pass

#Sort and print list
sorted_word_freq = dict(
    sorted(word_freq.items(), key=lambda item: int(item[1]), reverse=True))
for keys in sorted_word_freq:
    sorted_word_freq[keys] = int(sorted_word_freq[keys])
print('\nWord frequency calculated')
print('Total number of entries after filtering: ' + str(len(sorted_word_freq)))


#-------------------------------------------------------------------------------
# STEP 4: Remove any non-significant values (punctuation etc)
#-------------------------------------------------------------------------------

sorted_word_freq_output = {}
for key in list(sorted_word_freq.keys()):
    if key in punctuation or key in single_hiragana or key in digits:
        del sorted_word_freq[key]


#-------------------------------------------------------------------------------
# STEP 5: Save results to file and close program
#-------------------------------------------------------------------------------

#Write out words to .ods
words_out = list(sorted_word_freq.items())
filename = 'text_mining_output.ods'
write_out = {'Words': words_out}
pyexcel_ods3.save_data(filename, write_out)

#Closing messages and program close
end = datetime.datetime.now()
print('\nSUCCESS: All processes completed')
elapsed_time_min = convert_sec_to_min((end-start).seconds)
elapsed_time_sec = (end-start).seconds - elapsed_time_min*60
if elapsed_time_min == 0:
	print('\nProcesses executed in ' + str(elapsed_time_sec) + ' sec')
else:
	print('\nProcesses executed in ' + str(elapsed_time_min) + ' min and ' + str(elapsed_time_sec) + ' sec')
print('Program terminated...\n')