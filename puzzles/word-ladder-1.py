#!/usr/bin/env python

# A Python solution to the problem presented on this web site:
# http://www.programcreek.com/2012/12/leetcode-word-ladder/
# Patrick McCormack

start = "hit"
words=["hot","dot","dog","lot","log"]
end = "cog"

def generateWords(word):
	candidate_list=[]
	for pos in range(len(word)):
		# exclude any permuntation that includes a letter from the original word
		alphabet = "abcdefghijklmnopqrstuvwxyz".replace(word[pos],"")
		for c in alphabet:
			candidate = word[0:pos] + c + word[pos+1:]
			candidate_list.append(candidate)
	return candidate_list	

def findPath(word, wordlist, path):
	path.append(word)
	candidates = generateWords(word)
	if end in candidates:
		path.append(end)
		return 
	for w in wordlist:
		if w in candidates:
			# if we've visited this word already then exlude otherwise we'll get into a loop
			wordlist.remove(w)
			findPath(w, wordlist, path)
	return path

p = findPath(start, words, [])
print len(p)
print p
