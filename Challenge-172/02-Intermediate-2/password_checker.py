#!/usr/bin/python
import hashlib
import uuid

password = 'test123' 

f = open('salt.txt')
salt = f.read()
f.close()

f = open('encrypted.txt')
hashed_password = f.read()
f.close()

if hashlib.sha512(password + salt).hexdigest() == hashed_password:
	print 'ACCESS GRANTED'
else:
	print 'ACCESS DENIED'
