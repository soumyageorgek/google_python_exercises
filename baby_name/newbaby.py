#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -we have to create a list['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
 -Fix main() to use the extract_names list
"""
def extract_names(path):
	dict={}
	f=open(path)
	year=re.findall(r'(\d+)',str(path))
	s=f.read()
	tuples=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',s)
	for tuple in tuples:
		dict[tuple[1]]=tuple[0]
		dict[tuples[2]]=tuple[0]


	list=sorted(dict,key=lambda x:dict[x])
	for x in list:
		year.append(str(x)+str(dict[x]))
	print year
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
	print 'usage is ./newbaby.py filename'
	para=sys.argv[1]#input file name
	extract_names(para)
	
if __name__ == '__main__':
	main()

