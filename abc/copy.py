#write a program to copy files of special pattern to a directory
#(here .py extension is considered)
#pattern matching done using regular expression
import re
import shutil
import os
def find_req_files():
  new_list=[]
  list=os.listdir('.')
  for x in list:
    match=re.search('\w+\.py$',x)
    if match:
      new_list.append(match.group())
  return new_list
def copy(dir):
  p=os.path.abspath(dir)
  if not os.path.exists(p):
    os.mkdir(dir)
  list=find_req_files() 
  for x in list:
    shutil.copy(x,dir)
copy('abc')     
    

