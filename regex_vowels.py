#!/usr/bin/python3

import re

def vowel_finder(word):

	vowe_ls = 'aeiou'		# initialize a list of vowels to be used as regex pattern
					
	print("\n\n"+word+"\n")

	# find all the vowels in given string, ignore letter case
	print("\n\nThere are",len(re.findall(r'['+re.escape(vowe_ls)+']', word, re.I|re.M)),"vowels in your sentence\n\n")

	for letter in vowe_ls:

		# loop through the found vowels to specifiy the quantity of each individual vowel
		print("There are",len(re.findall(r'['+re.escape(letter)+']', ''.join(re.findall(r'['+re.escape(vowe_ls)+']', word, re.I|re.M)), re.I|re.M)),"instances of the letter,", letter,"\n\n")

if __name__ == "__main__":
	
	vowel_finder('hey i wonder if it will work')
	vowel_finder('738f88uehfiu8 28disiIIIIIkjfhiq3h3498ytfnsferhajdstystoiqexvjnvvoeqo')
	vowel_finder('Leets SEEE ifff we can pIck up CAPITALIZED vOwels45764574823')