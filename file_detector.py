#!/usr/bin/env python

import os
import inotify.adapters
from config import *
import all


i = inotify.adapters.InotifyTree('/root/sample/tmp')

for event in i.event_gen():
    if event is not None:
	(header, type_names, watch_path, filename) = event
	if 'IN_MODIFY' in type_names:
	    print "WD=(%d) MASK=(%d) COOKIE=(%d) LEN=(%d) MASK->NAMES=%s WATCH-PATH=[%s] FILENAME=[%s]"\
                             %(header.wd, header.mask, header.cookie, header.len, type_names,
                             watch_path.decode('utf-8'), filename.decode('utf-8'))
	    all.is_webshell(watch_path + "/" + filename,"jsp")
