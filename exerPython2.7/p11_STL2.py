
import repr
print repr.repr(set('supercalifragilisticexpialidocious'))


import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]


import textwrap
doc = """The wrap() method is just like fill() except that it returns
 a list of strings instead of one big string with newlines to separate
 the wrapped lines."""

"""
#print textwrap.fill(doc, width=80)


from string import Template
tt = Template('${village}folk send $$10 to $cause.')
tt.substitute(village='Nottingham', cause='the ditch fund')
print tt

t3 = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
#t3.substitute(d) #Exception here
t3.safe_substitute(d)

import time, os.path
photo_files = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
#fmt = raw_input('Enter rename style (%d-date %n-seqnum %f-format):  ')
#Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f
fmt = "Ashley_%n%f"

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photo_files):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print '{0} --> {1}'.format(filename, newname)
"""

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print 'Finished background zip of: ', self.infile

"""
background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print 'The main program continues to run in foreground.'

background.join()    # Wait for the background task to finish
print 'Main program waited until background was done.'
"""

import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')