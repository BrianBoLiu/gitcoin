#!/usr/bin/env python
# coding=utf-8

import hashlib
import os
import subprocess
import sys


clone_spec = sys.argv[1]
public_username = sys.argv[2]

def solve():

	# Start with a number with lots of digits so that the length of the commit
	# object can be predicted and is unlikely to ever increase (because we’ll
	# _probably_ have found a coin by then).
	nonce = 8110000000 # length=16

	difficulty = '00000000'
	#with open('difficulty.txt', 'r') as f:
	#	difficulty = f.read().strip()

	tree = subprocess.check_output(['git', 'write-tree']).strip()
	with open('.git/refs/heads/master', 'r') as f:
		parent = f.read().strip()
	###timestamp = int(time.time())
	print 'Mining…'
	base_hasher = hashlib.sha1()
	# The length of all such commit messages is 233, as long as the nonce is 16
	# digits long.
	header = "commit 233\x00"
	base_content = """tree %s
parent %s
author CTF user <me@example.com> 1333333337 +0000
committer CTF user <me@example.com> 1333333337 +0000

Give me 51 Bitcoooooins

""" % (tree, parent)
	base_hasher.update(header + base_content)

	while True:
		nonce = nonce + 1
		hasher = base_hasher.copy()
		#noncestr = str(nonce)
		hasher.update(str(nonce))
		content = base_content + str(nonce)
		sha1 = hasher.hexdigest()
                
                #print nonce
		#print '>>%s<<' % sha1
		if sha1[:8] == difficulty:
			with open('commit.txt', 'w') as f:
				f.write(content)
			print 'Mined a Gitcoin! The SHA-1 is:'
			os.system('git hash-object -t commit commit.txt -w')
			os.system('git reset --hard %s' % sha1)
                        os.system('git push origin master')
			break

def prepare_index():
	os.system('perl -i -pe \'s/(%s:)(\d+)/$1 . ($2+1)/e\' LEDGER.txt' % public_username)
	os.system('grep -q "%s" LEDGER.txt || echo "%s:1" >> LEDGER.txt' % (public_username, public_username))
	os.system('git add LEDGER.txt')

def reset():
	os.system('git fetch origin master')
        #os.system('git checkout HEAD LEDGER.txt && git pull')
	os.system('git reset --hard origin/master')
        
#os.system('git checkout HEAD LEDGER.txt && git pull')
while True:
        reset()
	prepare_index()
	solve()
        reset()
#	if os.system('git push origin master') == 0:
#		print 'Success :)'
#		os.system('git checkout HEAD LEDGER.txt && git pull') #break
#		reset()
                
#	else:
#		print 'Failure :('

		#break
#		reset()
