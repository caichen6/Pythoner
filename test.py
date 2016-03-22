#! /Users/caichen/.virtualenvs/pyenv/bin/python
print 'Hello Atom!'
import os
print os.popen('which python').readlines()
for i in range(1,5):
    cmd = 'ping 192.168.0.'+str(i)
    print cmd+':'+os.popen(cmd).readlines()
