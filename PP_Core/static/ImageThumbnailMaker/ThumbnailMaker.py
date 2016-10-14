'''
This program calls ImageRoutinesBasic to make a thumbnail for a particular image file

When an invention is put in the system, this program will take the image file as a commandline argument; a taxonomy of the Pillow accepted image file types is still needed.
'''

from subprocess import call
import sys

#could use Popen to get feedback, but at that point the damage is done.
#Restricting the accepted image file types on the sumbit is more practical because the user gets to put a good one in.
call(['python','ImageRoutinesBasic.py',sys.argv[1] ] )



