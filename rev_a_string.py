#!/usr/bin/python3


"""
A very simple program to reverse any word without using the reverse function

Leave room for expandibility for other word manipulation methods
"""
class ReversalTool():

	def __init__(self, word):
		self._word = word

	def word_reverser(self):

		re_container = []

		x = -1
		for i in range(len(self._word)):
			re_container.append(self._word[x])
			x -= 1

		rev_word = ''.join(re_container)
		
		print(rev_word)

if __name__ == "__main__":

	query = input("What word would you like to reverse : ")

	subject = ReversalTool(query)

	subject.word_reverser()