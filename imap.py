#!/usr/bin/python
# Small Tool just to login to an IMAP(s) Mailbox and perform a LIST command
# Steven Glogger <steven@glogger.ch>

import imaplib
import io

def open_connection(username,password,verbose=False):
    # Connect to the server
    hostname = 'imaps.bluewin.ch';
    if verbose: print ('Connecting to', hostname)
    connection = imaplib.IMAP4_SSL(hostname)

    if verbose: print ('Logging in as', username)
	connection.login(username,password)
    return connection


if __name__ == '__main__':

    # Open Config File and read out Username and Password
    f = open("imap.config", "r")
    line = f.readline()

    while line:
	username, password = line.split()
	print '======================================='
	print 'Trying Mailbox: ',username
	print '======================================='
    	c = open_connection(username,password,verbose=True)
    	try:
        	print c
    	finally:
		c.select()
		typ, data = c.list()	# Perform a LIST on the IMAP Server to trigger rebuild
		print 'RetValue:', typ
		print 'Data:', data
		c.logout()

	line = f.readline()
