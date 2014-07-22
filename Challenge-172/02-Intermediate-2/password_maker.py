#!/usr/bin/python
import sys

if len(sys.argv)<2:
	print "\nYou need to provide an argument!\nThe syntax is the following:\n\npython password_maker.py [password]"
	exit()

import hashlib
import uuid


password = sys.argv[1]
salt = uuid.uuid4().hex
hashed_password = hashlib.sha512(password + salt).hexdigest()

f = open('salt.txt', 'wb')
f.write(salt)
f.close()

f = open('encrypted.txt', 'wb')
f.write(hashed_password)
f.close()

print "\n=============================================================================\n\n"
print "Your password has been hashed and salted, and is ready to use on the web interface."
print "To reset it, log in through SSH and run this script again."
print "\n\n=============================================================================\n"
