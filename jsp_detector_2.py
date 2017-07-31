#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import time
import hashlib
from config import *
import all
import sys
import datetime
import sqlite3
from time import sleep

def md5(string):
    return hashlib.md5(string).hexdigest()

def check_file_hash(filepath):
    content = open(filepath).read()
    cursor = conn.execute("select filename,hash_id,last_check  from file where filename='%s'"%filepath)
    old_hash = ""
    for row in cursor:
	old_hash = row[1]
    hash_id = md5(content)
    sleep(check_hash_span)
    if hash_id != old_hash:
	print "[!]File => " + filepath + " has been modified or created! " + old_hash + "|" + hash_id
	time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	conn.execute("insert into file (filename,hash_id,last_check) values ('%s','%s','%s')"%(filepath,hash_id,time))
	print hash_id
	conn.commit()
	return False
    return True	 

def init_database():
    conn = sqlite3.connect('file.db')
    conn.execute('''drop table if exists `file`;''')
    conn.execute('''create table file(
       filename  TEXT    NOT NULL,
       hash_id   TEXT  NOT NULL,
       last_check     CHAR(64));''')     
    conn.commit()
    conn.close() 

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

#if not os.path.isfile('file.db'):
#    init_database();
#conn = sqlite3.connect('file.db')
pathdir = sys.argv[1]
wis = 'jsp|jspx'
filepaths = []	    
for fpathe,dirs,fs in walklevel(pathdir,max_directory_depth):
    for f in fs:
        ppp = os.path.join(fpathe,f)
        if os.path.isfile(ppp) and re.match(r'^\.('+wis+')$',os.path.splitext(ppp)[1]):
            filepaths.append(ppp)
webshell = 0
ok_file = 0
res = []
for f in filepaths:
    shell_type,is_shell = all.is_webshell(f,"jsp")
    if  is_shell:
	webshell += 1
    else:
	ok_file += 1
	res.append(f)
    print webshell,ok_file,ok_file + webshell
    print "###################### REST #########################"
    sleep(time_span)

#print rule_hit
#print file_match_rule
#print res
print webshell,ok_file,ok_file + webshell
