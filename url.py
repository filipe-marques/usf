#!/usr/bin/python3

#	Copyright 2014 Filipe Marques <eagle.software3@gmail.com>
#  
#	This program is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; either version 3 of the License, or
#	any later version.
#  
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#  
#	You received a copy of the GNU General Public License
#	along with this program in License folder; if not, write to the Free Software
#	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#	MA 02110-1301, USA.

# just helps with urls of sites, not yet terms of search

import platform
import webbrowser
import sys
import re

def debian_ubuntu():
	with open("url.txt","r") as file:
		urls = file.readlines()
	
	for element in urls:
		# substitui \n por '' espaço
		ele = re.sub('\n','',element)
		webbrowser.open_new_tab(ele)
        
def opensuse():
	with open("url.txt","r") as file:
		urls = file.readlines()
	
	for element in urls:
		# substitui \n por '' espaço
		ele = re.sub('\n','',element)
		webbrowser.open_new_tab(ele)

def main():
	# it returns a tuple
	system = platform.linux_distribution()
	# indexing the tuple
	if 'Ubuntu' in system[0]:
		debian_ubuntu()
	if 'openSUSE' in system[0]:
		opensuse()

if __name__ == "__main__":
    main()
    sys.exit()
